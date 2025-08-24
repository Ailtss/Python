def longestCommonPrefix(lista: list[str]) -> str:

    for i, word in enumerate(lista):
        lista[i] = word.lower()

    prefixo = lista[0]
    primeira_letra = lista[0][0]

    for palavra in lista[1:]:
        #while palavra.find(prefixo) != 0:
        while not palavra.startswith(prefixo):
            prefixo = prefixo[:-1]
            if not prefixo:
                return ""
    return prefixo




lista = ["flower","flow","flight"]
print("Prefixo comun entre as palavras: {}".format(longestCommonPrefix(lista)))