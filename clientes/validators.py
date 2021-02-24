import re

def cpf_valido(numero_do_cpf):

    return len(numero_do_cpf) == 11

def nome_valido(nome_do_cliente):
    
    return nome_do_cliente.isalpha()

def rg_valido(numero_do_rg):

    return len(numero_do_rg) == 9

def celular_valido(numero_do_celular):
    #informa se o número do telefone está dentor do padrão (12 12345-1234)

    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'

    resposta = re.findall(modelo, numero_do_celular)

    return resposta