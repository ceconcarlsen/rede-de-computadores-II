"""
1.1
Construir todas as conversões binárias, héxadecimal e decimal manualmente
sem utilizar biblioteca já construída (existente),
pode ser orientada a objeto (class) ou função
"""

hex_table = ['0', '1', '2', '3', '4', '5', '6',
             '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

# [DECIMAL]


def decimalParaBinario(value):  # Função recursiva que
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


if __name__ == '__main__':
    print("[BINÁRIO PARA DECIMAL]")
    print('O valor em decimal e =', binarioParaDecimal(1111111011011))
    print("[BINÁRIO PARA HEXADECIMAL]")
    print('O valor em hexadecimal e =', binarioParaHexa(1010))
    print("[DECIMAL PARA HEXADECIMAL]")
    print('O valor em hexadecimal e =', decimalParaHexa(8))
    print("[DECIMAL PARA BINARIO]")
    print('O valor em binario e =', decimalParaBinario(8))
    print('[HEXADECIMAL PARA BINARIO]')
    print('O valor em binario e =', hexaParaBinario('A'))
    print('[HEXADECIMAL PARA DECIMAL')
    print('O valor em decimal e =', hexaParaDecimal('A'))
