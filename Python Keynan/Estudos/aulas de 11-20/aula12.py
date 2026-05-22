#tkinter
# componentes principais
#TK = janela
#label =  texto em rótulo
#button = botão
#entry = campo de entrada

#Biblioteca
import tkinter as tk
from tkinter import messagebox  

# 1 Criar a janela principal
janela = tk.Tk()
janela.title("Minha primeira janela em GUI")
janela.geometry("400x200") #Largura x Altura
janela.configure (bg="lightgreen")

#2. Criar a função que será chamada quando o botão for clicado
def mostrar_mensagem():
    messagebox.showinfo("Sucesso", "Você clicou no botão!")
#3 Criar componentes (Widgets))
lbl_titulo =tk.Label(janela, text = "Bem vindo a aula de GUI com Tkinter", font=("times new roman", 14, "italic"),fg="purple", bg= "Grey")
btn_click = tk.Button(janela, text="Clique aqui", font=("arial",12,"bold"),bg="darkblue",fg="White",command=mostrar_mensagem)


#4. Posicionar os componentes da janela
lbl_titulo.pack(pady=20) #Adiciona um espaço vertical de 20 pixels
btn_click.pack(pady=10)
lbl_titulo.pack(padx=10)
btn_click.pack(padx=20)

#5. Rodar o loop da janela
janela.mainloop()