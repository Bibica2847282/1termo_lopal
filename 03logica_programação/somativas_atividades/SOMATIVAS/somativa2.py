# QUESTÃO 01
# Registro de Operador: Peça o nome do operador e o turno (A, B ou C). Exiba:
# "Operador [Nome] registrado no Turno [Turno]. Boa jornada!"

# import tkinter as tk
# from tkinter import messagebox

# def operador_usuario():
#     nome = campo_nome.get()
#     turno = campo_turno.get().upper().strip() 

#     if nome == "":
#         messagebox.showwarning("Aviso", "Por favor, digite o nome do operador!")
#     elif turno == "":
#         messagebox.showwarning("Aviso", "Por favor, digite o turno (A, B ou C)!")
#     elif turno not in ["A", "B", "C"]:
#         messagebox.showerror("Erro", "Turno inválido! Digite apenas A, B ou C.")
#     else:
#         messagebox.showinfo("Registro Concluído", f"Operador {nome} registrado no Turno {turno}.\nBoa jornada!")

# app = tk.Tk()
# app.title("Questão 01 - Registro de Operador ")
# app.geometry("500x350")       
# app.configure(bg="#fdd5f1")   

# lbl_nome = tk.Label(app, text="Nome do Operador:", bg="#ee35c0", fg="white", font=("Arial", 11))
# lbl_nome.pack(pady=(20, 5)) 

# campo_nome = tk.Entry(app, font=("Arial", 12), justify="center") 
# campo_nome.pack(pady=5)

# lbl_turno = tk.Label(app, text="Turno (A, B ou C):", bg="#ee35c0", fg="white", font=("Arial", 11))
# lbl_turno.pack(pady=(15, 5)) 

# campo_turno = tk.Entry(app, font=("Arial", 12), justify="center") 
# campo_turno.pack(pady=5)

# btn_enviar = tk.Button(app, text="Registrar", command=operador_usuario, bg="#ee35c0", fg="white", font=("Arial", 11), width=12)
# btn_enviar.pack(pady=(20, 5))

# btn_fechar = tk.Button(app, text="Fechar", command=app.destroy, bg="#ee35c0", fg="white", font=("Arial", 11), width=12)
# btn_fechar.pack(pady=5)

# app.mainloop()

# --------------------------------------------------------------------------------------------------------------------------

# QUESTÃO 02
# Cálculo de Produção: Peça a quantidade de peças produzidas em 1 hora. Calcule e
# exiba quantas peças serão produzidas em um turno de 8 horas.

# import tkinter as tk
# from tkinter import messagebox

# def produção_peças():
#     pecas = campo_pecas.get()

#     if campo_pecas.get() == "":
#         messagebox.showwarning("Aviso", "Digite o número de peças produzidas em uma hora!")
#     else:
#         pecas = int(campo_pecas.get())
#         total = pecas * 8
#         messagebox.showinfo("Cálculo de Peças", f"Em um turno de 8 horas o total de peças produzidas será de {total} peças.")

# app = tk.Tk()
# app.title("Questão 02 - Cálculo de Produção ")
# app.geometry("500x350")       
# app.configure(bg="#fdd5f1")   

# lbl_pecas = tk.Label(app, text="Digite o número de peças produzidas em uma hora:", bg="#ee35c0", fg="white", font=("Arial", 11))
# lbl_pecas.pack(pady=20)    

# campo_pecas = tk.Entry(app, font=("Arial", 12), justify="center")
# campo_pecas.pack(pady=5)

# btn_enviar = tk.Button(app, text="Enviar", command=produção_peças, bg="#ee35c0", fg="white", font=("Arial", 11), width=10)
# btn_enviar.pack(pady=(20, 5))

# btn_fechar = tk.Button(app, text="Fechar", command=app.destroy, bg="#ee35c0", fg="white", font=("Arial", 11), width=10)
# btn_fechar.pack(pady=5)

# app.mainloop()

# --------------------------------------------------------------------------------------------------------------------------

# QUESTÃO 03
# Conversor de Unidade: O sistema lê uma pressão em Bar. Converta para PSI (1 Bar ≈ 14.5 PSI) e exiba com duas casas decimais.

# import tkinter as tk
# from tkinter import messagebox

