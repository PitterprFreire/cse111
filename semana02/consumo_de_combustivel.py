def main():
  # Obtém do usuário o valor inicial do odômetro em quilômetros.
  # Obtém do usuário o valor final do odômetro em quilômetros
  # Obtém do usuário a quantidade de combustível em litros.
  # Chama a função quilometros_por_litro, calcula o consumo em
  # quilômetros por litro e armazena
  # o resultado em uma variável chamada kml.
  # Chama a função milhas_por_galao para converter o valor 
  # de quilômetros em milhas, de litros em galões e calcular
  # o consumo em milhas por galão.
  # Armazena o resultado em uma variável chamada mpg.
  # Exibe os resultados para o usuário.
  #pass
  valor_inicial_odometro = float(input("Qual o valor inicial do odômetro em quilômetros? "))
  valor_fim_odometro = float(input("Qual o valor final do odômetro em quilômetros? "))
  valor_combustivel_usado = float(input("Qual a quantidade de combustível consumida em litros? "))

  consumo_quilometros = quilometros_por_litro(valor_inicial_odometro, valor_fim_odometro, valor_combustivel_usado)
  consumo_galao = milhas_por_galao(valor_inicial_odometro, valor_fim_odometro, valor_combustivel_usado)

  print(f"O consumo por quilômetros foi de {consumo_quilometros:.1f} por litro...")
  print(f"O consumo por milhas foi de {consumo_galao:.2f} por galão...")
  
def quilometros_por_litro(valor_inicial, valor_final, quantidade_de_litros):
  """ 
  Calcula e retorna o consumo em quiLômetros por litro
  Parâmetros
    valor_inicial: O valor inicial do odômetro em quilômetros.
    valor_final: O valor final do odômetro em quilômetros.
    quantidade_de_litros: A quantidade de combustível em litros.
  Retorna: Consumo de combustível em quilômetros por litro.
  """
  resultado_quilometro = (valor_final - valor_inicial) / quantidade_de_litros
  return resultado_quilometro
 
def  milhas_por_galao(valor_inicial, valor_final, quantidade_de_litros):
  """
  Converte litros e quilômetros para galões e milhas
  e retorna o consumo em milhas por galão
  Parâmetros
      valor_inicial: O valor inicial do odômetro em quilômetros
      valor_final: O valor final do odômetro em quilômetros
      quantidade_de_litros: A quantidade de combustível em litros
  Retorna: Consumo de combustível em milhas por galão.
  """
  resultado_milhas = (valor_final - valor_inicial) / 1.609
  resultado_galao = quantidade_de_litros * 0.26417
  resultado_final_milhas = resultado_milhas / resultado_galao
  return resultado_final_milhas
 
# Chama a função main para que
# o programa seja executado.
main()