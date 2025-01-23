from django.db import models

class Configuration(models.Model):
    points_per_real = models.FloatField(default=1.0)
    progress_bar_max = models.FloatField(default=100.0)  # Máximo da barra de progresso

    def __str__(self):
        return f"Config: {self.points_per_real} points/real, {self.progress_bar_max} max bar"

class Customer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=15)
    points = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

class Purchase(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='purchases')
    amount_spent = models.FloatField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.name} - {self.amount_spent} - {self.date}"
