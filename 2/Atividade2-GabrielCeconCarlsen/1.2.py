import ipaddress
import time
"""
1.2 - Esse programa deve ser capaz de identificar um IPv4 CIDR, nas seguintes características:
1.2.1 - Dado o IP 27.15.100.128/17
1.2.2 - Qual o intervalo de endereço de host ?
1.2.3 - Qual o endereço de difusão/transmissão/broadcast?
1.2.4 - Qual a máscara da sub-rede ?
1.2.5 - Notações de CIDR ?
1.2.6 - Qual o ID da rede (número da rede)?
1.2.7 - Qual o número de hosts posso ter nessa rede?
"""

# /17 representa a notação CIDR, que indidca 17 bits para identificar a rede do endereço
ip = input('Digite um IP valido:')
network = ipaddress.IPv4Network(ip, False)

# Outra forma de expressar/representar a rede do IP
print("\nMascara de sub-rede: ", network.netmask)

# Permite que a informação seja passada em uma subnet
print("\nEndereço de broadcast", network.broadcast_address)

# Número total de endereçamentos da rede
print("\nNumero de hosts da rede: ", network.num_addresses)

# Sub-divisões da rede
print("\nSubnets:")
for subnet in network.subnets(prefixlen_diff=2):
    print(subnet)
# Combinação de todas as subnets
print("\nSupernet:", network.supernet(prefixlen_diff=1))

print("\n\n\nO programa terminará em 30 segundos...")
time.sleep(30)
