# # #Lista de temperatura lidas pelo sensor por minutos
# # leituras = [70,75,82,98,110,85,80]
 
# # for temp in leituras:
# #     if temp > 100:
# #         print(f"CRITICO: {temp}°C detectado! Acionando parada de emergência.")
# #         break # o loop para aqui e NÃO lê os proximos valores (85 e 80)
# #     print(f"Temperatura está em {temp}°C. Operação normal")
# # print("Sistema desligado. Aguardando manutenção")
# # baixos = [51,55,52,30,20,10]
# # temperatura = [90,80,70,110,50,30,5]
# # for temp in temperatura:
# #     if temp > 100 :
# #         print(f"ERRO {temp}°C detectado! Acionando parada de emergencia")
# #         break
# #     for temp1 in baixos:
# #        if temp <50 :
# #         print(f"Critico: {temp1}°C. Operação com valores baixos")
# #         break
# #        else:
# #             print(f"Temperatura está em {temp1}°C. Operação com valores normais.")
# # print("Checar Sistema. Aguardando manutenção")
     
# # material = ["metal","metal","plástico","metal","vidro","metal"]
# # for peca in material:
# #     if peca != "metal":
# #         print(f"Aviso: Peça de {peca} detectada. Desviando para o descarte ")
# #         continue
# #     print(f"Processando peça de  {peca}. Furando e polindo")
# # print("Fim da produção")

# # exercicio 1
# # Tente criar um código que conte de 1 a 10 , mas use o continue para não imprimir o número 5(simulando uma falha no 5)

# # from time import sleep
# # for numeros in range (1,11):
# #     if numeros == (5):
# #         print("Falha ao imprimir o número 5")
# #         sleep(3)
# #         continue
# #     print(f"listando os números {numeros}")
# #     sleep(2)
# # print(" Fim")


# # from time import sleep
# # cores = ["Verde","Amarelo","Vermelho"]
# # for sinal in cores:
# #     if sinal == "Verde": 
# #         print("Siga em frente")
# #     sleep(2)
# #     if sinal == "Amarelo":
        
# #         print("Atenção")
# #     sleep(0.5)
# #     if sinal == "Vermelho":
        
# #         print("Pare!")
# #     sleep(4)

# # Exercício 3 - Soma de Cargas de Energia (for)
# # Uma fábrica tem 5 máquinas. Peça ao usuário (via input dentro do loop) o consumo em kWh de cada uma das 5 máquinas. Ao final do loop, o programa deve exibir o consumo total da fábrica.

# # maquinas = ("maquina 1","Maquina 2", "maquina 3", "maquina 4", "maquina 5")
# # for i in maquinas :
# #    m1 = input(f"Qual é o consumo da maquina {i} ")
   

# # resultado = m1 
# # print(f"O consumo das maquinas são {resultado}Kwh")

# # Exercício 4 - Identificador de Peças Defeituosas (for + if)
# # Percorra uma lista de medidas de peças: 
# # medidas = [50.1, 49.8, 52.0, 50.0, 48.5].
# # O padrão de qualidade aceita apenas peças com exatamente 50.0 ou mais.
# # Use um for para ler a lista e, para cada peça, diga se ela está "Aprovada" ou "Rejeitada".
# # medidas = [50.1, 49.8, 52.0, 50.0, 48.5]
# # for pecas in medidas:
# #     if pecas >= 50:
# #         print(f"peça {pecas} aprovada")
# #     else:
# #         print(f"Peça {pecas} rejeitada ")
# #Exercício 5 - Uma balança industrial está pesando um lote de 6 sacos de insumos. O peso ideal de cada saco é 50kg, mas o sistema aceita variações.

# # sacos = [49.5, 50.0, 51.2, 48.9, 50.5, 47.8]
# # for peso in sacos:
# #     if 49.0 <= peso <= 51.0:
# #         print(f"Saco com peso {peso}kg: Aceitável")
# #     else:
# #         print(f"Saco com peso {peso}kg: Rejeitado - Fora do limite aceitável")


# # O Desafio: Gestão de Ciclo Térmico
# # Você deve criar um programa que monitore a temperatura de uma estufa que processa um lote de 5 peças.
# # Regras do Sistema:
# # O programa deve rodar em um loop até que 5 peças válidas sejam processadas.
# # Para cada peça, peça ao usuário a temperatura atual (input).
# # Filtro de Erro (continue): Se o usuário digitar uma temperatura negativa, exiba "Erro de leitura no sensor" e use o continue para pedir a temperatura novamente (essa leitura não conta como peça processada).
# # Parada de Emergência (break): Se a temperatura for maior que 150°C, o sistema deve exibir "ALERTA CRÍTICO: Risco de Explosão!", interromper o loop imediatamente e encerrar o programa
# # while True: 
    
# #     pecas = ("peça 1", "peça 2","peça 3", "peça 4", "peça 5",)
# #     for i in pecas :
# #         temp = int(input(f"Qual é a temperatura da  {i} :"))
# #         if temp <0 :
# #             print("Erro de Leitura do sensor")
# #             continue
# #         if temp >150 :
# #             print("Parando a máquina  Alerta risco de Explosão")
# #             break
# #         else: print(f"{i} processadas com sucesso")
   

# # Exercicio 7 - Monitoramento de Vibração
# # Uma máquina industrial tem um sensor de vibração que registra os seguintes valores em mm/s: [0.5, 1.2, 0.8, 2.5, 0.3, 1.0, 3.0, 0.4]. O limite de vibração aceitável é de até 1.5 mm/s.
# # Crie um programa que percorra a lista de vibração e:
# # - Se a vibração for maior que 1.5 mm/s, exiba "ALERTA: Vibração excessiva detectada!" e continue para a próxima leitura.
# # - Se a vibração for menor ou igual a 1.5 mm/s, exiba "Vibração dentro do limite aceitável." para cada leitura.
# vibracao =  [0.5, 1.2, 0.8, 2.5, 0.3, 1.0, 3.0, 0.4]
# for i in vibracao:
#     if vibracao >= 1.5:
#      print(f"Vibração excessiva detectada!")
#      if vibracao  <= 1.5:
#         print("Vibração dentro do limite aceitável.")















































































