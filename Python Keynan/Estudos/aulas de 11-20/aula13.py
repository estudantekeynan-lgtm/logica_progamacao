# import tkinter as tk
# from tkinter import messagebox,ttk

# #Defs linha de blocos de função
# #.get em todos os componentes que irão receber informação
# def cadastrar_usuario():
#     nome_usuario = ent_nome.get()
#     nome_escola = cmb_nome_escola.get()

#     if nome_usuario and nome_escola =="":
#         messagebox.showwarning("Verifique seus dados","Verifique os Campos")
#     else:
#         messagebox.showinfo("Bem vindo",f"Olá usuario {nome_usuario} sua escola é {cmb_nome_escola}")



# #Etapa 0 gerar janela
# janela = tk.Tk()
# janela.title("Revisão")
# janela.geometry("500x500")
# janela.configure(bg="light green")

# #1 etapa componentes
# lbl_title =tk.Label(janela,text="Revisão TKinter",font=("Arial",14), fg="black",bg="White")
# lbl_title.grid(row=3,column=2,pady=20,padx=20)

# lbl_nome =tk.Label(janela,text="Digite o seu nome:",font=("Arial",14))
# lbl_nome.grid(row=0,column=0,padx=20,pady=20)

# ent_nome = tk.Entry(janela,font=("Arial",12))
# ent_nome.grid(row=0,column=1,padx=10,pady=20)

# #2 Caixa de seleção ou combobox
# lbl_escola =tk.Label(janela,text="Escolha sua escola:",font=("Arial",14))
# lbl_escola.grid(row=2,column=0,padx=10,pady=10)

# cmb_nome_escola =ttk.Combobox(janela, values=["SESI 5","SESI 408"],state="readonly", width=40,height=40)
# cmb_nome_escola.grid(row=2,column=1,padx=10,pady=10)

# btn_dados =tk.Button(janela,text="Cadastrar usuario",font=("Arial",14),width=15,height=5,bg="blue", command=cadastrar_usuario)
# btn_dados.grid (row=2,column=4,padx=20,pady=20)
 
# btn_fechar =tk.Button(janela,text=" Fechar Janela",font=("Arial",14),width=15,height=5,bg="Red",command=janela.destroy)
# btn_fechar.grid (row=2,column=5,padx=20,pady=20)

# #4 etapa

# janela.mainloop()

