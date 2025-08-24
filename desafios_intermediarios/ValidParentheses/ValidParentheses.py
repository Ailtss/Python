def isValid(string: str) -> bool:

    pilha = []

    pares = {
        ')' : '(',
        ']' : '[',
        '}' : '{'
    }

    for s in string:
        if s in pares:
            if not pilha or pilha.pop() != pares[s]: # Se a pilha não estiver vazia ou o topo for diferente, return false
                return False
        else:
            pilha.append(s)

    return not pilha

string = "()"

b = isValid(string)

print(b)