from django.db import models

# Create your models here.

class Ciudad(models.Model):
    nombre = models.CharField(max_length=35, verbose_name='Ciudad', default='Manta')
    codigo_postal = models.CharField(max_length=10, verbose_name='Codigo Postal')

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
        db_table = 'tbl_city'
        ordering = ['id']

    def __str__(self) -> str:
        return self.nombre
    
