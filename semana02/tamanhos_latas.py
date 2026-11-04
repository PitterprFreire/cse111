
import math

def calcular_volume(raio, altura):
    
    resultado_volume = math.pi * (raio ** 2) * altura
    return resultado_volume

def calcular_eficiencia_de_custo(volume, custo):
    
    custo_eficiente = volume / custo
    return custo_eficiente

def calcular_area_da_superficie(raio, altura):
    
    resultado_area_superfice = (2 * math.pi * raio) * (raio + altura)
    return resultado_area_superfice

def calcular_eficiencia_de_armazenamento(raio, altura):

    resultado_volume = calcular_volume(raio, altura)
    resultado_area = calcular_area_da_superficie(raio, altura)
    resultado_eficiencia = resultado_volume / resultado_area
    return resultado_eficiencia

def main():
    lista_tipos_lata = {
    1: {"nome": "#1 Piquenique", "raio": 6.83, "altura": 10.16, "custo": 0.28},
    2: {"nome": "#1 Grande", "raio": 7.78, "altura": 11.91, "custo": 0.43},
    3: {"nome": "#2", "raio": 8.73, "altura": 11.59, "custo": 0.45},
    4: {"nome": "#2.5", "raio": 10.32, "altura": 11.91, "custo": 0.61},
    5: {"nome": "#3 Cilindro", "raio": 10.79, "altura": 17.78, "custo": 0.86},
    6: {"nome": "#5", "raio": 13.02, "altura": 14.29, "custo": 0.83},
    7: {"nome": "#6Z", "raio": 5.40, "altura": 8.89, "custo": 0.22},
    8: {"nome": "#8Z pequena", "raio": 6.83, "altura": 7.62, "custo": 0.26},
    9: {"nome": "#10", "raio": 15.72, "altura": 17.78, "custo": 1.53},
    10: {"nome": "#21", "raio": 16.83, "altura": 12.38, "custo": 0.34},
    11: {"nome": "#300", "raio": 7.62, "altura": 11.27, "custo": 0.38},
    12: {"nome": "#303", "raio": 8.10, "altura": 11.11, "custo": 0.42}
    }

    melhor_eficiencia = 0
    item_eficiente = ""
    
    item_custo = ""
    melhor_custo = float('inf')
    
    print()
    for codigo_item, tipo_lata in lista_tipos_lata.items():
        
        eficiencia = calcular_eficiencia_de_armazenamento(tipo_lata['raio'], tipo_lata['altura'])
        custo = calcular_eficiencia_de_custo(calcular_volume(tipo_lata['raio'], tipo_lata['altura']),tipo_lata['custo'])
        
        print(f"A Eficiência do item: '{tipo_lata['nome']}' é de {eficiencia:.2f}. O seu custo é de R$ {custo:.2f} por volume.")
    
        if melhor_eficiencia < eficiencia:
           melhor_eficiencia = eficiencia
           item_eficiente = tipo_lata['nome']
        
        if custo < melhor_custo:
           melhor_custo = custo
           item_custo = tipo_lata['nome']
               
    print()
    print(f"E o item que teve a melhor eficiência foi: '{item_eficiente}' com o valor de {melhor_eficiencia:.2f}.")
    print(f"E o item que teve a melhor Eficiência em Custo foi: '{item_custo}' com o valor de R$ {melhor_custo:.2f}.")
    print()

main()

