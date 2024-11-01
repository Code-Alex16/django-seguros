# Generated by Django 5.1.2 on 2024-10-29 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ruc', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('address_person', models.CharField(blank=True, max_length=250, null=True)),
                ('type_person', models.CharField(blank=True, choices=[('Natural', 'Natural'), ('Sociedad', 'Sociedad')], max_length=10, null=True)),
                ('genero_person', models.CharField(blank=True, choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Otro', 'Otro')], max_length=10, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
            ],
        ),
    ]
