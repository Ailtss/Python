def fibonacci(x):

    antipeultimo = 0
    penultimo = 1
    indice = 3
    
    while True:
        ultimo = antipeultimo+penultimo
        if ultimo > x:
            print("O valor passado: {} não está na sequência de fibonnaci".format(x))
            break

        elif ultimo == x:
            print("O valor passado: {} está na sequência de fibonnaci".format(ultimo))
            print("Posição: {}".format(indice))
            break
        else:
            antipeultimo = penultimo
            penultimo = ultimo
            indice +=1

def rec_fibonacci(posicao):
    
    if posicao == 1:
        return 0
    elif posicao == 2: 
        return 1
    else:
        return rec_fibonacci(posicao-1) +rec_fibonacci(posicao-2)






fibonacci(8)