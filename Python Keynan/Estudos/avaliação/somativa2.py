#HELLO WORLD




import tkinter as tk
from tkinter import messagebox,ttk

#1
# def cadastro_usuario():
#     nome_usuario = ent_nome.get()
#     turno_usuario = cmb_turno.get()
#     if nome_usuario =="" or turno_usuario =="":
#       messagebox.showwarning("Falha nas credencias","Por favor verifique suas informações")
#     else:
#        messagebox.showinfo("Seja bem vindo",f"Seja bem vindo {nome_usuario}, o seu turno é {turno_usuario}")  

janela =tk.Tk()
janela.title("Avaliação somativa")
janela.geometry("1920x1080")
janela.configure(bg="dark grey")


btn_fechar =tk.Button(janela,text="Fechar janela",bg="red",command=janela.destroy)
btn_fechar.grid(row=6,column=0,padx=10,pady=10)



# lbl_nome =tk.Label(janela,text="Digite o seu nome:",width=25,height=5)
# lbl_nome.grid(row=0,column=0,padx=10,pady=10)

# ent_nome =tk.Entry(janela)
# ent_nome.grid(row=0,column=1,padx=10,pady=10)


# lbl_turno =tk.Label(janela,text="Qual é o seu turno?",width=25,height=5)
# lbl_turno.grid(row=2,column=0,padx=10,pady=10)

# cmb_turno =ttk.Combobox(janela,values=["Noite","Manhã","Tarde"],state="readonly")
# cmb_turno.grid(row=2,column=1,padx=10,pady=10)

# btn_cadastro =tk.Button(janela,text="Cadastrar usuario", command=cadastro_usuario,bg="cyan")
# btn_cadastro.grid(row=3,column=0,padx=10,pady=10)

# btn_fechar =tk.Button(janela,text="Fechar aplicativo",command=janela.destroy,bg="red",fg="White")
# btn_fechar.grid(row=3,column=1,padx=10,pady=10)



#2
# def calculo():
#     pecas_produzidas = int (ent_pecas.get())
#     calculo_pecas = pecas_produzidas*8
#     messagebox.showinfo("Calculo de pecas",f"foram produzidas {pecas_produzidas} peças, e em 8 horas será produzidas {calculo_pecas} peças")



# lbl_pecas =tk.Label(janela,text="Quantas peças foram feitas em 1 hora?",)
# lbl_pecas.grid(row=0,column=0,padx=10,pady=10)

# ent_pecas =tk.Entry(janela)
# ent_pecas.grid(row=0,column=1,padx=10,pady=10)

# btn_calculo =tk.Button(janela,text="Calculo de peças",bg="Cyan",command=calculo)
# btn_calculo.grid(row=1,column=0,padx=10,pady=10)


#3

# def converter():
#     bar = int(ent_conversor.get())
#     PSI = bar *14.5
#     messagebox.showinfo("Sucesso",f"O valor convertido em PSI é : {PSI:.2f}")

# lbl_conversor =tk.Label(janela,text="Converta Bar para PSI:")
# lbl_conversor.grid(row=0,column=0,padx=10,pady=10)

# ent_conversor=tk.Entry(janela)
# ent_conversor.grid(row=0,column=1,padx=10,pady=10)

# btn_conversor =tk.Button(janela,text="Converter",bg="Cyan",command=converter)
# btn_conversor.grid(row=1,column=0,padx=10,pady=10)


#4
# def media():
#     nota1= int(ent_nota1.get())
#     nota2 =int(ent_nota2.get())
#     nota3=int(ent_nota3.get())
#     soma = nota1 + nota2 + nota3

#     divisao= soma/3
#     if nota1 >=10 or nota2 >=10 or nota3 >=10:
#         messagebox.showerror("erro","Porfavor digite números menores que 10")
#     else:
#         messagebox.showinfo("Media",f"A média do aluno foi {divisao:.2f}")
    



# lbl_nota1 =tk.Label(janela,text="Insira a primeira nota")
# lbl_nota1.grid(row=0,column=0,padx=10,pady=10)


# lbl_nota2 =tk.Label(janela,text="Insira a segunda nota")
# lbl_nota2.grid(row=1,column=0,padx=10,pady=10)


# lbl_nota3 =tk.Label(janela,text="Insira a terceira  nota")
# lbl_nota3.grid(row=2,column=0,padx=10,pady=10)

# ent_nota1 =tk.Entry(janela)
# ent_nota1.grid(row=0,column=1,padx=10,pady=10)

# ent_nota2 =tk.Entry(janela)
# ent_nota2.grid(row=1,column=1,padx=10,pady=10)

# ent_nota3 =tk.Entry(janela)
# ent_nota3.grid(row=2,column=1,padx=10,pady=10)

# btn_media=tk.Button(janela,text="Calcular media",bg="cyan",command=media)
# btn_media.grid(row=4,column=0,padx=10,pady=10)

#5
# def calculo_temp():
#     temperatura= int(ent_temp.get())
#     if temperatura <40:
#         messagebox.showinfo("Temperatura","Baixa Carga")
#     elif temperatura <70:
#         messagebox.showinfo("Temperatura","Normal")
#     else:
#         messagebox.showwarning("Temperatura","Alerta!!! Resfiamento ativado")


