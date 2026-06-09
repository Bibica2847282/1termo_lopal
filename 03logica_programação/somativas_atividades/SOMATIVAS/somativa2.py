# QUESTÃO 01
# Registro de Operador: Peça o nome do operador e o turno (A, B ou C). Exiba:
# "Operador [Nome] registrado no Turno [Turno]. Boa jornada!"

# tk: Janela principal
# Label: Texto ou rotulo
# Button: Um botão clicável 
# Entry: Um campo de entrada de texto

# import tkinter as tk
# from tkinter import messagebox

# def operador_usario():
#     nome = campo_nome.get()
#     turno = campo_turno.get()

#     if nome == "":
#         messagebox.showwarning("Digite seu nome: ")
#     else:
#         messagebox.showinfo(f"Operador {nome} registrado no Turno {turno}. Boa jornada!")

#     if turno == "":
#         messagebox.showwarning("Digite o seu turno: ")
#     else:
#         messagebox.showinfo("Saudação", f"Operador {nome} registrado no Turno {turno}. Boa jornada! ")


# app = tk.Tk()
# app.title("QUESTÃO 01")
# app.geometry("500x400")

# lbl_instrucao = tk.Label(app, text="Digite seu nome abaixo:")
# lbl_instrucao.pack(pady=10)

# lbl_instrucao = tk.Label(app, text="E o seu turno:")
# lbl_instrucao.pack(pady=10)

# campo_nome = tk.Entry(app, font=("Arial", 12))
# campo_nome.pack(pady=5)

# campo_turno = tk.Entry(app, font=("Arial", 12))
# campo_turno.pack(pady=5)

# btn_enviar = tk.Button(app, text="Enviar", command=operador_usario)
# btn_enviar.pack(pady=15)
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
# app.title("QUESTÃO 02")
# app.geometry("400x250")       
# app.configure(bg="#fdd5f1")   

# lbl_pecas = tk.Label(app, text="Digite o número de peças produzidas em uma hora:", bg="#ee35c0", font=("Arial", 11))
# lbl_pecas.pack(pady=20)    

# campo_pecas = tk.Entry(app, font=("Arial", 12), justify="center")
# campo_pecas.pack(pady=5)

# btn_enviar = tk.Button(app, text="Enviar", command=produção_peças, bg="#ee35c0", fg="white", font=("Arial", 11), width=10)
# btn_enviar.pack(pady=20)

# app.mainloop()

# --------------------------------------------------------------------------------------------------------------------------

# QUESTÃO 03
# Conversor de Unidade: O sistema lê uma pressão em Bar. Converta para PSI (1 Bar ≈ 14.5 PSI) e exiba com duas casas decimais.

# import tkinter as tk
# from tkinter import messagebox

# def pressão_bar():
#     bar = campo_bar.get()

#     if campo_bar.get() == "":
#         messagebox.showwarning("Aviso", "Digite o número de Bar!")
#     else:
#         pecas = int(campo_bar.get())
#         total = pecas * 14.5
#         messagebox.showinfo("Inversor de Bar", f"Convertendo de Bar para PSI a pressão será de {total}.")

# app = tk.Tk()
# app.title("QUESTÃO 03")
# app.geometry("400x250")       
# app.configure(bg="#fdd5f1")   

# lbl_bar = tk.Label(app, text="Digite o número de Bar:", bg="#ee35c0", font=("Arial", 11))
# lbl_bar.pack(pady=20) 

# campo_bar = tk.Entry(app, font=("Arial", 12), justify="center") 
# campo_bar.pack(pady=5)

# btn_enviar = tk.Button(app, text="Enviar", command=pressão_bar, bg="#ee35c0", fg="white", font=("Arial", 11), width=10)
# btn_enviar.pack(pady=20)

# app.mainloop()

# --------------------------------------------------------------------------------------------------------------------------

# QUESTÃO 04
# Média de Qualidade: Peça 3 notas de inspeção de uma peça (0 a 10). Exiba a média aritmética simples delas.

# import tkinter as tk
# from tkinter import messagebox

# def campo_media():
#     nota1 = int(campo_nota1.get())
#     nota2 = int(campo_nota2.get())
#     nota3 = int(campo_nota3.get())
#     resultado = nota1 + nota2 + nota3

