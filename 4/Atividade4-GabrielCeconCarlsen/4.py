# Atividade 4 - Conjunto de endereços IPv4 - Gabriel Cecon Carlsen - 181250969

import ipaddress  # https://docs.python.org/3/library/ipaddress.html
import random

network = ipaddress.IPv4Network('200.230.17.15/23', False)

# 1 - Ter a biblioteca em binário, decimal e Hexadecimal
hex_table = ['0', '1', '2', '3', '4', '5', '6',
             '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

# [DECIMAL]


def decimalParaBinario(value):
    if (value > 1):
        decimalParaBinario(value // 2)
    return value % 2


def decimalParaHexa(value):
    hexa = ''
    while(value > 0):
        aux = value % 16
        hexa = hex_table[aux] + hexa
        value = value//16

    return hexa

# [BINÁRIO]


def binarioParaDecimal(value):
    expo = 1
    dec_value = 0
    while(value):
        digito = value % 10
        value = int(value / 10)

        dec_value += digito * expo
        expo = expo * 2
    return dec_value


def binarioParaHexa(value):
    dec_value = binarioParaDecimal(value)
    hexa = ''
    while(dec_value > 0):
        aux = dec_value % 16
        hexa = hex_table[aux] + hexa
        dec_value = dec_value//16

    return hexa

# [HEXADECIMAL]


def hexaParaDecimal(value):
    return int(value, 16)


def hexaParaBinario(value):
    return bin(int(value, 16))


"""
2 - Para o endereço 200.230.17.15/23 é necessário ter:
2.1 - Uma rede com 64 hosts
2.2 - Uma rede com 70 hosts
2.3 - Uma rede com 15 hosts
2.4 - Uma rede com 14 hosts

EX: 192.168.1.0/24, necessário ter 30 hosts

1º Determinar o tamanho das sub-redes (número mágico)
30 + 2 = 32

2º Determinar o prefixo das sub-redes
256 - 32 = 224, ou seja, máscara 255.255.255.224 = /27

3º Escrever a lista de sub-redes, começando no ip original /prefixo do 2º passo e ir somando número
mágico do 1º passo
-192.168.1.0/27
-192.168.1.32/27
-192.168.1.64/27
-192.168.1.96/27
-192.168.1.128/27
-192.168.1.160/27
-192.168.1.192/27
-192.168.1.224/27 
"""
# lista de sub-redes com pelo menos 64 hosts, passando o novo prefixo (RFC 1878)
lista_de_redes = list(network.subnets(
    new_prefix=25))
print("Rede com 64 hosts: ",
      lista_de_redes[random.randrange(0, len(lista_de_redes))])  # escolhendo uma rede da lista de redes com pelo menos 64 hosts

# lista de sub-redes com pelo menos 70 hosts, passando o novo prefixo (RFC 1878)
lista_de_redes = list(network.subnets(new_prefix=25))
print("Rede com 70 hosts: ",
      lista_de_redes[random.randrange(0, len(lista_de_redes))])  # escolhendo uma rede da lista de redes com pelo menos 70 hosts

# lista de sub-redes com pelo menos 15 hosts, passando o novo prefixo (RFC 1878)
lista_de_redes = list(network.subnets(new_prefix=27))
print("Rede com 15 hosts: ",
      lista_de_redes[random.randrange(0, len(lista_de_redes))])  # escolhendo uma rede da lista de redes com pelo menos 15 hosts

# lista de sub-redes com pelo menos 14 hosts, passando o novo prefixo (RFC 1878)
lista_de_redes = list(network.subnets(new_prefix=28))
print("Rede com 14 hosts: ",
      lista_de_redes[random.randrange(0, len(lista_de_redes))])  # escolhendo uma rede da lista de redes com pelo menos 14 hosts

"""
3 - Demonstre o IP da rede;
4 - Demonstre o IP de Broadcast;
5 - Demonstre o conjunto de IP's da sub-rede com 64 hosts.
"""
print("\nDemonstre o IP da rede: ", network.network_address)
print("Demonstre o IP de Broadcast: ", network.broadcast_address)
print('Demonstre o conjunto de IPs da sub-rede com 64 hosts: ',
      list(network.subnets(new_prefix=25)))
