import os

LISTAS_CARACTERES_MINUSCULAS=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
LISTAS_CARACTERES_MAIUSCULAS=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
LISTAS_CARACTERES_DIGITOS=["0","1","2","3","4","5","6","7","8","9"]
LISTAS_CARACTERES_ESPECIAIS=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", '"', "'", ",", ".", "<", ">", "?", "/", "`", "~"]

lista_caracteres = []

def funcao_unificando_lista(lista, tipo_caracter, lista_acumuladora):
    for linha in lista:
        lista_acumuladora.append((linha, tipo_caracter))
    return lista_acumuladora
    
funcao_unificando_lista(LISTAS_CARACTERES_MINUSCULAS, "minuscula", lista_caracteres)
funcao_unificando_lista(LISTAS_CARACTERES_MAIUSCULAS, "maiuscula", lista_caracteres)
funcao_unificando_lista(LISTAS_CARACTERES_DIGITOS, "digito", lista_caracteres)
funcao_unificando_lista(LISTAS_CARACTERES_ESPECIAIS, "especial", lista_caracteres)


for i in lista_caracteres:
    print(i)
