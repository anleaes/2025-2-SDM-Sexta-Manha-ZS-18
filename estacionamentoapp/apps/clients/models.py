from django.db import models
from socialnetworks.models import Socialnetwork
# Create your models here.
class Client(models.Model):
    Client_id = models.AutoField(primary_key=True)
    cpf = models.CharField('CPF', max_length=14,)
    idade = models.IntegerField('Idade')
    ativo = models.BooleanField('Ativo')
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, null=True, blank=True)

    # CAMPOS ANTIGOS DA ATIVIDADE 
    first_name = models.CharField('Nome', max_length=50)
    last_name = models.CharField('Sobrenome', max_length=100) 
    address = models.CharField('Endereco', max_length=200)   
    cell_phone = models.CharField('Telefone celular', max_length=20)
    email = models.EmailField('E-mail',null=False, blank=False)
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    )
    gender = models.CharField('Genero', max_length=1, choices=GENDER_CHOICES)
    socialnetwork = models.ManyToManyField(Socialnetwork, verbose_name="Redes Socias")

class Veiculo(models.Model):
    veiculo_id = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    placa = models.CharField(max_length=10, unique=True)
    cor = models.CharField(max_length=30)

    cliente = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="veiculos")

    def __str__(self):
        return f"{self.modelo} - {self.placa}"
    
class EnderecoCliente(models.Model):
    endereco_id = models.AutoField(primary_key=True)
    rua = models.CharField(max_length=150)
    bairro = models.CharField(max_length=80)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=150, null=True, blank=True)

    # Relacionamento com Cliente
    cliente = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="enderecos")

    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.bairro}"

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering =['cliente_id']

    def __str__(self):
        return self.first_name

