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
        


cpf = gerador_cpf()
print("Novo cpf gerado: {}".format(cpf))
