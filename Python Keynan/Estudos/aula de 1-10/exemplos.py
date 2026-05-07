# O laço for (repetições )
# Use o for quando vocÊ sane extamente qyantas vezes algo deve acontecer 
# Exenplo : relatorio de peças 
# Imagine que você tenha uma meta de produzir 5 e lote e quer numerar cada um :
# exemplo1 :
# for lote in range(1, 6):
#     print(f"processabdo lote número {lote}...")
#     print("Qualidade verificada . [OK]")
#     print("Produção do dia finalizada")
# for carro in range(1,6):
#     print(f"processando carro {carro}...")

# for i in range(5):
#   print(i)
# pecas = [" Engrenagem"," Eixo"," Rolamento"," Parafuso"," Martelo"]
# tipospecas =[ " Barra Dentada"," Porca do Eixo", "Rolamento anel estranho"," Parafuso phillips"," Martelo cabeça chata"]
# for item in pecas:
#     print(f"Item em estoque:{item} ")
#     for tipos in tipospecas:
#         print(f"Meus tipos de peças {tipospecas}")


# Exemplo 04
# Imagine a seguine situação gostaria de ter um menu onde pudesse perguntar qual opção você deseha e a partir da seleção
# ele listar os produtos

# pecas = [" Engrenagem"," Eixo"," Rolamento"," Parafuso"," Martelo"]
# tipospecas =[ " Barra Dentada"," Porca do Eixo", "Rolamento anel estranho"," Parafuso phillips"," Martelo cabeça chata"]
# print("Bem vindo a loja de peças sem peças")
# print(" Bem - Vindo ao nosso Sistemas")
# print("Escolha duas opção")
# print("1 - peças")
# print("2 - tipos de peças")
# opçao = int(input("qual opção você deseja"))
# if opçao == (1):
#  for item in pecas:
#   print(f"Item em estoque:{item} ")
# elif opçao == (2):
#   for tipos in tipospecas:
#        print(f"Meus tipos de peças {tipospecas}")
#   else : print(" Encerrando programa")


# Exercicio 1

# for pecas in range (1, 11):
#     print (f"peça N°{pecas} processado com sucesso ") 
    
# print ("Ciclo de produção produzido ")


# Exercicio 2"Frutas = ["banana  manga , melancia , abacaxi"]

# for frt1 in range (1, 11) :
#     print(f"Frutas no estoque: {frt1} bananas")
# for frt2 in range (1, 6) :
#     print(f"Frutas no estoque: {frt2} manga")
# for frt3 in range (1, 11):
#     print (f"Frutas no estoque: {frt3} melancia")
# for frt4 in range (1, 14):
#     print(f"Frutas no estoque: {frt4} abacaxi")


# exercicio 04

# tabuada = int(input("Qual tabuada você quer\n"))
# for i in range (1,11):
#     resultado = tabuada * i
    
#     print(f"{tabuada} x { i} = {resultado}")


# o Laço while (repetições indeterminadas)
#     Use o while quando você não sabe quando vai parar. Ele depende de uma condição (como sensor de segurança ou um botão de emergencia )
# ex : Monitor de temperatura (loop infinito controlado )
# Repete enquanto a temperatura estiver segura

# import time
# temperatura = 25
# while temperatura <= 40 :
#     print(f"Temperatura atual: {temperatura}°C.Sitema operando...")
#     time.sleep (2)
#     temperatura += 3 #Simulando o aquecimento da máquina
    
# print("ALERTA! Temperatura atingio o limite . Desligando o monitor")

# Menu de interação 


# opção =" "


# while opção != "sair" and "SAIR":
#     opção = input("Digite a Leitura do sensor ou sair para fechar: ").upper().lower()
    
#     if opção != "sair" and "SAIR": 
#         print(f"Dado '{opção}'registrado no banco de dados.")
#         print("sistema encerrado ")




#and e or
# and comparações verdadeiras e iguais
# or comparações verdadeiras mas não iguais
    

# pressao = int(input("Qual é a pressão? \n"))
# while pressao <= 100 :
    
#     pressao = int(input("Qual é a pressão? \n"))
#     print(f"A pressão {pressao} é normal")
    

# print("ALERTA : Pressão crítica atingida! \n Desligando sistema")



# import time
# pressao = int(input("Qual é a pressão? \n"))
# while pressao <= 100 :
#     print(f"Pressão atual: {pressao} é normal...")
#     time.sleep (2)

    
# print("ALERTA! Temperatura atingio o limite . Desligando o monitor")


# print("Vote na melhor serie do ano\n 1 - Outer Banks, \n 2-Stranger things, \n 3-Riverdale, \n 4-Elite")
# escolha = int(input("Escolha de 1 a 4"))
# while escolha 








































































 
 






































































