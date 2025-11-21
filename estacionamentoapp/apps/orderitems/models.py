from django.db import models
from products.models import Product
from orders.models import Order
# Create your models here.
class Orderitem(models.Model):
    quantity = models.PositiveIntegerField('Quantidade',null=True, blank=True,default=0)
    unitary_price = models.DecimalField('Preco unitario', max_digits=10, decimal_places=2)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('order', 'product')
        verbose_name = 'Item de pedido'
        verbose_name_plural = 'Itens de pedido'
        ordering =['id']

    def __str__(self):
        return f"{self.quantity} - {self.product.name}"