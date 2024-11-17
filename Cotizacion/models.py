from django.db import models
from ClientesSF.models import Clientes

# Create your models here.

class QuoteOptions(models.TextChoices):
    SEGURO_VIDA = 'vida', 'seguro de vida'
    SEGURO_AUTOS = 'auto', 'Seguro de Autos'
    SEGURO_ROBOS = 'robo', 'Seguro de Robos'
    SEGURO_INCENDIOS = 'incendio', 'seguro contra incendios'


class Cotizacion(models.Model):

    customer = models.ForeignKey(to=Clientes, verbose_name='Cliente', on_delete= models.CASCADE)
    quote_option = models.CharField(max_length=25, choices= QuoteOptions.choices, verbose_name='Producto')
    created_quote = models.DateTimeField(auto_now=True, verbose_name='fecha de Cotizacion')
    updated_quote = models.DateTimeField(auto_now_add=True, verbose_name='fecha de la ultima Cotizacion')
    quote_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio Base', default=0)
    
    PRECIOS_BASE = {
        QuoteOptions.SEGURO_VIDA       : 500.00,
        QuoteOptions.SEGURO_AUTOS      :  800.00,
        QuoteOptions.SEGURO_ROBOS      : 400.00,
        QuoteOptions.SEGURO_INCENDIOS  :  1200.00
    }

    class Meta:
        verbose_name = 'Cotizacion'
        verbose_name_plural = 'Cotizaciones'
        db_table = 'tbl_cotizacion'
        ordering = ['id']

    def __str__(self) -> str:
        return self.quote_option
    
    def save(self, *args, **kwargs):
        """Sobrescribir el método save para asignar el precio de acuerdo con el tipo de cotización"""
        # Asigna el precio de acuerdo con la opción seleccionada en quote_option
        if not self.quote_price:  # Solo asigna si quote_price está vacío
            self.quote_price = self.PRECIOS_BASE.get(self.quote_option, 0)
        super().save(*args, **kwargs)