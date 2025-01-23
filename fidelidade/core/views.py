from django.shortcuts import render
from .models import Customer, Configuration, Purchase

def index(request):
    config = Configuration.objects.first()
    if not config:
        config = Configuration.objects.create(points_per_real=1.0, progress_bar_max=100.0)

    selected_customer = None
    congratulation_message = None

    if request.method == "POST":
        if "search_name" in request.POST:  # Consulta de pontos por nome
            search_name = request.POST.get("search_name")
            selected_customer = Customer.objects.filter(name__iexact=search_name).first()
        else:  # Registro de compra
            name = request.POST.get("name")
            phone = request.POST.get("phone")
            amount_spent = float(request.POST.get("amount_spent"))

            # Obtém ou cria o cliente
            try:
                customer = Customer.objects.get(name=name)
                customer.phone = phone  # Atualiza o telefone, se necessário
            except Customer.DoesNotExist:
                customer = Customer.objects.create(name=name, phone=phone)

            # Atualiza os pontos do cliente
            customer.points += amount_spent * config.points_per_real

            # Verifica se o cliente atingiu o limite de pontuação
            if customer.points >= config.progress_bar_max:
                congratulation_message = f"Congratulations, {customer.name}! You've completed the progress bar."
                customer.points %= config.progress_bar_max  # Restante após zerar

            customer.save()

            # Registra a compra
            Purchase.objects.create(customer=customer, amount_spent=amount_spent)
            selected_customer = customer

    return render(request, 'index.html', {
        'selected_customer': selected_customer,
        'congratulation_message': congratulation_message,
        'points_per_real': config.points_per_real,
        'progress_bar_max': config.progress_bar_max
    })
