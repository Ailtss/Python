"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""


"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

import re
import random

def calculo_digito(cpf):
    
    if len(cpf) != 9:
        print ("São necessários 9 valores entre 0 e 9, para darmos prosseguimento!")
        return
    
    soma_digito_1 = 0
    soma_digito_2 = 0
    
    #Cálculo primeiro dígito
    for c, peso in zip(cpf[:9], range(10,1,-1)):
        soma_digito_1 += int(c) * peso
    
    primeiro_digito = (soma_digito_1*10) % 11
    
    if primeiro_digito > 9:
        primeiro_digito = 0
    
    print("O primeiro digito para o CPF: {}, seria {}".format(cpf, primeiro_digito))
    cpf += str(primeiro_digito)
    
    #Cálculo segundo dígito
    for c, peso in zip(cpf[:10], range(11,1,-1)):
        soma_digito_2 += int(c) * peso
    
    segundo_digito = (soma_digito_2*10) % 11
    
    if segundo_digito > 9:
        segundo_digito = 0
    
    print("O segundo digito para o CPF: {}, seria {}".format(cpf, segundo_digito))
    cpf += str(segundo_digito)

    return cpf

#Checar se o CPF possui dígitos repetidos
def cpf_repetido(cpf):
    cpf_tratado = re.sub(
        r'[^0-9]',
        '',
        cpf
    )

    igual = True

    primeiro_digito = cpf_tratado[0]

    # for c in cpf_tratado[1:]:
    #     if c != primeiro_digito:
    #         igual = False
    #         break

    if (primeiro_digito*len(cpf_tratado)) != cpf_tratado:
        igual = False
    
    return igual

        


def gerador_cpf():

    valores = ""

    for _ in range(9):
        valores += str(random.randint(0,9))

    if not cpf_repetido(valores):
        return calculo_digito(valores)
        








# cpf = input("Digite o CPF: ")

# if cpf_repetido(cpf):
#     print("O CPF possui dígitos iguais!")
# else:
#     calculo_digito(cpf)

cpf = gerador_cpf()
print("Novo cpf gerado: {}".format(cpf))