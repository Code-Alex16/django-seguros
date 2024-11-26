from django.db import models
from Ciudad.models import Ciudad

# Create your models here.
class Clientes(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombres')
    dni = models.CharField(max_length=13, verbose_name='Ruc o cedula')
    email = models.EmailField(max_length=150, verbose_name='email', unique=True)
    address = models.TextField(verbose_name='direccion')
    phone = models.CharField(max_length=15,verbose_name='telefono')
    movil = models.CharField(max_length=15, verbose_name='celular')
    avatar = models.ImageField(upload_to='avatar', verbose_name='foto cliente', null=True, blank=True)
    city = models.ForeignKey(to=Ciudad, verbose_name='Ciudad', on_delete= models.CASCADE, null= True, blank=True)
    created = models.DateTimeField(auto_now=True, verbose_name='fecha de creacion')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='fecha de modificacion')
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'customers'
        ordering = ['id']

    def __str__(self) -> str:
        return self.name