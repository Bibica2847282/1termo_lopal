# 1. Registro de veiculos

def registrar_veiculo():
    # Nomes de variáveis descritivos em vez de 'm' ou 'p'
    modelo_veiculo = input("Digite o modelo do veículo: ")
    placa_veiculo = input("Digite a placa do veículo: ")

    # Uso de f-string para facilitar a leitura da mensagem
    print(f"\nVeículo {modelo_veiculo} de placa {placa_veiculo} registrado no sistema.")
    print("Boa viagem!")

# Execução do módulo
if __name__ == "__main__":
    registrar_veiculo()

# 2. Cálculo de autonomia

def calcular_distancia_maxima(capacidade_tanque, consumo_medio):
    """Calcula quantos km o veículo percorre com o tanque cheio."""
    return capacidade_tanque * consumo_medio

def executar_calculo_autonomia():
    print("--- Calculadora de Autonomia ---")
    
    # Conversão explícita de tipos para evitar erros de cálculo
    try:
        capacidade = float(input("Capacidade do tanque (litros): "))
        consumo = float(input("Consumo médio do caminhão (km/l): "))

        distancia_total = calcular_distancia_maxima(capacidade, consumo)

        print(f"\nCom o tanque cheio, o veículo pode percorrer {distancia_total:.2f} km.")
    
    except ValueError:
        print("Erro: Por favor, insira apenas valores numéricos.")

# Execução do módulo
if __name__ == "__main__":
    executar_calculo_autonomia()
    