from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=False, max_length=30, )
    cpf = models.CharField(max_length=11, unique=True)
    rg = models.CharField(max_length=9)
    celular = models.CharField(max_length=14)
    ativo = models.BooleanField()
    objects = models.Manager() #This line code is only to resolve the false alert that VSCode had shown

    def __str__(self):
        return self.nome