# def pressão_bar():
#     if campo_bar.get() == "":
#         messagebox.showwarning("Aviso", "Digite o número de Bar!")
#     else:
#         bar = float(campo_bar.get().replace(",", ".")) 
#         total = bar * 14.5
#         messagebox.showinfo("Inversor de Bar", f"Convertendo de Bar para PSI a pressão será de {total:.2f} PSI.")

# app = tk.Tk()
# app.title("Questão 03 - Conversor de Unidade ")
# app.geometry("500x350")       
# app.configure(bg="#fdd5f1")   

# lbl_bar = tk.Label(app, text="Digite o número de Bar:", bg="#ee35c0", fg="white", font=("Arial", 11))
# lbl_bar.pack(pady=20) 

# campo_bar = tk.Entry(app, font=("Arial", 12), justify="center") 
# campo_bar.pack(pady=5)

# btn_enviar = tk.Button(app, text="Enviar", command=pressão_bar, bg="#ee35c0", fg="white", font=("Arial", 11), width=10)
# btn_enviar.pack(pady=(20, 5))

# btn_fechar = tk.Button(app, text="Fechar", command=app.destroy, bg="#ee35c0", fg="white", font=("Arial", 11), width=10)
# btn_fechar.pack(pady=5)

# app.mainloop()

# --------------------------------------------------------------------------------------------------------------------------

# QUESTÃO 04
# Média de Qualidade: Peça 3 notas de inspeção de uma peça (0 a 10). Exiba a média aritmética simples delas.

# import tkinter as tk
# from tkinter import messagebox

# def campo_media():
#     n1 = campo_nota1.get().strip()
#     n2 = campo_nota2.get().strip()
#     n3 = campo_nota3.get().strip()

#     if n1 == "" or n2 == "" or n3 == "":
#         messagebox.showwarning("Aviso", "Por favor, digite as três notas!")
#     else:
#         try:
#             nota1 = float(n1.replace(",", "."))
#             nota2 = float(n2.replace(",", "."))
#             nota3 = float(n3.replace(",", "."))
            
#             resultado = (nota1 + nota2 + nota3) / 3
            
#             messagebox.showinfo("Média Aritmética", f"A média aritmética é {resultado:.2f}.")
#         except ValueError:
#             messagebox.showerror("Erro", "Por favor, digite apenas números válidos nas notas!")

# app = tk.Tk()
# app.title("Questão 04 - Média de Qualidade ")
# app.geometry("500x350")       
# app.configure(bg="#fdd5f1")   

# lbl_nota1 = tk.Label(app, text="Digite a nota n°1:", bg="#ee35c0", fg="white", font=("Arial", 11))
# lbl_nota1.pack(pady=(15, 2)) 
# campo_nota1 = tk.Entry(app, font=("Arial", 12), justify="center") 
# campo_nota1.pack(pady=5)

# lbl_nota2 = tk.Label(app, text="Digite a nota n°2:", bg="#ee35c0", fg="white", font=("Arial", 11))
# lbl_nota2.pack(pady=(10, 2)) 
# campo_nota2 = tk.Entry(app, font=("Arial", 12), justify="center") 
# campo_nota2.pack(pady=5)

# lbl_nota3 = tk.Label(app, text="Digite a nota n°3:", bg="#ee35c0", fg="white", font=("Arial", 11))
# lbl_nota3.pack(pady=(10, 2)) 
# campo_nota3 = tk.Entry(app, font=("Arial", 12), justify="center") 
# campo_nota3.pack(pady=5)

# btn_enviar = tk.Button(app, text="Enviar", command=campo_media, bg="#ee35c0", fg="white", font=("Arial", 11), width=10)
# btn_enviar.pack(pady=(20, 5))

# btn_fechar = tk.Button(app, text="Fechar", command=app.destroy, bg="#ee35c0", fg="white", font=("Arial", 11), width=10)
# btn_fechar.pack(pady=5)

# app.mainloop()

# --------------------------------------------------------------------------------------------------------------------------

# QUESTÃO 05
# Termostato Inteligente: Peça a temperatura de um motor.
# ● Abaixo de 40°C: "Baixa carga".
# ● Entre 40°C e 70°C: "Normal".
# ● Acima de 70°C: "ALERTA: Resfriamento Ativado!".

