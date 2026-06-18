import tkinter as tk
from tkinter import messagebox,ttk





# def dividir (a,b):
#     try:
#         resultado = a/b
#         print(F"O resultado da sua divisão é : {resultado}")
#     except ZeroDivisionError:
#         print(f"Erro, Não é possivel fazer divisão por 0")
#     except TypeError:
#         print("Por favor digite somente números")
#     except Exception as e:
#         print(f"Ocorreu um erro inesperado {e}")

# dividir(10,"a")

# janela =tk.Tk()

# def divisao():
#     num1 =  int(ent_num1.get())
#     num2 = int(ent_num2.get())
#     try:
#        resultado = num1/num2
#        if num1 =="" and num2=="":
#            messagebox.showerror("Erro","Insira todos os campos")
#        else:
#            messagebox.showinfo("sucesso",f"O seu resultado é {resultado}") 
       
       
#     except ZeroDivisionError:
#         messagebox.showerror("Error","Não é possivel fazer a divisão por 0")
#     except TypeError:
#         messagebox.showerror("Error","Digite somente números")

#     except Exception as e:
#         messagebox.showerror(f"Error",f"Erro inesperado {e}")
#     except ValueError:
#         messagebox.showerror("Erro", "Inserir numeros válidos")




# janela.title("Tratamento de erros")
# janela.geometry("720x600")


# lbl_num1 =tk.Label(janela,text="Insira o primeiro valor")
# lbl_num1.grid(row=0,column=0,padx=10,pady=10)

# ent_num1 =tk.Entry(janela)
# ent_num1.grid(row=0,column=1,padx=10,pady=10)


# lbl_num2 = tk.Label(janela,text="Insira o segundo valor")
# lbl_num2.grid(row=1,column=0,padx=10,pady=10)

# ent_num2 =tk.Entry(janela)
# ent_num2.grid(row=1,column=1,padx=10,pady=10)

# btn_calculo =tk.Button(janela,text="CALCULE",bg="Red",fg="white",command=divisao)
# btn_calculo.grid(row=2,column=0,padx=10,pady=10)

janela= tk.Tk()
janela.title("Teste")
janela.geometry("720x600")


def buscar():
    codigo = ent_code.get()
    if codigo.startswith ("E"):
        resultado.config(text="Eletronicos")

    elif codigo.startswith("A"):
        resultado.config(text="Alimentos")

    else:
        resultado.config(text="Desconhecido")




lbl_code =tk.Label(janela,text="Digite o codigo do produto")
lbl_code.grid(row=0,column=0,padx=10,pady=10)

ent_code =tk.Entry(janela)
ent_code.grid(row=0,column=1,padx=10,pady=10)

btn_buscar =tk.Button(janela,text="Buscar",bg="Cyan",command=buscar)
btn_buscar.grid(row=1,column=0,padx=10,pady=10)

resultado =tk.Label(janela,text="")
resultado.grid(row=2,column=0,padx=10,pady=10)

















































janela.mainloop()