from django.db import models
from categories.models import Category, Estacionamento

# Create your models here.
class Product(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100)
    date_fabrication = models.DateField('Data Fabricacao', auto_now=False, auto_now_add=False) 
    is_active = models.BooleanField('Ativo', default=False)
    photo = models.ImageField('Foto', upload_to='photos', null=True, blank=True)
    doc = models.FileField('Documentos', upload_to='docs', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name  # Método correto para retornar o nome do produto


class Vaga(models.Model):
    vaga_id = models.AutoField(primary_key=True)
    numero = models.IntegerField()
    tipo_vaga = models.CharField(max_length=50)
    status = models.BooleanField(default=True)  

    estacionamento = models.ForeignKey(
        Estacionamento,
        on_delete=models.CASCADE,
        related_name="vagas"
    )

    def __str__(self):
        return f"Vaga {self.numero} - {self.tipo_vaga}"  # Método correto para descrição da vaga

    class Meta:
        verbose_name = 'Vaga'
        verbose_name_plural = 'Vagas'
        ordering = ['vaga_id']  # Usando 'vaga_id' para ordenação
