import tkinter as tk
from tkinter import messagebox

def solicitar_informacoes():
    #.get() Serve para buscar o texto que foi digitado
    nome_usuario =campo_nome.get()
    idade_usuario =campo_idade.get()

    if nome_usuario and idade_usuario=="":
        messagebox.showwarning("Aviso","Por favor, Digite o seu nome e sua idade")
    else:
        messagebox.showinfo("Saudações querido aluno",f"Olá {nome_usuario} seja bem vindo ao mundo das interfaces gráficas, Você possui {idade_usuario} anos.")

app =tk.Tk()
app.title("Tela de usuário")
app.geometry("300x300")

lbl_nome_usuario =tk.Label(app, text="Digite o seu nome").grid(row=0, column=0, padx=10,pady=10)
# lbl_nome_usuario.pack(pady=15)


campo_nome =tk.Entry(app,font=("Arial",12))
campo_nome.grid(row=1,column=0,padx=10,pady=5)
# campo_nome.pack(pady=3)
lbl_idade_usuario = tk.Label(app,text="Digite sua idade")
lbl_idade_usuario.grid(row=2,column=0,pady=15)
# lbl_idade_usuario.pack(pady=10)
campo_idade =tk.Entry(app,font=("Arial",12))
campo_idade.grid(row=3,column=0,padx=10,pady=5)
# campo_idade.pack(pady=5)
btn_cadastrar =tk.Button(app,text="Cadastrar", command=solicitar_informacoes)
btn_cadastrar.grid(row=4,column=0,pady= 15)
# btn_cadastrar.pack(pady=3)


btn_fechar =tk.Button(app, text="Fechar",command=app.destroy)
btn_fechar.grid(row=5,column=0,pady=5)
#  btn_fechar.pack(pady=30)












app.mainloop()