#     if nota1 == "" and nota2 == "" and nota3 == "" :
#         messagebox.showwarning("Aviso", "Digite as três notas!")
#     else:
#         messagebox.showinfo("média aritmética", f"A média arimética é {resultado / 3}.")

# app = tk.Tk()
# app.title("QUESTÃO 04")
# app.geometry("500x350")       
# app.configure(bg="#fdd5f1")   

# lbl_nota1 = tk.Label(app, text="Digite a nota n°1 :", bg="#ee35c0", font=("Arial", 11))
# lbl_nota1.pack(pady=20) 

# campo_nota1 = tk.Entry(app, font=("Arial", 12), justify="center") 
# campo_nota1.pack(pady=5)

# lbl_nota2 = tk.Label(app, text="Digite a nota n°2 :", bg="#ee35c0", font=("Arial", 11))
# lbl_nota2.pack(pady=20) 

# campo_nota2 = tk.Entry(app, font=("Arial", 12), justify="center") 
# campo_nota2.pack(pady=5)

# lbl_nota3 = tk.Label(app, text="Digite a nota n°3 :", bg="#ee35c0", font=("Arial", 11))
# lbl_nota3.pack(pady=20) 

# campo_nota3 = tk.Entry(app, font=("Arial", 12), justify="center") 
# campo_nota3.pack(pady=5)


# btn_enviar = tk.Button(app, text="Enviar", command=campo_media, bg="#ee35c0", fg="white", font=("Arial", 11), width=10)
# btn_enviar.pack(pady=20)

# app.mainloop()

# --------------------------------------------------------------------------------------------------------------------------

# QUESTÃO 09
# Validação de Medida: Uma peça deve ter entre 9.8mm e 10.2mm. Peça a medida e diga se está dentro da tolerância, acima ou abaixo.


# QUESTÃO 05
# Termostato Inteligente: Peça a temperatura de um motor.
# ● Abaixo de 40°C: "Baixa carga".
# ● Entre 40°C e 70°C: "Normal".
# ● Acima de 70°C: "ALERTA: Resfriamento Ativado!".

# import tkinter as tk
# from tkinter import messagebox

# def verificar_temperatura():
#     texto_temp = campo_temp.get()

#     # Validação: verifica se o campo está vazio
#     if texto_temp == "":
#         messagebox.showwarning("Aviso", "Por favor, digite a temperatura do motor!")
#     else:
#         try:
#             temp = float(texto_temp)
            
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
# app.title("QUESTÃO 05 - Termostato")
# app.geometry("500x350")       
# app.configure(bg="#fdd5f1")   

# lbl_instrucao = tk.Label(app, text="Digite a temperatura do motor (°C):", bg="#ee35c0", fg="white", font=("Arial", 11))
# lbl_instrucao.pack(pady=30) 

# campo_temp = tk.Entry(app, font=("Arial", 12), justify="center") 
# campo_temp.pack(pady=10)

# btn_enviar = tk.Button(app, text="Verificar", command=verificar_temperatura, bg="#ee35c0", fg="white", font=("Arial", 11), width=12)
# btn_enviar.pack(pady=30)

# app.mainloop()

# --------------------------------------------------------------------------------------------------------------------------

# QUESTÃO 06
# Classificador de Lotes: O usuário insere o código do produto. Se começar com "A",exiba "Alimentos". Se "E", "Eletrônicos". Para qualquer outro, "Desconhecido".

# QUESTÃO 06
# Classificador de Lotes: O usuário insere o código do produto. 
# Se começar com "A", exiba "Alimentos". Se "E", "Eletrônicos". Para qualquer outro, "Desconhecido".

# import tkinter as tk
# from tkinter import messagebox

# def classificar_produto():
#     codigo = campo_codigo.get()

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
# app.title("QUESTÃO 06")
# app.geometry("500x350")       
# app.configure(bg="#fdd5f1")   

# lbl_codigo = tk.Label(app, text="Digite o código do produto:", bg="#ee35c0", font=("Arial", 11))
# lbl_codigo.pack(pady=40) 

# campo_codigo = tk.Entry(app, font=("Arial", 12), justify="center") 
# campo_codigo.pack(pady=10)

# btn_enviar = tk.Button(app, text="Enviar", command=classificar_produto, bg="#ee35c0", fg="white", font=("Arial", 11), width=10)
# btn_enviar.pack(pady=40)