# lbl_temp=tk.Label(janela,text="Qual é a temperatura do motor?")
# lbl_temp.grid(row=0,column=0,padx=10,pady=10)

# ent_temp=tk.Entry(janela)
# ent_temp.grid(row=0,column=1,padx=10,pady=10)

# btn_calculo =tk.Button(janela,text="Calcule a Temperatura",bg="cyan",command=calculo_temp)
# btn_calculo.grid(row=1,column=0,padx=10,pady=10)



# 6

# def classificacao():
#     lote =cmb_lote.get()
#     if lote =="A":
#         messagebox.showinfo("Lote","Lote de alimentos")
#     elif lote =="E":
#         messagebox.showinfo("Lote","Lote de eletronicos")
#     else:
#         messagebox.showwarning("lote","Lote desconhecido")
    
    

# lbl_lotes =tk.Label(janela,text="Classifique os lotes")
# lbl_lotes.grid(row=0,column=0,padx=10,pady=10)

# cmb_lote =ttk.Combobox(janela,values=["A","E","Outro"],state="readonly")
# cmb_lote.grid(row=0,column=1,padx=10,pady=10)

# btn_lotes =tk.Button(janela,text="Buscar",bg="cyan",command=classificacao)
# btn_lotes.grid(row=1,column=0,padx=10,pady=10)


#7
# def verificar():
#     porta = cmb_porta.get()
#     verificar =cmb_emergencia.get()
#     if verificar =="Desligado" and porta =="Fechada":
#         messagebox.showinfo("Liberação","A máquina pode iniciar")
#     else:
#         messagebox.showwarning("Atenção","A máquina não pode iniciar")


# lbl_porta =tk.Label(janela,text="A porta esta aberta ou fechada?")
# lbl_porta.grid(row=0,column=0,padx=10,pady=10)


# cmb_porta =ttk.Combobox(janela,values=["Fechada","Aberta"],state="readonly")
# cmb_porta.grid(row=0,column=1,padx=10,pady=10)

# lbl_emergencia =tk.Label(janela,text="O botão está ligado ou desligado?")
# lbl_emergencia.grid(row=1,column=0,padx=10,pady=10)

# cmb_emergencia=ttk.Combobox(janela,values=["Ligado","Desligado"],state="readonly")
# cmb_emergencia.grid(row=1,column=1,padx=10,pady=10)


# btn_verificar =tk.Button(janela,text="Verificar requisitos",bg="cyan",command=verificar)
# btn_verificar.grid(row=3,column=0,padx=10,pady=10)


#8
# def calculo():
#     produzidas = int(ent_produzidos.get())
#     defeitos = int(ent_defeitos.get())
#     porcentagem = (defeitos*produzidas)/100
#     if porcentagem <=5:
#         messagebox.showinfo("Porcentagem","Processo otimizado")
#     else:
#         messagebox.showerror("Atenção","Revisar processo")

# lbl_produzidos = tk.Label(janela,text="Insira aqui o total de itens produzidos")
# lbl_produzidos.grid(row=0,column=0,padx=10,pady=10)


# ent_produzidos =tk.Entry(janela)
# ent_produzidos.grid(row=0,column=1,padx=10,pady=10)


# lbl_defeitos = tk.Label(janela,text="Quantos itens ficaram com defeito")
# lbl_defeitos.grid(row=1,column=0,padx=10,pady=10)

# ent_defeitos =tk.Entry(janela)
# ent_defeitos.grid(row=1,column=1,padx=10,pady=10)

# btn_calculo =tk.Button(janela,text="Calcule aqui",bg="cyan",command=calculo)
# btn_calculo.grid(row=2,column=0,padx=10,pady=10)


#9
# def verificacao():
#     peca = float(ent_pecas.get())
    
#     if peca <9.8:
#         messagebox.showwarning("Medida","Abaixo do ideal")
#     elif peca <10.2:
#         messagebox.showinfo("Medida","Tamanho ideal")
#     else:
#         messagebox.showwarning("Medida","Atenção peça muito grande")

# lbl_medida =tk.Label(janela,text="Quanto mm possui a peça")
# lbl_medida.grid(row=0,column=0,padx=10,pady=10)

# ent_pecas =tk.Entry(janela)
# ent_pecas.grid(row=0,column=1,padx=10,pady=10)

# btn_verificacao =tk.Button(janela,text="Verifique",bg="cyan",command=verificacao)
# btn_verificacao.grid(row=1,column=1,padx=10,pady=10)


#10
# def ativar():   
#     for i in range(1,11):
#         messagebox.showinfo("CONTAGEM REGRESSIVA",f"{i}")
#     messagebox.showinfo("COncluido","Prensa ativada")


# btn_ativar=tk.Button(janela,text="Ativar prensa",width=25,height=15,bg="red",command=ativar)
# btn_ativar.grid(row=6,column=6,padx=800,pady=400)











janela.mainloop()

