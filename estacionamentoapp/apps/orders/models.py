from django.db import models
from clients.models import Client
# Create your models here.
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
        ordering =['id']

    def __str__(self):
        return "%s" % (self.client) 