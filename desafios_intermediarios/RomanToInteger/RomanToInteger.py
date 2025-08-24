
def romanToInt(s:str) -> int:

    romanos = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    sum = 0

    tamanho = len(s)

    for i in range(tamanho):

        valor_atual = romanos.get(s[i])

        if (i+1) < tamanho and romanos.get(s[i+1]) > valor_atual:
            sum -= valor_atual
        else:
            sum += valor_atual
    
    return sum


print(romanToInt("MCMXCIV"))