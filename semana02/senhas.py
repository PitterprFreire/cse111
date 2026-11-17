"""Criatividade 1 -> Coloquei um TRY EXCEPT na função "procurar_palavra" quando o arquivo consultado não existir. 
                     Alé da mensagem de erro do Python, antes disso eu mostro o que de fato aconteceu
    Criatividade 2-> Deixei um pouco o visual de retorno para o cliente mais clean, respeitando os retornos obrigatórios """

import os

################################################################################################################################################################
#Listas com os caracteres a serem utilizados no código

MINUSCULAS=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
MAIUSCULAS=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITOS=["0","1","2","3","4","5","6","7","8","9"]
ESPECIAIS=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", '"', "'", ",", ".", "<", ">", "?", "/", "`", "~"]

################################################################################################################################################################

def procurar_palavra(palavra, nome_do_arquivo, maiusculas_e_minusculas = False):

    #Fazendo a leitura do nome_do_arquivo
    diretorio_atual = os.path.dirname(__file__)
    caminho_arquivo = os.path.join(diretorio_atual, nome_do_arquivo)
    
    try:

        with open(caminho_arquivo, "r", encoding="utf-8") as lista_arquivo:
            arquivo_carregado = [linha_lida.strip() for linha_lida in lista_arquivo]

    except FileNotFoundError:
        print(f"\nAtenção: O arquivo de validação '{nome_do_arquivo}' não foi encontrado!")
        print("A validação não pode prosseguir sem a base de dados de segurança necessária.\n")
        raise
        #Fazendo alógica de aplicação da validação da palavra com o arquivo
    if not maiusculas_e_minusculas:
        palavra = palavra.lower()
    
    for linha in arquivo_carregado:
        linha_comparar = linha if maiusculas_e_minusculas else linha.lower()

        if palavra == linha_comparar:
            return True
    
    return False
### --------------------------------------------------------------------------------------------------------------------
def palavra_tem_caractere(palavra, lista_caracteres):
    
    for letra in palavra:
        if letra in lista_caracteres:
            return True
   
    return False
### --------------------------------------------------------------------------------------------------------------------
def calcular_complexidade(palavra):

    pontuacao = 0
    
    if palavra_tem_caractere(palavra, MINUSCULAS):
        pontuacao += 1
    
    if palavra_tem_caractere(palavra, MAIUSCULAS):
        pontuacao += 1

    if palavra_tem_caractere(palavra, DIGITOS):
        pontuacao += 1

    if palavra_tem_caractere(palavra, ESPECIAIS):
        pontuacao += 1

    return pontuacao

### --------------------------------------------------------------------------------------------------------------------
def validar_senha(senha, comprimento_min = 10, comprimento_forte = 16):

    if procurar_palavra(senha, "dicionario.txt", False):
        print("A senha está no dicionário e não é segura.")
        return 0

    elif procurar_palavra(senha, "senhas_mais_comuns.txt", True):
        print("A senha é comumente usada e não é segura.")
        return 0

    elif len(senha) < comprimento_min:
        print("A senha é muito curta e não é segura.")
        return 1
    
    elif len(senha) >= comprimento_forte:
        print("A senha é longa, o comprimento supera a complexidade e é uma boa senha.")
        return 5
    else:
        return 1 + calcular_complexidade(senha)
    
### --------------------------------------------------------------------------------------------------------------------
def main():
    
    print()
    print("Seja bem vindo ao validador de Senha!")

    while True:
        senha = input("Por favor, digite sua senha: ")            
        
        if senha == "q" or senha == "Q":
            print("Obrigado pelos testes. Até mais!")
            break
        else:
            print()
            validacao_senha = validar_senha(senha)
            print(f"Força da senha é: {validacao_senha}")
            print("=============================================================================")
            print("\nCaso deseje sair do programa, digite somente a letra 'q' ou 'Q' abaixo..")

################################################################################################################################################################

#Executando o programa

if __name__ == "__main__":
    main()