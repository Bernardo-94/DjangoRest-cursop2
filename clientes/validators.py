import re
from validate_docbr import CPF


#A função abaixo informa se o número do CPF inserido é valido
def cpf_valido(numero_do_cpf):
    
    cpf = CPF()

    return cpf.validate(numero_do_cpf)

def nome_valido(nome_do_cliente):
    
    return nome_do_cliente.isalpha()

def rg_valido(numero_do_rg):

    return len(numero_do_rg) == 9

#A função abaixo informa se o número do telefone está dentro do padrão (12 12345-1234)
def celular_valido(numero_do_celular):

    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'

    resposta = re.findall(modelo, numero_do_celular)

    return resposta