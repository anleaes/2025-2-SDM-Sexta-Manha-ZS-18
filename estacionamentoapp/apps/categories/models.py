from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100)

    def __str__(self):
        return self.name
    
class Estacionamento(models.Model):
    estacionamento_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150)
    capacidade_total = models.IntegerField()
    vagas_ocupadas = models.IntegerField(default=0)

    def __str__(self):
        return self.nome
    
class EnderecoEstacionamento(models.Model):
    endereco_id = models.AutoField(primary_key=True)
    rua = models.CharField(max_length=150)
    bairro = models.CharField(max_length=80)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=150, null=True, blank=True)

    estacionamento = models.ForeignKey(
        Estacionamento,
        on_delete=models.CASCADE,
        related_name="enderecos"
    )

    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.bairro}"

class Tarifa(models.Model):
    tarifa_id = models.AutoField(primary_key=True)
    valor_hora = models.DecimalField(max_digits=8, decimal_places=2)
    valor_diaria = models.DecimalField(max_digits=8, decimal_places=2)
    valor_mensal = models.DecimalField(max_digits=8, decimal_places=2)

    estacionamento = models.ForeignKey(
        Estacionamento,
        on_delete=models.CASCADE,
        related_name="tarifas"
    )

    class Meta:
        verbose_name = 'Tarifa'
        verbose_name_plural = 'Tarifas'
        ordering = ['tarifa_id']  # ordering deve usar o campo correto da classe

    def __str__(self):
        return f"Tarifa do Estacionamento {self.estacionamento.nome}"