import tkinter as tk
from tkinter import messagebox

# def verificar_temperatura():
#     texto_temp = campo_temp.get().strip()

#     if texto_temp == "":
#         messagebox.showwarning("Aviso", "Por favor, digite a temperatura do motor!")
#     else:
#         try:
#             temp = float(texto_temp.replace(",", "."))
            
#             if temp < 40:
#                 status = "Baixa carga"
#                 messagebox.showinfo("Status do Motor", f"Temperatura: {temp}°C\nClassificação: {status}")
            
#             elif 40 <= temp <= 70:
#                 status = "Normal"
#                 messagebox.showinfo("Status do Motor", f"Temperatura: {temp}°C\nClassificação: {status}")
            
#             else:
#                 status = "ALERTA: Resfriamento Ativado!"
#                 messagebox.showwarning("PERIGO", f"Temperatura: {temp}°C\n{status}")
                
#         except ValueError:
#             messagebox.showerror("Erro", "Por favor, insira um número válido para a temperatura.")


# app = tk.Tk()
# app.title("Questão 05 - Termostato Inteligente ")
# app.geometry("500x350")       
# app.configure(bg="#fdd5f1")   

# lbl_instrucao = tk.Label(app, text="Digite a temperatura do motor (°C):", bg="#ee35c0", fg="white", font=("Arial", 11))
# lbl_instrucao.pack(pady=(30, 10)) 

# campo_temp = tk.Entry(app, font=("Arial", 12), justify="center") 
# campo_temp.pack(pady=5)

# btn_enviar = tk.Button(app, text="Verificar", command=verificar_temperatura, bg="#ee35c0", fg="white", font=("Arial", 11), width=12)
# btn_enviar.pack(pady=(20, 5))

# btn_fechar = tk.Button(app, text="Fechar", command=app.destroy, bg="#ee35c0", fg="white", font=("Arial", 11), width=12)
# btn_fechar.pack(pady=5)

# app.mainloop()

# --------------------------------------------------------------------------------------------------------------------------

# QUESTÃO 06
# Classificador de Lotes: O usuário insere o código do produto. 
# Se começar com "A", exiba "Alimentos". Se "E", "Eletrônicos". Para qualquer outro, "Desconhecido".

# import tkinter as tk
# from tkinter import messagebox

# def classificar_produto():
#     codigo = campo_codigo.get().strip()

#     if codigo == "":
#         messagebox.showwarning("Aviso", "Digite o código do produto!")
#     else:
#         if codigo.upper().startswith("A"):
#             categoria = "Alimentos"
#         elif codigo.upper().startswith("E"):
#             categoria = "Eletrônicos"
#         else:
#             categoria = "Desconhecido"
            
#         messagebox.showinfo("Classificador de Lotes", f"A categoria do produto é: {categoria}")

# app = tk.Tk()
# app.title("Questão 06 - Classificador de Lotes ")
# app.geometry("500x350")       
# app.configure(bg="#fdd5f1")   

# lbl_codigo = tk.Label(app, text="Digite o código do produto:", bg="#ee35c0", fg="white", font=("Arial", 11))
# lbl_codigo.pack(pady=(35, 10)) 

# campo_codigo = tk.Entry(app, font=("Arial", 12), justify="center") 
# campo_codigo.pack(pady=5)

# btn_enviar = tk.Button(app, text="Enviar", command=classificar_produto, bg="#ee35c0", fg="white", font=("Arial", 11), width=10)
# btn_enviar.pack(pady=(25, 5))

# btn_fechar = tk.Button(app, text="Fechar", command=app.destroy, bg="#ee35c0", fg="white", font=("Arial", 11), width=10)
# btn_fechar.pack(pady=5)

# app.mainloop()

# --------------------------------------------------------------------------------------------------------------------------

# QUESTÃO 07
# Segurança de Operação: A máquina só liga se o sensor_porta == "fechada" E o botao_emergencia == "desligado". 
# Peça esses dois inputs e diga se a máquina pode iniciar.

# import tkinter as tk
# from tkinter import messagebox

# def verificar_seguranca():
#     porta = campo_porta.get().lower().strip()
#     emergencia = campo_emergencia.get().lower().strip()

