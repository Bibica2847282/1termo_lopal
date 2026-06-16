# Você foi contratado para desenvolver o módulo de validação de empréstimos de livros de uma biblioteca comunitária. O sistema precisa coletar os dados do usuário, do livro e decidir se o empréstimo será aprovado, negado ou se haverá cobrança de taxa de segurança.

# print("--- SISTEMA DE EMPRÉSTIMO DA BIBLIOTECA ---")

# print("\n[1] Aluno")
# print("[2] Comunidade Geral")
# perfil = input("Escolha o tipo de usuário (1 ou 2): ").strip()

# categoria_livro = input("O livro é da categoria 'Raros'? (S/N): ").strip().upper()
# dias_desejados = int(input("Por quantos dias deseja ficar com o livro?: "))

# emprestimo_aprovado = True
# taxa_adicional = 0.0
# motivo_negado = ""

# if categoria_livro == "S" and perfil == "2":
#     emprestimo_aprovado = False
#     motivo_negado = "Livros da categoria 'Raros' não podem ser emprestados para a Comunidade Geral."

# else:
#     if perfil == "1":
#         limite_gratis = 14
#     elif perfil == "2":  
#         limite_gratis = 7
#     else:
#         emprestimo_aprovado = False
#         motivo_negado = "Tipo de usuário inválido."

#     if emprestimo_aprovado and dias_desejados > limite_gratis:
#         dias_adicionais = dias_desejados - limite_gratis
#         taxa_adicional = dias_adicionais * 5.00

# print("\n" + "="*40)
# print("             RESULTADO FINAL             ")
# print("-"*40)

# if emprestimo_aprovado:
#     print("Status: EMPRÉSTIMO APROVADO! :)")
#     if taxa_adicional > 0:
#         print(f"Observação: Foram solicitados dias adicionais além do seu limite gratuito.")
#         print(f"Taxa de segurança a ser paga: R$ {taxa_adicional:.2f}")
#     else:
#         print("Observação: Empréstimo dentro do prazo gratuito. Sem taxas adicionais.")
# else:
#     print("Status: EMPRÉSTIMO NEGADO! ")
#     print(f"Motivo: {motivo_negado}")

# print("="*40)