from Validador_e_Gerador_de_CPF.lib import funcoes, interface
from time import sleep

import re
while True:
    option_principal = interface.MenuPrincipal()
    if option_principal == 1:
        while True:
            option = interface.Menu()
            if option == 1:
                while True:
                    try:
                        numero = input('Digite o CPF: ')
                        numero = re.sub(r'[^0-9]', '', numero)
                        numero = int(numero)
                        print(funcoes.ValidarCPF(numero))
                        interface.linha()
                    except:
                        print('CPF inválido. Tente Novamente!')
                        interface.linha()
                    option2 = input('Quer continuar [S/N]? ').upper()
                    if option2[0] == 'N':
                        break
                    interface.linha()
            elif option == 2:
                while True:
                    print(f'Um novo CPF foi gerado: {funcoes.formataCPF(funcoes.GerarCPF())}')
                    option2 = input('Quer continuar [S/N]? ').upper()
                    if option2[0] == 'N':
                        break
                    interface.linha()
            elif option == 3:
                break
            else:
                print('Opção inválida. Tente novamente!')
    elif option_principal == 2:
        while True:
            option = interface.MenuCnpj()
            if option == 1:
                while True:
                    try:
                        numero = input('Digite o CNPJ: ')
                        funcoes.valida(numero)
                    except:
                        print('CNPJ inválido. Tente Novamente!')
                        interface.linha()
                    option2 = input('Quer continuar [S/N]? ').upper()
                    if option2[0] == 'N':
                        break
                    interface.linha()
            elif option == 2:
                while True:
                    cnpj = funcoes.gera()
                    print(f'Um novo CNPJ foi gerado: {cnpj}')
                    option2 = input('Quer continuar [S/N]? ').upper()
                    if option2[0] == 'N':
                        break
                    interface.linha()
            elif option == 3:
                break
            else:
                print('Opção inválida. Tente novamente!')
    elif option_principal == 3:
        option2 = input('Tem certeza que quer sair [S/N]? ').upper()
        if option2[0] == 'S':
            interface.linha()
            print('Encerrando programa...')
            sleep(2)
            break
    else:
        print('Opção inválida. Tente novamente!')