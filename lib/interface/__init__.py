def Menu():
    linha()
    print('Digite uma das seguintes opções:')
    print('[ 1 ] - Validar CPF')
    print('[ 2 ] - Gerar CPF')
    print('[ 3 ] - Sair')
    linha()
    option = int(input('>>> '))
    linha()
    return option


def linha():
    print('-'*43)


def MenuPrincipal():
    print('Digite uma das seguintes opções:')
    print('[ 1 ] - CPF')
    print('[ 2 ] - CNPJ')
    print('[ 3 ] - Sair')
    linha()
    option = int(input('>>> '))
    linha()
    return option


def MenuCnpj():
    linha()
    print('Digite uma das seguintes opções:')
    print('[ 1 ] - Validar CNPJ')
    print('[ 2 ] - Gerar CNPJ')
    print('[ 3 ] - Sair')
    linha()
    option = int(input('>>> '))
    linha()
    return option
