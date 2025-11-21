from django.db import models
from clients.models import Client
from products.models import Vaga
from clients.models import Veiculo, Client

# Evite os imports diretos e use strings no campo ForeignKey
class Order(models.Model):
    payment_method = models.CharField('Forma de Pagamento', max_length=30, choices=[
        ('boleto', 'Boleto'),
        ('cartao', 'Cartão de Crédito'),
        ('pix', 'PIX'),
    ])
    status = models.CharField('Status', max_length=20, default='andamento', choices=[
        ('andamento', 'Em andamento'),
        ('finalizado', 'Finalizado'),
        ('cancelado', 'Cancelado'),
    ])
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['id']

    def __str__(self):
        return "%s" % (self.client)

    
class Reserva(models.Model):
    reserva_id = models.AutoField(primary_key=True)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    aprovado = models.BooleanField(default=False)

    vaga = models.ForeignKey(
        Vaga,
        on_delete=models.CASCADE,
        related_name="reservas"
    )

    veiculo = models.ForeignKey(
        Veiculo,
        on_delete=models.CASCADE,
        related_name="reservas"
    )

    cliente = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name="reservas"
    )

    def __str__(self):
        return f"Reserva {self.reserva_id} - Cliente {self.cliente.first_name}"
