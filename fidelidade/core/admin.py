from django.contrib import admin
from .models import Customer, Configuration, Purchase

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'points', 'get_purchase_dates')

    def get_purchase_dates(self, obj):
        return ", ".join([purchase.date.strftime('%Y-%m-%d') for purchase in obj.purchases.all()])
    get_purchase_dates.short_description = "Purchase Dates"

@admin.register(Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ('points_per_real', 'progress_bar_max')

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('customer', 'amount_spent', 'date')
    list_filter = ('date',)
