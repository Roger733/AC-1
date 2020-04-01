from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


class Cliente(models.Model):
    TIPO_CHOICES = (
        ("Carro", "Carro"),
        ("Moto", "Moto"),
         )

    nome = models.CharField(max_length=255)
    Modelo_Veiculo = models.CharField(max_length=100, null=False, blank=False)
    Placa_Veiculo = models.CharField(max_length=100, null=False, blank=False)
    tipo = models.CharField(
        max_length=10,
        choices= TIPO_CHOICES,
        )
    email = models.EmailField(null=False, blank=False)
    profissao = models.CharField(max_length=50, null=False, blank=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)   # data de quando foi inserido
    updated_at = models.DateTimeField(auto_now=True)      # data de quando foi alterado

    def __str__(self):
        return self.nome


   