# app.mainloop()

# --------------------------------------------------------------------------------------------------------------------------

# QUESTÃO 07
# Segurança de Operação: A máquina só liga se o sensor_porta == "fechada" E o botao_emergencia == "desligado". Peça esses dois inputs e diga se a máquina pode iniciar.

# import tkinter as tk
# from tkinter import messagebox

# def verificar_seguranca():
#     porta = campo_porta.get()
#     emergencia = campo_emergencia.get()

#     if porta == "" or emergencia == "":
#         messagebox.showwarning("Aviso", "Por favor, preencha ambos os campos!")
#     else:
#         if porta == "fechada" and emergencia == "desligado":
#             messagebox.showinfo("Status de Operação", "A máquina pode iniciar com segurança.")
#         else:
#             messagebox.showerror("Bloqueio de Segurança", "A máquina não pode iniciar!\nVerifique as condições de segurança.")

# app = tk.Tk()
# app.title("QUESTÃO 07")
# app.geometry("500x350")       
# app.configure(bg="#fdd5f1")   

# lbl_porta = tk.Label(app, text="Status do sensor da porta (aberta/fechada):", bg="#ee35c0", font=("Arial", 11))
# lbl_porta.pack(pady=20) 

# campo_porta = tk.Entry(app, font=("Arial", 12), justify="center") 
# campo_porta.pack(pady=5)

# lbl_emergencia = tk.Label(app, text="Status do botão de emergência (ligado/desligado):", bg="#ee35c0", font=("Arial", 11))
# lbl_emergencia.pack(pady=20) 

# campo_emergencia = tk.Entry(app, font=("Arial", 12), justify="center") 
# campo_emergencia.pack(pady=5)

# btn_enviar = tk.Button(app, text="Enviar", command=verificar_seguranca, bg="#ee35c0", fg="white", font=("Arial", 11), width=10)
# btn_enviar.pack(pady=20)

# app.mainloop()

# --------------------------------------------------------------------------------------------------------------------------

# QUESTÃO 08
# Cálculo de Descarte: Peça o total de peças produzidas e o total de defeituosas. Se o descarte for maior que 5% do total, exiba "Revisar Processo", caso contrário "Processo Otimizado".

# import tkinter as tk
# from tkinter import messagebox

# def verificar_descarte():
#     total_produzidas = int(campo_produzidas.get())
#     total_defeituosas = int(campo_defeituosas.get())

#     if campo_produzidas.get() == "" and campo_defeituosas.get() == "":
#         messagebox.showwarning("Aviso", "Digite os valores solicitados! ")
#     else:
#         percentual_descarte = (total_defeituosas / total_produzidas) * 100
    
#     if percentual_descarte > 5:
#         mensagem = "Revisar processo... "
    
#     else:
#         mensagem = "Processo otimizado! "
    
#     messagebox.showinfo("Resultado da Análise", f"Status: {mensagem}\nPercentual de descarte: {percentual_descarte:.2f}%")

# app = tk.Tk()
# app.title("QUESTÃO 08")
# app.geometry("500x350")       
# app.configure(bg="#fdd5f1")   

# lbl_produzidas = tk.Label(app, text="Total de peças produzidas :", bg="#ee35c0", font=("Arial", 11))
# lbl_produzidas.pack(pady=20) 

# campo_produzidas = tk.Entry(app, font=("Arial", 12), justify="center") 
# campo_produzidas.pack(pady=5)

# lbl_defeituosas = tk.Label(app, text="Total de peças defeituosas :", bg="#ee35c0", font=("Arial", 11))
# lbl_defeituosas.pack(pady=20) 

# campo_defeituosas = tk.Entry(app, font=("Arial", 12), justify="center") 
# campo_defeituosas.pack(pady=5)

# btn_enviar = tk.Button(app, text="Enviar", command=verificar_descarte, bg="#ee35c0", fg="white", font=("Arial", 11), width=10)
# btn_enviar.pack(pady=20)

# app.mainloop()

# --------------------------------------------------------------------------------------------------------------------------

# QUESTÃO 09
# Validação de Medida: Uma peça deve ter entre 9.8mm e 10.2mm. Peça a medida e diga se está dentro da tolerância, acima ou abaixo.

import tkinter as tk
from tkinter import messagebox