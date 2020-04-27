from random import randint


def ValidarCPF(cpf):
    cpf = str(cpf).strip()
    soma1 = soma2 = 0
    for pos, c in enumerate(range(10, 1, -1)):
        mult = c * int(cpf[pos])
        soma1 += mult

    validador = 11 - (soma1 % 11)

    if validador > 9:
        digito1 = 0
    else:
        digito1 = validador

    novo_cpf = cpf[:9] + str(digito1)

    for pos, c in enumerate(range(11, 1, -1)):
        mult = c * int(novo_cpf[pos])
        soma2 += mult

    validador = 11 - (soma2 % 11)

    if validador > 9:
        digito2 = 0
    else:
        digito2 = validador

    novo_cpf = novo_cpf + str(digito2)
    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)
    if novo_cpf == cpf and not sequencia:
        return f'O {cpf} é válido!'
    else:
        return f'O {cpf} é inválido!'


def GerarCPF():
    cpf = randint(100000000, 999999999)
    cpf = str(cpf)
    soma1 = soma2 = 0
    for pos, c in enumerate(range(10, 1, -1)):
        mult = c * int(cpf[pos])
        soma1 += mult

    validador = 11 - (soma1 % 11)

    if validador > 9:
        digito1 = 0
    else:
        digito1 = validador

    novo_cpf = cpf[:9] + str(digito1)

    for pos, c in enumerate(range(11, 1, -1)):
        mult = c * int(novo_cpf[pos])
        soma2 += mult

    validador = 11 - (soma2 % 11)

    if validador > 9:
        digito2 = 0
    else:
        digito2 = validador

    novo_cpf = novo_cpf + str(digito2)
    return novo_cpf


def formataCPF(cpf):
    novo_cpf = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
    return novo_cpf

