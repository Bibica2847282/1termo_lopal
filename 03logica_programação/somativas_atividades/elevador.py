# Sistema de Elevador de Prédio

# O prédio possui 10 andares, sendo o térreo o andar 0. O elevador pode se mover para cima ou para baixo, e tem a capacidade de transportar até 5 pessoas.

# O elevador começa no andar 0 e pode ser chamado por qualquer pessoa em qualquer andar. 

# O elevador deve se mover para o andar onde a pessoa chamou, e depois para o andar destino da pessoa. 

# O elevador deve exibir mensagens indicando o andar atual, o número de pessoas no elevador, e as ações realizadas (subindo, descendo, parando). O programa deve continuar rodando até que o usuário decida encerrar. 

print("Bem-vindo ao sistema do elevador! ")

andares = 10
capacidade = 5
andar_atual = 0

while True:
    try:
           
        destino = int(input("Digite o andar de destino: (0-10) "))
        pessoas = int(input("Quantas pessoas tem no elevador? "))

        if pessoas > 5:
                print("Sinto muito! O elevador está cheio, espere um momento...")
                break

        elif 0 >= pessoas <= 5:
                print("Bem-vindo ao elevador! ")
        if destino < 0 or destino > 10:
            raise ValueError("Andar inválido! Por favor, digite umvalor entre 0 e 10...")
            
        print(f"Elevador se movendo do andar {andar_atual} para o andar {destino}... ")
        andar_atual = destino
        print(f"Chegamos ao andar {andar_atual}! ")

        if input("Deseja escolher outro andar? (s/n): ").lower() != 's':
                print("Obrigada por usar o elevador! Até a próxima! ")
                break
        for listagem in range(11):
                print(f"Andar {listagem} - {'[X]' if listagem == andar_atual else '[ ]'} ")

    except ValueError:
        print()