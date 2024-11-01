from django.db import models

# Create your models here.

class Cliente(models.Model):
    # el id se autogenera en django, y es auto_incrementable por defecto
    
    #Objetos de seleccion (tipo de persona, genero)
    TYPE_PERSON_CHOICES = [
        ('Natural', 'Natural'),
        ('Sociedad', 'Sociedad')
    ]

    GENERO_PERSON_CHOICES = [
        ('Masculino','Masculino'),
        ('Femenino', 'Femenino'),
        ('Otro', 'Otro')
    ]

    name = models.CharField(max_length=100)
    ruc = models.CharField(unique=True, max_length=13, null= True, blank= True)
    email = models.EmailField(unique=True, max_length=100)
    phone = models.CharField(max_length=15)
    address_person = models.CharField(max_length=250, null= True, blank= True)
    type_person = models.CharField(max_length=10,choices=TYPE_PERSON_CHOICES, null= True, blank= True)
    genero_person = models.CharField(max_length=10,choices=GENERO_PERSON_CHOICES, null= True, blank= True)

    #Avatar (si es una imagen), sera opcional y se guardara en un fichero avatars/...
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
