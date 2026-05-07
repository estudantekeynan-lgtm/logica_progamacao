# # # # # print("seja bem vindo ao registro de veiculos ")
# # # # # veiculo= str(input("Qual é o modelo do seu veiculo "))
# # # # # placa = str(input("Qual é a placa do seu veiculo "))
# # # # # print(f"Veículo {veiculo} de placa {placa} registrado no sistema. Boa viagem!")


# # # # print("Olá seja bem vindo ao calculo de KM/L")
# # # # capacidade_tanque = float(input("Qual é a capacidade total do seu tanque " ))
# # # # quilometros_litro = float(input("Quantos Km por litro faz o seu veículo "))
# # # # print(f"O seu veículo com o tanque cheio consegue percorrer {capacidade_tanque*quilometros_litro}km")

# # # # print("Conversor de Moeda (Frete Internacional)")
# # # # valor_frete = float(input("Valor de frete em Dolar"))
# # # # conversao_real = float(input("Valor da taxa em reais "))
# # # # total_conversao = valor_frete * conversao_real
# # # # print(f"O valor do frete foi {valor_frete} e a taxa aplicada foi de {conversao_real} e o total do frete {total_conversao:.2f}") # :.2f para exibir com duas casas decimais
# # # # print("O valor do frete foi",valor_frete,"E a taxa aplicada foi de",conversao_real,"e o total do frete",round(total_conversao,2))
# # # print("Média de Entrgas")
# # # rota1 = int(input("Digite a primeira rota em horas "))
# # # rota2 = int(input("Digite a segunda rota em horas "))
# # # rota3 = int(input("Digite a terceira rota em horas "))
# # # média = (rota1 + rota2 + rota3) /3
# # # print(f"A media das suas rotas são {média:.1f} horas")


# # # print("Monitoramento de cargas em toneladas")
# # # peso_caminhao = float(input("Informe o peso do seu caminhão em TON"))
# # # if peso_caminhao <10:
# # #     print("carga leve")

# # # elif peso_caminhao <25:
# # #     print("Carga padrão")
# # # else: print("Carga muito alta")
# # # while True:
# # #  print("Classificador de destino- Codigo de cargas")
# # #  codigo_carga=input("Qual é o codigo da sua carga (escreva tudo em maiusculo)\n")
# # #  if codigo_carga =="N".upper():
# # #     print("Sua entrega irá para zona norte")
# # #  elif codigo_carga =="S".upper():
# # #     print("Sua entrega sera enviada para zona sul")
# # #  else: print("Sua entrega é internacional")
# # print("Liberação  de Saida - Cheklist e motorista")
# # cheklist = input("o checklist foi realizado? (sim ou não) ")
# # motorista = input("Você é um motorista verificado (sim ou não) ")
# # if cheklist == "sim" and motorista == "sim":
# #     print("Boa viagem ")
# # else: print("Desculpe mas você não pode seguir viagem ")
# # print("Calculo de atraso")
# # entregas_agendadas = int(input("Quantas entregas foram agendadas"))
# # entregas_atrazo= int(input("Quantas entregas foram atrazadas"))
# # total = entregas_atrazo/entregas_agendadas
# # if total > 0.1:
# #     print("Necessario otimizar ")
# # else: print("logistica eficiente")


# # print("Calibraçãp de pneu")
# # calibragem = float(input("Qual é a calibragem do pneu"))
# # if calibragem <100:
# #     print("Abaixo do recomendado")
# # elif calibragem <110:
# #     print("recomendado")

# # else: print("Acima do recomendado")
# # import time
# # print("Contagem de embarque")
# # for embarque in range (5,0,-1):
# #     time.sleep(1)
# #     print (f"O portão de embarque fechara em {embarque} ")
# # time.sleep(1)
# # print("O portão foi f
# # print("Somatorio de frete")
# # faturamento = 0
# # frete = 1
# # while frete !=0:
# #     frete = float(input("Valor do frete ou 0 para encerrar "))
# #     faturamento += frete
# #     print(f"Faturamento total foi de {faturamento} ")







# # var = 0
# # print("Monitoramento de Frota - Km - Versão 2.0")
# # veiculo1 = int(input("Informe a KM do veiculo 1"))
# # for km in range(2,6):
# #     veiculos = float(input(f"Informe a KM do veiculo{km}registrada"))
# # #     if veiculos > var:
# #         var = var + veiculos
# #     # print(f"A maior KM foi de {var}")



# # print("Sistemas de rastreio")
# # erros = 0
# # tentativas = 3

# # while erros != 3:
# #     codigo = input("Qual é o codigo")
# #     if codigo != "track99":
# #         erros = erros +1
# #         tentativas = tentativas -1
# #         print(f"Você tem {tentativas} tentativas")
# #     else: 
# #         break
# #     if erros == 3:
# #         print("Rastreamento bloqueado")
# #     else: print("Acesso bloqueado")


# print("Gerenciador de Combustível")
# tanque = 500
# while True:
#     print("1 - Abastecer")
#     print("2 - Retirar")
#     print("3 - Sair")
#     opcao = input("Escolha uma opção")
#     if opcao == "1":
#         valor = float(input("Quantidade a abastecer"))
#         tanque += valor
#         print(f"Tanque atual: {tanque}")
#     elif opcao == "2":
#         valor = float(input("Quantidade a retirar"))
#         if valor > tanque:
#             print("Quantidade indisponível")
#         else:
#             tanque -= valor
#             print(f"Tanque atual {tanque}")
#     elif opcao == "3":
#         print("Encerrando o Sistema")
#         break
#     else:
#         print("Opção Inválida")
#         if tanque < 50:
#             print("Reserva Critica")





# print("Relatório de Inspeção de Pneus")
# contagem = 0
# total = 5
# for pneu in range(1,6):
#     medida = float(input(f"Medida do sulco do pneu {pneu} em mm"))
#     if medida >= 1.6:
#         contagem = contagem + 1
#         print("Pneu aprovado e adicionado a contagem :)")
#     else:
#         print("Pneu fora das medidas regulares não foi adicionado a contagem")
#         pass 
#     porcentagem = (contagem / total) * 100
#     print(f"Tiveram {contagem} pneus aprovados hoje com uma taxa de {porcentagem}% de conformidade")







































    






































