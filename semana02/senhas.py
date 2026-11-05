import os

################################################################################################################################################################

#Criando as variaveis e listas do programa

#Listas
lista_caracteres = []
dicionario = []
senhas_comun = []

#variaveis
tipo_caracter = None

################################################################################################################################################################

#Criando as listas baseado nos arquivos

#Mapeando os caminhos do arquivo
diretorio_atual = os.path.dirname(__file__)
caminho_arquivo_dicionario = os.path.join(diretorio_atual, "dicionario.txt")
caminho_arquivo_senha_comun = os.path.join(diretorio_atual, "senhas_mais_comuns.txt")


with open(caminho_arquivo_dicionario, "r", encoding="utf-8") as dicionario:
    arquivo_dicionario = [linha_lida_dicionario.strip() for linha_lida_dicionario in dicionario]

with open(caminho_arquivo_senha_comun, "r", encoding="utf-8") as senhas_comun:
    arquivo_senhas_comun = [linha_lida_senhas_comun.strip() for linha_lida_senhas_comun in senhas_comun]

################################################################################################################################################################

#Criando as funções para o programa
def funcao_unificando_lista(lista, tipo_caracter, lista_acumuladora):

    for linha in lista:
        lista_acumuladora.append((linha, tipo_caracter))

def procurar_palavra(palavra, nome_do_arquivo, maiusculas_e_minusculas):
    pass

def palavra_tem_caractere(palavra, lista_caracteres):
    
    verificar_palavra_tem_caractere = None

    for index in range(len(palavra)):
        if palavra[index] in LISTAS_CARACTERES_MINUSCULAS:
           verificar_palavra_tem_caractere = True
           break
        elif palavra[index] in LISTAS_CARACTERES_MAIUSCULAS:
            verificar_palavra_tem_caractere = True
            break
        elif palavra[index] in LISTAS_CARACTERES_MAIUSCULAS:
            verificar_palavra_tem_caractere = True
            break
        elif palavra[index] in LISTAS_CARACTERES_MAIUSCULAS:
            verificar_palavra_tem_caractere
            break
        else:
            verificar_palavra_tem_caractere = False
            break
    
    return verificar_palavra_tem_caractere
    
    pass

def calcular_complexidade(palavra):
    pass

def validar_senha(senha, comprimento_min, comprimento_forte):
    pass

def main():
    
    print()
    print("Seja bem vindo ao validador de Senha!")
    senha = input("Por favor, digite sua senha: ")

    #verificar_procurar_palavra = procurar_palavra(senha, arquivo_dicionario,    )
    
    pass


################################################################################################################################################################

#Unificando as listas em uma unica

LISTAS_CARACTERES_MINUSCULAS=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
LISTAS_CARACTERES_MAIUSCULAS=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
LISTAS_CARACTERES_DIGITOS=["0","1","2","3","4","5","6","7","8","9"]
LISTAS_CARACTERES_ESPECIAIS=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", '"', "'", ",", ".", "<", ">", "?", "/", "`", "~"]
    
funcao_unificando_lista(LISTAS_CARACTERES_MINUSCULAS, "minuscula", lista_caracteres)
funcao_unificando_lista(LISTAS_CARACTERES_MAIUSCULAS, "maiuscula", lista_caracteres)
funcao_unificando_lista(LISTAS_CARACTERES_DIGITOS, "digito", lista_caracteres)
funcao_unificando_lista(LISTAS_CARACTERES_ESPECIAIS, "especial", lista_caracteres)

################################################################################################################################################################

#Executando o programa

if __name__ == "__main__":
    main()