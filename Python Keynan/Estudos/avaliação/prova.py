# # print("Olá mundo")
# # 
# # ex:1
# # print("Olá sou o pedagio inteligenti da rodovia Tamoios")
# # mode =  str(input("Qual é o modelo do seu carro?"))
# # pla = input("Qual é a placa do seu veículo")

# # print(f"Seu carro é {mode} da placa {pla} boa Viagem!!!")


# # #EX: 2
# # print(" Olá sou o medidor de eficiencia de combustivel ")
# # com = float(input("Quantos litros tem o seu tanque de combústivel\n"))
# # km = float(input("Quantos quilometros ele faz por litro?\n"))
# # total = com / km
# # print(f"O seu veiculo pode correr {total} KM com o tanque cheio")


# # EX : 3

# # print("Conversão de Dolar para Real\n")
# # pedido = float(input("Quantos dolares você irá querer? "))
# # conver = print(f"Convertendo será {pedido * 5} reais")

# # EX :4
# # print("Seja bem vindo ao aplicativo De rotas 88")
# # rota1 = float(input("Qual é o tempo da 1° rota? : "))
# # rota2 = float(input("Qual é o tempo da 2° rota? "))
# # rota3 = float(input("Qual é o tempo da 3° rota? "))
# # total = (rota1 + rota2 + rota3) /3
# # print(f"Calculamos todas as possiveis rotas e elas deram a media de {total} horas ")


# EX: 5
# peso = float(input("Qual é o peso do seu caminhão em toneladas " ))
# if peso <= 10:
#     print("Caminhão Leve")
# elif peso <=25 :
#     print("Carga padrão")
# else: print("ALERTA: Excesso de Peso!")

# EX: 6

# print(" Bem vindo a Distribuidora Vant")
# cod = input("Qual é o codigo de rastreio?")
# if cod == "s":
#     print("Sua entrega vai ser para região sul")
# elif cod == "n":
#     print(" Sua entrega será para o norte")
# else: print("Sua entrega é internacional")

# EX: 7

# print("Liberação de carga")
# moto = str(input("Você é um motorista registrado? "))

# check = str(input("Qual é o estado do seu CheckList? "))
# if moto == "sim" and check == "concluído": 
#     print("Liberado boa viagem")
# else: print("Passagem negada")
# Ex 8
# print("Bem vindo ao Cálculo de Atrasos: ")
# n1= float(input("Qual é o total de peças entregas "))
# n2 = float(input("Quantas se atrasaram "))
# n3 =  n2/n1 *100
# print(f"A porcentagen de atraso é {n3} %")
# if n3 >10:
#     print("Melhore sua eficiencia")
# else: print("Sua eficiencia está ótima")




# EX 9 

# print("Bem vindo a calibragem de pneu")
# pneu = int(input("Quantos PSi tem seu pneu? "))
# if pneu >110:
#     print("Está acima do recomendado")
# elif pneu >=100:
#     print("Seu pneu está dentro do padrão")
# elif pneu <100:
#     print("Seu pneu está abaixo do recomendado")

# EX 10
# for i in range (5,0,-1):
#     print (i)


#EX 11

# n1 = ""
# print("Calculo de frete")

# for fr in range (1,6):
#     frete = float(input(f"Qual é o valor do frete{fr} "))
#     if frete > 0:     
#       print( frete + fr)
#     elif frete <=0:
#        break
    
    
  
   

   
    
   



# Ex 12
# n1 = int(input("Qual é a maior quilometragem"))
# for i in range (1,5):
#     veiculos = str(input(f"Qual é a velocidade do veiculo {i} "))
#     print(f"sendo mais rapido  {n1}")

# Ex 13:
for i in range (1,4):
           while i <4:
        
            cod =str(input("Qual é o codigo "))
            if cod == "oi":
                print("Acesso liberado")
                break
            else: print("Codigo errado")        
            break
















