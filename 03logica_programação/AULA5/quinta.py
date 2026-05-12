# 1. Perfil de Gamer: Peça o nick (nome) do jogador e o nível atual. Exiba: "O
# jogador [nick] está no nível [nível] e pronto para a partida!"

nick = input("Qual é o nome do jogador? ")
nivel = int(input("Qual é o seu nível? "))

print(f"O jogador {nick} está no nível {nivel} e pronto para a partida! ")

#  2. Calculadora de Mesada: Peça o valor que o aluno ganha por semana e
# multiplique por 4 para mostrar quanto ele terá no final do mês.

print("Bem-vindo(a) ao contador de mesada!")

pergunta1 = int(input("Qual o valor da sua mesada semanalmente? "))
valor = pergunta1 * 4

print("O valor da sua mesada mensalmente é: " , valor)

# 3. Conversor de Internet: Peça um valor em Gigabytes (GB) e converta para
# Megabytes (MB) (multiplique por 1024).

print("Bem-vindo(a) ao conversor de internet!")

pergunta1 = int(input("Qual o valor em Gigabytes? "))
valor = pergunta1 * 1024

print(f"O valor em Megabytes é: " , valor)

# 4. Média de Notas: Peça as notas de Matemática e Português. Calcule e mostre a
# média final.

print("Bem-vindo(a) a soma de seu boletim!")

pergunta1 = int(input("Qual sua nota em  português? "))
pergunta2 = int(input("Qual sua nota em matemática? "))
valor = pergunta1 + pergunta2 
total = valor /2

print("A sua média final é: " , total)


# 5. Seguidores: Peça a quantidade de seguidores atuais e quantos novos seguidores
# o aluno ganhou hoje. Exiba o total atualizado.

seguidoresatuais = int(input("Quantos seguidores você tinha antes? "))
novosseguidores = int(input("Quantos seguidores você ganhou hoje? "))

total = seguidoresatuais + novosseguidores

print(f"Parabéns! Seu total atualizado é de {total} seguidores.") 

# 6. Idade em Dias: Peça a idade do aluno e calcule aproximadamente quantos dias
# ele já viveu (idade * 365).

pergunta1 = int(input("Qual sua idade? "))
total = pergunta1 * 365

print("Você já viveu por aproximadamente", total, "dias")

# 7. Cosumo de lanche: Peça o preço do salgado e o preço do suco, no final exiba o total da compra.

print("Bem-vindo(a) a nossa lanchonete! ")

pergunta1 = float("Você comeu um salgado e um suco, qual o preço do salgado? ")
pergunta2 = float("E do suco? ")
soma = pergunta1 + pergunta2

print("O valor total gastado foi de:", soma)

# 8. Ano de Nascimento: Peça o ano atual e a idade do aluno. Calcule e exiba o ano
# em que ele nasceu.

pergunta1 = int(input("Digite o ano atual "))
pergunta2 = int(input("Digite sua idade "))
total = pergunta1 - pergunta2

print("O ano em que você nasceu é: " , total)

# 9. Filtro de Idade (TikTok): Peça a idade do usuário. Se for menor que 13, exiba
# "Acesso restrito". Se tiver entre 13 e 17, "Acesso moderado". Se for 18 ou
# mais, "Acesso liberado".

pergunta1 = int(input("Qual sua idade? "))

if pergunta1 < 13:
    print("Acesso Restrito!!!")

elif 13 < pergunta1 < 17:
    print("Acesso Moderado!")

else:
    print("Acesso Liberado!")

# 10.Bateria do Celular: Crie um while que começa com a bateria em 100. A cada
# repetição, subtraia 10 e mostre: "Bateria em [valor]%". O loop para quando
# chegar em 10 e exibe: "Por favor, conecte o carregador!".

bateria = 100

while bateria > 10:
    print(f"Bateria em {bateria}%")
    bateria -= 10

print(f"Bateria em {bateria}% ")
print("Por favor, conecte o carregador!")

# 11. Contagem de Curtidas: Use um for para simular a contagem de curtidas em uma
# foto. Peça ao usuário o limite de curtidas (ex: 5). O programa deve contar de 1 até
# esse número, printando: "Curtida no [i] recebida!".

limite = int(input("Digite o limite de curtidas: "))

for i in range(1, limite + 1):
    print(f"Curtida nº {i} recebida!")

# 12.Carrinho de Compras Online: Use um while para pedir nomes de produtos que o
# aluno quer comprar. O loop só para quando ele digitar "sair". No final, mostre
# quantas vezes ele adiciona itens ao carrinho (use um contador).

contador = 0
produto = ""

print("Carrinho de Compras Online ")
print("(Digite 'sair' para finalizar a compra)")

while produto.lower() != "sair":
    produto = input("Digite o nome do produto: ")
    contador += 1
if produto.lower() != "sair":
        print(f"Produto '{produto}' adicionado ao carrinho!")

print(f"Compra finalizada! Você adicionou {contador-1} itens ao seu carrinho.")