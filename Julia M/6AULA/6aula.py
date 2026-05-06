# Clean Code - Aula 6
# Para que usar?
# Como usar? 
# print("Clean Code - Aula 6 ")
# aula = 6
# print(f"Estamos na aula {aula} de Clean Code. ")

# Manipulação de arquivos e textos 
# texto = "  Python é muito legal  "
# print(texto.strip().upper())
# print(texto.strip().lower())
# print(texto.strip().capitalize())
# print(texto.strip().title())
# print(texto.strip().replace(" ", "_"))
# print(texto.strip().split())

# Escrevendo..
# with open ("notas.txt",  "w") as arquivo:
#     arquivo.write("Estudar Python hoje! ")
#     arquivo.write("\nLer sobre Clean Code. ")


# # Lendo..
# with open ("notas.txt", "r") as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)

# # Exercicio 1 
# # Crie um programa que peça ao usuário para inserir a frase e. em seguida, exiba a frase com as seguintes transformações:
# # - Remova os espaços extras no inicio e no final da frase.

# frase = input("Digite sua frase: ")
# print(frase.strip().upper())

# Exercicio 2 
# Crie um programa que leia o conteúdo de um arquivo de texto e conte quantas vezes a palavra "Python" aparece no arquivo. Exiba o resulado para o usuário.

print("Contagem de palavras em arquivos ")
with open("notas.txt", "r") as arquivo:
    conteudo = arquivo.read()
    quantidade = conteudo.count("Python")
    print(f"A contagem de palavras {quantidade} foi de...")