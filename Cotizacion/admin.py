from django.contrib import admin
from .models import Cotizacion
# Register your models here.

@admin.register(Cotizacion)
class CotizacionAdmin(admin.ModelAdmin):
    list_display = ('customer', 'quote_option', 'quote_price', 'created_quote', 'updated_quote')
    list_filter = ('quote_option',)
