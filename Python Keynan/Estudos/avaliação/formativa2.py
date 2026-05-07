#1. O Problema da Idade
#  idade =input("Digite sua idade:")
# if idade >= 18:     
#     print("Você é maior de idade")  #Errado






# idade =int(input("Digite sua idade:"))
# if idade >= "18":     
#     print("Você é maior de idade")  #Certo

# idade =int(input("Digite sua idade:"))
# if idade >= 18:     
#     print("Você é maior de idade")
# else: print("Você é menor de idade")  #Mais eficiente
 

#2. A Escrita Fiel
# nome ="Mariana"
# print("Seja bem vinda,nome!") #Errado


# nome ="Mariana"
# print("Seja bem vinda,",nome,"!") #Certo


# nome ="Mariana"
# print(f"Seja bem-vinda,{nome}!") #Mais eficiente

#3. Falta de Espaço
# numero=10
# if numero>5:
# print("O numero é maior que cinco")
# else:
# print("O Numero é menor ou igual a cinco") #Errado

# numero = float(input("Qual é o Número\n"))
# if numero >5:
#     print("Número maior que cinco")
# else: 
#     print("Número menor ou igual a cinco") #Certo


# numero = float(input("Qual é o Número\n"))
# if numero >5:
#     print("Número maior que cinco")
# elif numero <5:
#     print("Número menor que 5")
# else:
#     print("Seu número é igual a 5") #Mai eficiente


#4. Esquecimento Fatal
# usuario = "aluno123"
# if usuario == "aluno123"
#   print("Login realizado com sucesso") #Errado


# usuario = "aluno123"
# if usuario == "aluno123":
#   print("Login realizado com sucesso")#Certo

# usuario = input("Qual é o seu usuario? ")
# if usuario == "aluno123":
#   print("Login realizado com sucesso")
# else: print("Usuario incorreto") #Eficiente



#5 Atribuição vs. Comparação
# clima ="ensolarado"
# if clima = "chuvoso":
# print("Leve um guarda-Chuva!") #Errado

# clima ="ensolarado"
# if clima == "chuvoso":
#     print("Leve um guarda-Chuva!") #Correto

# clima =input("Como está o clima de hoje?")
# if clima == "chuvoso":
#     print("Leve um guarda-chuva!")
# else: 
#     print("Aproveite o dia") #Eficiente

#6 Misturando Alhos com Bugalhos
# pontos = 50
# print("Parabéns!Você fez"+pontos+"pontos.") #Errado


# pontos = int (50)
# print("Parabéns!Você fez", pontos +pontos,"Pontos") #Correto



# pontos = float(input("Quantos pontos você fez "))
# print(f"Parabens você fez {pontos*2} pontos") #Eficiente



#7 A Ordem dos Fatores
#O sistema deve dar "Excelente" para notas 9 ou 10.

# nota = 9.5
# if nota >= 7:
#     print("Aprovado")
# elif nota >= 9:
#     print("Exelente!") #Errado



# nota = 9.5
# if nota >=9:
#     print("Exelente")
# elif nota >= 7:
#     print("Aprovado") #Correto



# nota = float(input("Qual foi a nota do aluno? "))
# if nota >=9:
#     print("Exelente")
# elif nota >= 7:
#     print("Aprovado")
# else: print("Reprovado") # Eficiente





#8 O Contador de 1 a 5
# for i in range(5):
#     print(i) #Errado


# for i in range(1,6):
#     print(i) #Correto




#9 O Loop Eterno
# tentativas = 1
# while tentativas <=3:
#     print("Tentando conectar...") # Errado



# tentativas = 1
# while tentativas <=3:
#     print("Tentando conectar")
#     tentativas = tentativas +1 #Correto




#10 A Senha Teimosa
# senha = ""
# while senha == "python123":
#     senha = input("Digite a senha secreta ")
#     print("Acesso concedido!") #Errado


# senha = ""
# while True:
#     senha = input("Qual é a senha secreta ")
#     if senha == "python123":
#         print("Acesso concedido!")
#         break
    
#      #Correto







    
    












