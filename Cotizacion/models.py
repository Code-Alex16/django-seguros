from django.db import models

# Create your models here.

class Cotizacion(models.Model):
    name_cotizacion = models.CharField(max_length=35, verbose_name='cotizacion')
    
    class Meta:
        verbose_name = 'Cotizacion'
        verbose_name_plural = 'Cotizaciones'
        db_table = 'tbl_cotizacion'
        ordering = ['id']

    def __str__(self) -> str:
        return self.name_cotizacion