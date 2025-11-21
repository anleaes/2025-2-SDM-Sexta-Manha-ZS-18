from django.db import models
from products.models import Product

# Evite o import circular, referenciando os modelos como strings
class Orderitem(models.Model):
    quantity = models.PositiveIntegerField('Quantidade', null=True, blank=True, default=0)
    unitary_price = models.DecimalField('Preço unitário', max_digits=10, decimal_places=2)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE)  # Usando string para resolver o circular import

    class Meta:
        unique_together = ('order', 'product')
        verbose_name = 'Item de pedido'
        verbose_name_plural = 'Itens de pedido'
        ordering = ['id']

    def __str__(self):
        return f"{self.quantity} - {self.product.name}"

class Pagamento(models.Model):
    pagamento_id = models.AutoField(primary_key=True)
    tipo_metodo = models.CharField(max_length=30, choices=[
        ('pix', 'PIX'),
        ('cartao', 'Cartão de Crédito'),
        ('boleto', 'Boleto'),
    ])
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateTimeField(auto_now_add=True)
    aprovado = models.BooleanField(default=False)

    # Usando string para resolver o circular import
    reserva = models.ForeignKey('orders.Reserva', on_delete=models.CASCADE, related_name="pagamentos")

    def __str__(self):
        return f"Pagamento {self.pagamento_id} - Reserva {self.reserva.reserva_id}"
