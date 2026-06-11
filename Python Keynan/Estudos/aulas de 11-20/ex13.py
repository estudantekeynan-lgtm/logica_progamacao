# Exercício
# Crie uma aplicação que pergunte o nome e o ano de nascimento do usuário
# Calcule a idade
import tkinter as tk
from tkinter import messagebox, ttk

def cadastro():
    ent_idade.get()
    ent_nome.get()
    if ent_idade and ent_nome =="":
        messagebox.showwarning("Tela de erro","Insira todos os dados")
    else: messagebox.showinfo(f"Olá {ent_nome} você tem {2026-ent_idade} anos de idade")

janela=tk.Tk()
janela.title("EX 1")
janela.geometry("1920x1080")
janela.configure(bg="Grey")


lbl_nome =tk.Label(janela,text="Digite seu nome",font=("Arial",14))
lbl_nome.grid(row=0,column=0,padx=10,pady=10)

ent_nome =tk.Entry(janela,font=("Arial",12))
ent_nome.grid(row=0,column=1,padx=10,pady=10)

lbl_idade =tk.Label(janela,text="Digite o ano que vocÊ nasceu",font=("Arial",12))
lbl_idade.grid(row=2,column=0,padx=10,pady=10)

ent_idade =tk.Entry(janela,font=("Arial",12))
ent_idade.grid(row=2,column=1,padx=10,pady=10)

btn_cadastro =tk.Button(janela,text="Cadastrar",font= ("Arial",12),bg="Light Blue",command=cadastro)
btn_cadastro.grid(row=3,column=0,padx=10,pady=10)






janela.mainloop()