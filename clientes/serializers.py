from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':"O CPF deve conter 11 dígitos"})
        
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':"Ponha somente letras nesse campo"})
        
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':"RG deve conter 9 dígitos"})
        
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':"O celular deve conter de 11 a 14 dígitos"})

        return data

    