#     if porta == "" or emergencia == "":
#         messagebox.showwarning("Aviso", "Por favor, preencha ambos os campos!")
#     else:
#         if porta == "fechada" and emergencia == "desligado":
#             messagebox.showinfo("Status de Operação", "A máquina pode iniciar com segurança.")
#         else:
#             messagebox.showerror("Bloqueio de Segurança", "A máquina não pode iniciar!\nVerifique as condições de segurança.")

# app = tk.Tk()
# app.title("Questão 07 - Segurança de Operação ")
# app.geometry("500x350")       
# app.configure(bg="#fdd5f1")   

# lbl_porta = tk.Label(app, text="Status do sensor da porta (aberta/fechada):", bg="#ee35c0", fg="white", font=("Arial", 11))
# lbl_porta.pack(pady=(20, 5)) 

# campo_porta = tk.Entry(app, font=("Arial", 12), justify="center") 
# campo_porta.pack(pady=5)

# lbl_emergencia = tk.Label(app, text="Status do botão de emergência (ligado/desligado):", bg="#ee35c0", fg="white", font=("Arial", 11))
# lbl_emergencia.pack(pady=(15, 5)) 

# campo_emergencia = tk.Entry(app, font=("Arial", 12), justify="center") 
# campo_emergencia.pack(pady=5)

# btn_enviar = tk.Button(app, text="Enviar", command=verificar_seguranca, bg="#ee35c0", fg="white", font=("Arial", 11), width=10)
# btn_enviar.pack(pady=(25, 5))

# btn_fechar = tk.Button(app, text="Fechar", command=app.destroy, bg="#ee35c0", fg="white", font=("Arial", 11), width=10)
# btn_fechar.pack(pady=5)

# app.mainloop()

# --------------------------------------------------------------------------------------------------------------------------

# QUESTÃO 08
# Cálculo de Descarte: Peça o total de peças produzidas e o total de defeituosas. 
# Se o descarte for maior que 5% do total, exiba "Revisar Processo", caso contrário "Processo Otimizado".

# import tkinter as tk
# from tkinter import messagebox

# def verificar_descarte():
#     txt_prod = campo_produzidas.get().strip()
#     txt_def = campo_defeituosas.get().strip()

#     if txt_prod == "" or txt_def == "":
#         messagebox.showwarning("Aviso", "Por favor, digite ambos os valores solicitados!")
#     else:
#         try:
#             total_produzidas = int(txt_prod)
#             total_defeituosas = int(txt_def)
            
#             if total_produzidas <= 0:
#                 messagebox.showerror("Erro", "O total de peças produzidas deve ser maior que zero!")
#                 return

#             percentual_descarte = (total_defeituosas / total_produzidas) * 100
            
#             if percentual_descarte > 5:
#                 mensagem = "Revisar processo... "
#             else:
#                 mensagem = "Processo otimizado! "
            
#             messagebox.showinfo("Resultado da Análise", f"Status: {mensagem}\nPercentual de descarte: {percentual_descarte:.2f}%")
            
#         except ValueError:
#             messagebox.showerror("Erro", "Por favor, digite apenas números inteiros válidos!")

# app = tk.Tk()
# app.title("Questão 08 - Cálculo de Descarte ")
# app.geometry("500x350")       
# app.configure(bg="#fdd5f1")   

# lbl_produzidas = tk.Label(app, text="Total de peças produzidas:", bg="#ee35c0", fg="white", font=("Arial", 11))
# lbl_produzidas.pack(pady=(20, 5)) 

# campo_produzidas = tk.Entry(app, font=("Arial", 12), justify="center") 
# campo_produzidas.pack(pady=5)

# lbl_defeituosas = tk.Label(app, text="Total de peças defeituosas:", bg="#ee35c0", fg="white", font=("Arial", 11))
# lbl_defeituosas.pack(pady=(15, 5)) 

# campo_defeituosas = tk.Entry(app, font=("Arial", 12), justify="center") 
# campo_defeituosas.pack(pady=5)

# btn_enviar = tk.Button(app, text="Enviar", command=verificar_descarte, bg="#ee35c0", fg="white", font=("Arial", 11), width=10)
# btn_enviar.pack(pady=(25, 5))

