# Generated by Django 5.1.2 on 2024-11-04 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombres')),
                ('dni', models.CharField(max_length=13, verbose_name='Ruc o cedula')),
                ('email', models.EmailField(max_length=150, unique=True, verbose_name='email')),
                ('address', models.TextField(verbose_name='direccion')),
                ('phone', models.CharField(max_length=15, verbose_name='telefono')),
                ('movil', models.CharField(max_length=15, verbose_name='celular')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatar', verbose_name='foto cliente')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='fecha de creacion')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='fecha de modificacion')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'db_table': 'tbl_customers',
                'ordering': ['id'],
            },
        ),
    ]
