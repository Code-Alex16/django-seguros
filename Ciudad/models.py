from django.db import models

# Create your models here.

class Ciudad(models.Model):
    province = models.CharField(max_length=20, verbose_name='Provincia')
    name_city = models.CharField(max_length=20, verbose_name='Ciudad')

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
        db_table = 'tbl_city'
        ordering = ['id']

    def __str__(self) -> str:
        return self.name_city
    
