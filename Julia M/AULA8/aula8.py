# Exercicios de Programação Python: "O Caça-Erros "

# 1. O problema da Idade:
# Erro

# idade = input("Digite sua idade: ")
# if idade >= 18:
#     print("Você é maior de idade.")

# Correto

# idade = float(input("Digite sua idade: "))
# if idade >= 18:
#     print("Você é maior de idade.")

# Melhorado 
# idade = float(input("Digite sua idade: "))
# if idade >= 18:
#     print("Você é maior de idade.")

# else:
#     print("Você é menor de idade. ")

# 2. A escrita fiel:
# erro
# nome = "Mariana"
# print("Seja bem-vinda, nome!")

# Corrigido 
# nome = "Mariana"
# print(f"Seja bem-vinda, {nome}!")

# Melhorado

# nome = input("Qual seu nome? ")
# print(f"Seja Bem-vindo (a), {nome}")

# 3. Falta de Espaço
# Errado

# numero = 10
# if numero > 5:
# print("O número é maior que cinco.")
# else:
# print("O número é menor ou igual a cinco.")

# Corrigido

# numero = 10
# if numero > 5:
#     print("O número é maior ou igual a cinco.")
# else:
#     print("O número é menor que cinco. ") 

# Melhorado

# numero = float(input("Qual o numero? "))

# if numero >= 5:
#     print("O número é maior ou igual a cinco.")
# else:
#     print("O número é menor que cinco.") 

# 4. Esquecimento fatal

# Errado

# usuario = "aluno123"
# if usuario == "aluno123"
#     print("Login realizado com sucesso.")

# Corrigido 

# usuario = "aluno123"
# if usuario == "aluno123":
#     print("Login realizado com sucesso! ")

# Melhorado 

# usuario = input("Digite o senha do usuario! ")
# if usuario == "aluno123":
#     print("Login realizado com sucesso! ")

# else:
#     print("Erro! Senha incorreta..")

# 5. Atribuição vs. Comparação

# Errado

# clima = "ensolarado"
# if clima = "chuvoso":
#     print("Leve um guarda-chuva!")

# Correto

# clima = "ensolarado"

# if clima == "chuvoso":
#     print("Leve um guarda-chuva!")

# Melhorado 

# clima = input("Como está o clima hoje? ")

# if clima == "Chuvoso":
#     print("Leve um Guarda-Chuva. ")

# elif clima == "Ensolarado":
#     print("Passe protetor e Beba bastante água. ")

# else:
#     print("Aproveite o dia! ")

# 6. Misturando Alhos com bugalhos

# Errado

# pontos = 50
# print("Parabéns! Você fez "+ pontos +" pontos. ")

# Correto

# pontos = 50
# print(f"Parabéns! Você fez {pontos} pontos.")

# Melhorado 

# pontos = int(input("Digite a quantidade de pontos: "))
# print(f"Parabéns! Você fez {pontos} pontos.")

# 7. A ordem dos fatores

# Errado

# O sistema deve dar "Excelente" para notas 9 ou 10.
# nota = 9.5
# if nota >= 7:
# print("Aprovado")
# elif nota >= 9:
# print("Excelente!")

# Correto

# O sistema deve dar "Excelente" para notas 9 ou 10.
# nota = 9
# if nota <= 7:
#     print("Aprovado")
# elif nota >= 9:
#     print("Excelente!")

# Melhorado

# nota = int(input("Qual nota você tirou de 0 a 10? "))
# if 5 < nota <= 8:
#     print("Aprovado")
# elif nota >= 9:
#     print("Excelente!")
# else:
#     print("Reprovado..")

# 8. O contador de 1 a 5

# Errado

# Objetivo: Mostrar na tela os números 1, 2, 3, 4 e 5.
# for i in range(5):
# print(i)

# Correto

# for i in range(1, 6):
#     print(i)

 # Melhorado

# balas = int(input("Seja Bem-Vindo ao mercadinho da Julia! Quantas balas gostaria de comprar? ")) 
# for i in range(1, balas + 1):
#     print(i)

# 9. O Loop Eterno

# tentativas = 1
# while tentativas <= 3:
# print("Tentando conectar...")
# O código deveria parar após 3 tentativas

# Correto

# tentativas = 1
# while tentativas <= 3:
#     print("Tentando conectar...")
#     tentativas += 1

# Melhorado

# tentativas = 1
# while tentativas <= 3:
#     print(f"Tentando conectar... (Tentativa {tentativas}/3)")
#     falha = True 
    
#     if falha:
#         resposta = input("Falha na conexão. Deseja tentar novamente? (sim/nao): ").lower()
#         if resposta != 'sim':
#             print("Encerrando.")
#             break
#     else:
#         print("Conectado com sucesso!")
#         break
    
#     tentativas += 1
# else:
#     print("Número máximo de tentativas atingido.")

# 10. A senha teimosa

#  Errado

# O programa deve pedir a senha até que o usuário digite "python123"
# senha = ""
# while senha == "python123":
# senha = input("Digite a senha secreta: ")
# print("Acesso concedido!")

# Correto

senha = ""

# Usamos o operador != (diferente de)
# O loop continuará rodando ENQUANTO a senha NÃO FOR "python123"

# while senha != "python123":
#     senha = input("Digite a senha secreta: ")

# print("Acesso concedido!") 

# Melhorado

# print("Seja bem-vindo! Faça login como administrador logando com a senha secreta! ")

# while senha != "python123":
#      senha = input("Digite a senha secreta: ")

# print("Acesso concedido!") 