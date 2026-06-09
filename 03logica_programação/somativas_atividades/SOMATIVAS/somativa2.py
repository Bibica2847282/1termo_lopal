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

import tkinter as tk
from tkinter import messagebox

def campo_media():
    nota1 = campo_nota1.get()
    nota2 = campo_nota2.get()
    nota3 = campo_nota3.get()


    if nota_media.get() == "":
        messagebox.showwarning("Aviso", "Digite as três notas!")
    else:
        total = (nota1 + nota2 + nota3) / 3
        messagebox.showinfo("média aritmética", f"Convertendo de Bar para PSI a pressão será de {total}.")

app = tk.Tk()
app.title("QUESTÃO 04")
app.geometry("400x250")       
app.configure(bg="#fdd5f1")   

lbl_nota1 = tk.Label(app, text="Digite a nota n°1 :", bg="#ee35c0", font=("Arial", 11))
lbl_media.pack(pady=20) 

campo_nota1 = tk.Entry(app, font=("Arial", 12), justify="center") 
campo_nota1.pack(pady=5)



btn_enviar = tk.Button(app, text="Enviar", command=campo_media, bg="#ee35c0", fg="white", font=("Arial", 11), width=10)
btn_enviar.pack(pady=20)

app.mainloop()

