# exercicio 1
# tente criar um codigo que conte de 1 a 10, mas use o continue para não imprimir o número 5 (simulando uma falha de sensor específica no item 5).
# leituras = [1, 2, 3, 4, "5", 6, 7, 8, 9, 10 ]
# for numero in leituras:
#     if numero != "5":
#         print(f" {numero} ")
#         continue
#     print(f"falha de sensor {numero}.")

# for sensor in range(1,11):
#         if sensor ==5:
#             print(f"Sensor n°{sensor}com falha")
#         print(f"Sensor n°{sensor}sem falha")
#         continue
# print("Fim")


# exercicio2
# simule um semaforo com parada para cada cor. Determine um tempo que deseja para quando mudar para tal cor ele represente uma pausa para cada cor.Use o oontinue para pular a cor amarela(simulando um semaforo com defeito que nao acende a luz amarela ).
# import time
# cores = ["vermelho", "amarelo", "verde"]

# for cor in cores:
#       if cor =="amarelo":
#        print(f"Semáforo com defeito, pulando a cor {cor}...")   
#        continue   
#       print(f"Semáforo na cor {cor}. parando por 3 segundos...")
#       time.sleep(3)
# print("Fim do ciclo")

# exercio3 soma de cargas de energia (for)
# uma fabrica tem 5 maquinas. Peça ao usuario (via input dentro do loop)
# o consumo de kwh de cada uma das 5 maquinas ao final do loop, o programa deve exibir o consumo total da fabrica

# maquinas = ["1", "2", "3","4", "5",]
# for maquina in "1":
  

#   total_consumo=0
#   for maquina in range(1,6):
#     consumo = float(input(f"Digite o consumo em kwh da máquina {maquina}:"))
#     total_consumo += consumo
# print(f"O consumo total da fábrica é de {total_consumo} kwh .")


# exercicio 4 identificador de peças defeituosas (for + if)
# percorra uma lista de medidas de peças
# medidas =50.1, 49.8, 52.0, 50.0, 48.5
# o padrao de qualidades aceita apenas peças com exatamente 50.0 ou mais.
# usse um for para ler a lista e, para cada peça, diga se ela está "aprovada" ou "rejeitada"

# pecas= [50.1, 49.8, 52.0, 50.0, 48.5]
# for medida in pecas:
#   if medida >= 50.0:
#     print(f"peça com medida {medida}mm: Aprovada")
#   else:
#     print(f"Peça com medida {medida}mm: Rejeitada")
# print("Fim da avaliação de peças.")



# exercicio 5 uma balança industrial está pesando um lote de 6 sacos de insumos. O peso ideal de cada saco é 50kg, mas o sistema aceita variações.
# crie um programa que peça ao usuario o peso de cado saco (via input dentro do loop) e, para cada um, informe se ele está "dentro do limite"(entre 48kg e 52kg) ou fora do limite
# no final, exiba quantos sacos estão dentro do limite
  
# sacos_d1=0
# for saco in range(1,7):
#      peso = float(input(f"Digite o peso {saco}:"))
# if 48 <= peso <= 52:
#     print(f"Saco {saco} com peso {peso}kg: Dentro do limite")
#     sacos_d1 += 1
# else:
#      print(f"Saco {saco} com peso {peso}kg: fora do limite")
# print(f"Quantidade de sacos dentro do limite: {sacos_d1}")



# o desafio gestao de ciclo termico 
# voce deve criar um programa que monitore a temperatura de uma estufa que processa um lote de 5 peças
# regras do sistema 
# o programa deve rodar em um loop até que 5 peças validas sejam processadas
# para cada peça peça ao usuario a temperatura atual input
# Filtro de erro (continue) se o usuario digitar uma temperatura negativa exiba "erro de leitura no sensor" e use o continue para pedir a temperatura novamente ( essa leitura nao conta como peça processada).
# paradara de emergencia (break) Se a temperatura for maior qu 150, o sistema deve exibir
# "Alerta critico: risco de explosão!", interromper o loop imediatamente e encerrar o programa.


# lote_t=0
# import time
# temperatura = 1
# while temperatura < 150:
#     for lote in range(1,6):lote + float (input(f"digite a temperatura do lote{lote}"))
#     if 0 <= temperatura <= 150
# ciclo = 0
# while ciclo < 5:
#     temperatura = float(input(f'Digite a temperatura da peça {ciclo + 1} em °C:'))

#     if temperatura < 0:
#         print ("Erro de leitura do Sensor. Por favor, digite uma temperatura valida.")
#         continue

#     if temperatura > 150:
#         print("ALERTA CRÍTICO: Risco de explosão!")
#         break
    
#     print(f"Peça {ciclo + 1} processada com temperatura {temperatura}°C.")
#     ciclo += 1

#     print(f"Peça {ciclo} processada com sucesso. temperatura dentro do limite.")
# print("Fim do monitoramento de temperatura.")

# exercicio 6
#  contador de peças com falha while + if + continuem em uma linha de produçao deve Contar quantas peças com falha foram detectadas o usuario deve digitar sim para indicar que uma peça tem falha e nao para indicar que esta de boa o programa deve continuar pedindo a condiçao da peça ate que o usuario digite fim no final exiba total

# total_falhas = 0

# print("Monitoramento de Linha de Produção ")
# print("Digite 'sim' para falha, 'nao' para ok ou 'fim' para encerrar.")

# while True:
#     status = input("A peça possui falha? ").lower().strip()

#     if status == "fim":
#         break

#     if status == "nao":
#         print("Peça aprovada. Continuando...")
#         continue

#     if status == "sim":
#         total_falhas += 1
#         print("Falha registrada!")
#     else:
#         print("Comando inválido. Tente 'sim', 'nao' ou 'fim'.")

# print("-" * 30)
# print(f"Produção encerrada. Total de peças com falha: {total_falhas}")