# btn_fechar = tk.Button(app, text="Fechar", command=app.destroy, bg="#ee35c0", fg="white", font=("Arial", 11), width=10)
# btn_fechar.pack(pady=5)

# app.mainloop()

# --------------------------------------------------------------------------------------------------------------------------

# QUESTÃO 09
# Validação de Medida: Uma peça deve ter entre 9.8mm e 10.2mm. 
# Peça a medida e diga se está dentro da tolerância, acima ou abaixo.

# import tkinter as tk
# from tkinter import messagebox

# def validando_pecas():
#     texto_medida = campo_medida.get().strip()

#     if texto_medida == "":
#         messagebox.showwarning("Aviso", "Por favor, digite a medida da peça!")
#     else:
#         try:
#             medida = float(texto_medida.replace(",", "."))
            
#             if medida < 9.8:
#                 status = "Abaixo da tolerância"
#                 messagebox.showwarning("Resultado", f"Medida: {medida}mm\nClassificação: {status}")
            
#             elif 9.8 <= medida <= 10.2:
#                 status = "Dentro da tolerância (Normal)"
#                 messagebox.showinfo("Resultado", f"Medida: {medida}mm\nClassificação: {status}")
            
#             else:
#                 status = "Acima da tolerância"
#                 messagebox.showwarning("Resultado", f"Medida: {medida}mm\nClassificação: {status}")
                
#         except ValueError:
#             messagebox.showerror("Erro", "Por favor, insira um número válido para a medida.")

# app = tk.Tk()
# app.title("Questão 09 - Validação de Medida ")
# app.geometry("500x350")       
# app.configure(bg="#fdd5f1")   

# lbl_instrucao = tk.Label(app, text="Digite a medida da peça (mm):", bg="#ee35c0", fg="white", font=("Arial", 11))
# lbl_instrucao.pack(pady=(35, 10)) 

# campo_medida = tk.Entry(app, font=("Arial", 12), justify="center") 
# campo_medida.pack(pady=5)

# btn_enviar = tk.Button(app, text="Verificar", command=validando_pecas, bg="#ee35c0", fg="white", font=("Arial", 11), width=12)
# btn_enviar.pack(pady=(25, 5))

# btn_fechar = tk.Button(app, text="Fechar", command=app.destroy, bg="#ee35c0", fg="white", font=("Arial", 11), width=12)
# btn_fechar.pack(pady=5)

# app.mainloop()

#  --------------------------------------------------------------------------------------------------------------------------

# QUESTÃO 10
# 10.Contagem Regressiva de Setup: Faça uma contagem regressiva de 10 até 1 
# para o início de uma prensa diretamente na tela (GUI), e finalize com "Prensa Ativada!".

# import tkinter as tk
# from tkinter import messagebox

# def iniciar_contagem():
#     btn_enviar.config(state="disabled")
#     contar(10)

# def contar(i):
#     if i > 0:
#         lbl_contagem.config(text=str(i))
#         app.after(1000, contar, i - 1)
#     else:
#         lbl_contagem.config(text="0")
#         status = "Prensa Ativada!"
#         messagebox.showinfo("Status da Prensa", f"{status}")
        
#         btn_enviar.config(state="normal")
#         lbl_contagem.config(text="--")

# app = tk.Tk()
# app.title("Questão 10 - Contagem Regressiva de Setup ")
# app.geometry("500x380")       
# app.configure(bg="#fdd5f1")   

# lbl_instrucao = tk.Label(app, text="Clique no botão para iniciar a prensa:", bg="#ee35c0", fg="white", font=("Arial", 11))
# lbl_instrucao.pack(pady=(30, 10)) 

# lbl_contagem = tk.Label(app, text="--", bg="#fdd5f1", fg="#ee35c0", font=("Arial", 48, "bold"))
# lbl_contagem.pack(pady=10)

# btn_enviar = tk.Button(app, text="Iniciar", command=iniciar_contagem, bg="#ee35c0", fg="white", font=("Arial", 11), width=12)
# btn_enviar.pack(pady=(15, 5))

# btn_fechar = tk.Button(app, text="Fechar", command=app.destroy, bg="#ee35c0", fg="white", font=("Arial", 11), width=12)
# btn_fechar.pack(pady=5)

# app.mainloop()

#  --------------------------------------------------------------------------------------------------------------------------