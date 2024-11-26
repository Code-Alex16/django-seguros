from django.db import models
from ClientesSF.models import Clientes

class Cotizador(models.Model):
    TIPO_POLIZA_CHOICES = [
        ('BUEN_USO', 'Buen uso del anticipo'),
        ('CUMPLIMIENTO', 'Cumplimiento de contrato'),
        ('FIDELIDAD', 'Fidelidad'),
        ('RESPONSABILIDAD', 'Responsabilidad civil'),
    ]

    customer = models.ForeignKey(to=Clientes,verbose_name='Cliente', on_delete=models.CASCADE)    
    vigencia = models.DateField(verbose_name="Vigencia", blank=True, null=True)
    plazo = models.PositiveIntegerField(verbose_name="Plazo (días)", blank=True, null=True)
    vencimiento = models.DateField(verbose_name="Vencimiento", blank=True, null=True)
    tipo_poliza = models.CharField(
        max_length=50,
        choices=TIPO_POLIZA_CHOICES,
        verbose_name="Tipo de Póliza",
        blank=True, null=True
    )
    valor_asegurado = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Valor Asegurado",  blank=True, null=True)
    tasa = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Tasa (%)",  blank=True, null=True)
    prima_minima = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prima Mínima", blank=True, null=True)
    prima = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prima", blank=True, null=True)
    super_banco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Super Banco (3,5%)", blank=True, null=True)
    derecho = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Derecho", blank=True, null=True)
    iva = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="IVA (15%)", blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total", blank=True, null=True)

    class Meta:
        verbose_name = 'Cotización'
        verbose_name_plural = 'Cotizaciones'
        db_table = 'tbl_cotizacion'
        ordering = ['id']

    def __str__(self):
        return f"{self.customer} - {self.get_tipo_poliza_display()}"


'''from decimal import Decimal
# Create your models here.

class QuoteOptions(models.TextChoices):
    SEGURO_VIDA = 'vida', 'Seguro de Vida'
    SEGURO_AUTOS = 'auto', 'Seguro de Autos'
    SEGURO_ROBOS = 'robo', 'Seguro de Robos'
    SEGURO_INCENDIOS = 'incendio', 'Seguro contra Incendios'

# Opciones para los plazos diferidos
class DiferiedOptions(models.TextChoices):
    TRES_MESES = '3_meses', '3 Meses'
    SEIS_MESES = '6_meses', '6 Meses'
    NUEVE_MESES = '9_meses', '9 Meses'
    DOCE_MESES = '12_meses', '12 Meses'

# Modelo para cotización
class Cotizador(models.Model):
    PRECIOS_BASE = {
        QuoteOptions.SEGURO_VIDA: 500.00,
        QuoteOptions.SEGURO_AUTOS: 800.00,
        QuoteOptions.SEGURO_ROBOS: 400.00,
        QuoteOptions.SEGURO_INCENDIOS: 1200.00,
    }

    Qutoe_number = models.IntegerField(verbose_name='N°', blank= True, null= True)
    quote_option = models.CharField(
        max_length=25,
        choices=QuoteOptions.choices,
        verbose_name='Concepto'
    )
    value = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        editable=False, 
        verbose_name='Valor',
        null= True,
        blank=True  # Se elimina la dependencia de `quote_option` en el valor por defecto
    )
    diferied = models.CharField(
        max_length=10, 
        choices=DiferiedOptions.choices, 
        verbose_name='Diferido',
        default=DiferiedOptions.TRES_MESES
    )
    prima = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        editable=False, 
        verbose_name='Prima'
    )
    imports = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        verbose_name='Impuesto (%)',
        default=12.5
    )
    value_to_pay = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        editable=False, 
        verbose_name='Valor a Pagar',
        default=0.0
    )
    created_quote = models.DateTimeField(auto_now=True, verbose_name='Fecha de Cotización')
    updated_quote = models.DateTimeField(auto_now_add=True, verbose_name='Última Actualización')
    customer = models.ForeignKey(
        to=Clientes, 
        verbose_name='Cliente', 
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Cotización'
        verbose_name_plural = 'Cotizaciones'
        db_table = 'tbl_cotizacion'
        ordering = ['id']

    def __str__(self):
        return f"{self.quote_option} - {self.customer}"

    def calcular_prima(self):
        """Calcula la prima en función del plazo diferido."""
        plazo = {
            DiferiedOptions.TRES_MESES: 3,
            DiferiedOptions.SEIS_MESES: 6,
            DiferiedOptions.NUEVE_MESES: 9,
            DiferiedOptions.DOCE_MESES: 12,
        }.get(self.diferied, 1)  # Por defecto 1 para evitar divisiones por cero
        return self.value / plazo

    def calcular_valor_total(self):
        """Calcula el valor total considerando la prima e impuesto."""
        # Asegúrate de que imports sea un decimal antes de la operación
        imports_decimal = Decimal(self.imports)  
        prima_decimal = Decimal(self.prima)
        return prima_decimal + (prima_decimal * imports_decimal / Decimal(100)) 

    def save(self, *args, **kwargs):
        """Sobrescribir el método save para asignar valores calculados."""
        # Asigna el valor base según la opción seleccionada, en lugar de usar el valor por defecto
        if not self.value:  # Solo asignar si 'value' no está ya asignado
            self.value = self.PRECIOS_BASE.get(self.quote_option, 0)
        
        # Calcula la prima
        self.prima = self.calcular_prima()
        
        # Calcula el valor total a pagar
        self.value_to_pay = self.calcular_valor_total()
        
        super().save(*args, **kwargs)
'''