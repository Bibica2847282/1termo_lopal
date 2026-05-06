# Projeto Cancela Automatica

# Projeto 1:
# Projeto: Precisamos de um algoritmo para gerenciamento de cancelas para um shopping.
# Toda entrada e saída irá ser sinalizada
# Valores para entrada e permanência do veículo deverá ser pergutado
# As entrada deverão ser registradas por placa.


# Passo 1:  
# Perguntar informações sobre o veiculo ou forma acesso
# Pressionar o botao para emitir ticket
# Verificar se possui TAG para acesso liberado
# Se possuir erros informar ao usuário


# Passo 2:
# Verificar tempo de permanência
# Valor a ser cobrado

# Passo 3:
# Saída como será?
# Calcular tempo de permanência
# Se for TAG gerar na fatura da TAG
# Pagar ticket
# Devolver ticket na saída


# Passo 4:
# Gerar relatório de entradas e saídas
# Tratamento de Erros
# Revisão do código

# def processar_entrada_veiculo():

#     print("----- Bem vindo(a) ao estacionamento ----- ")
    
#     placa_veic = input("Insira a placa e modelo do veiculo: ")

#     sist_veiculo = input("O veículo possui tag de acesso? (sim/nao): ").strip().lower()

#     if sist_veiculo == "sim":
#         print("Tag detectada. Acesso liberado! ")
    
#     elif sist_veiculo == "nao":
#         input("Pressione ENTER para emitir o ticket...")
#         print("Ticket emitido. Retire-o e a cancela irá abrir. ")
    
#     else:
#         print("Erro: Resposta inválida. Por favor, tente novamente ou chame o suporte no interfone.")


# processar_entrada_veiculo()

def processar_tempo_veiculo():

    metodo_tarifa = print("---- Hora da tarifa de estacionamento ---- ")

    placa_veic = input("Insira o metodo de pagamento: ")

    if metodo_tarifa == "Estacionamento": 

        hora_entrada = float(input("Digite o horário de entrada: "))
        valor_estacionamento = float(input("Digite o valor a cobrar: "))
        hora_saida = float(input("Digite a hora de saida: "))
        total_permanencia = hora_saida - hora_entrada
        valor_total = total_permanencia * valor_estacionamento
        print(f"Tempo: {total_permanencia} horas")
        print(f"Total a pagar: R$ {valor_total}")

    else: 
        print("ERRO: Resposta inválida. Por Favor, tente novamente! ")

processar_tempo_veiculo()