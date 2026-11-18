
import random


def main():

    
    lista_de_numeros_aleatorio = []
    lista_de_palavras_aleatorio = []
    quantidade_aleatorio = 1

    #Chamando a primeira vez a função:
    anexar_numeros_aleatorios(lista_de_numeros_aleatorio)
    print(lista_de_numeros_aleatorio)

    #Chamando a segunda vez a função:
    anexar_numeros_aleatorios(lista_de_numeros_aleatorio, quantidade_aleatorio)
    print(lista_de_numeros_aleatorio)

    #Chamando a primeira vez a função:
    anexar_palavras_aleatorias(lista_de_palavras_aleatorio)
    print(lista_de_palavras_aleatorio)
    
    #Chamando a segunda vez a função:
    anexar_palavras_aleatorias(lista_de_palavras_aleatorio, quantidade_aleatorio)
    print(lista_de_palavras_aleatorio)

def anexar_numeros_aleatorios(lista_de_numeros, quantidade = 1):

    for i in range(quantidade):
        numero_aleatorio = random.uniform(0, 100)
        numero_aleatorio_arredondado = round(numero_aleatorio, 1)
        lista_de_numeros.append(numero_aleatorio_arredondado)

def anexar_palavras_aleatorias(lista_palavras, quantidade = 1):

    lista = ["lua", "sol", "céu", "passaros", "cachorro", "leão", "urso", "computador", "geladeira", "sofa", "mesa", "cadeira"]

    for i in range(quantidade):

        palavra = random.choice(lista)
        lista_palavras.append(palavra)

if __name__ == "__main__":
    main()