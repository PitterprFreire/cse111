# Exemplo 5
import math
# Define uma função chamada main.
def main():
  # Obtém o raio e a altura do usuário.
  raio = float(input("Digite o raio de um cilindro: "))
  altura = float(input("Digite a altura de um cilindro: "))
  # Calcula o volume do cilindro.
  volume = math.pi * raio**2 * altura
  # Exibe o volume do cilindro.
  print(f"Volume: {volume:.2f}")
# Inicia este programa
# chamando a função main.
main()