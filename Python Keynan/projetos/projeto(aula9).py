# print("Hello World")
# print("Hello World")
num_vagas = 500
import time
while num_vagas >=1:
    print("Seja bem vindo ao Shopping Center")
    print("Atenção⚠️  caso perca o ticket, será cobrado uma multa de R$50,00")
    
    tipo_acesso = int(input("Qual é o seu tipo de acesso \n 1- tag \n 2- ticket \n 3- Sair\n"))
    if tipo_acesso == 3:
        break
    if tipo_acesso == 1:
        time.sleep(1)
        hora_entrada = float(input("Qual é a hora de entrada? "))
        print("Seja bem vindo, pode entrar")
        time.sleep(1)
        hora_saida = float(input("Insira a hora da saída: "))
        totaltag_horas = hora_saida - hora_entrada
        if totaltag_horas <= 0.25:
            print("Grátis")
        elif totaltag_horas <=3:
            valortag_3horas = 15 * 0.1
            print(f"O valor a ser pago é de {15 -valortag_3horas}")
        elif totaltag_horas >3:
           horastag_extras = totaltag_horas -3
           valortag_maior_3_horas = (horastag_extras *3) +15
           valortag_3horas_desconto= valortag_maior_3_horas * 0.1
           print(f"O total a ser pago é {valortag_maior_3_horas - valortag_3horas_desconto }")
           print("Obrigado volte sempre")
           
           num_vagas = num_vagas -1
        
    elif tipo_acesso == 2:
        print(f"Atualmente temos {num_vagas} vagas")
        time.sleep(1)
        hora_entrada_ticket = float(input("Qual é a hora de entrada? "))
        print("Retire seu ticket e boas compras")
        time.sleep(1)
        hora_saida_ticket = float(input("Qual é o horário de saída? "))
        time.sleep(1)
        perca_ticket = str(input("Apresente o ticket \n 1- apresentar ticket \n 2-perdi meu ticket\n"))
        if perca_ticket == "2":
            print("Você terá que pagar uma taxa de R$50,00")
        else:
            total_ticket_horas = hora_saida_ticket - hora_entrada_ticket
            if total_ticket_horas <= 0.25:
                print("Grátis")
            elif total_ticket_horas <=3:
                valor_ticket_3horas = 15
                print(f"O valor a ser pago é R${valor_ticket_3horas},00.")
            elif total_ticket_horas >3:
                horas_extras_ticket = total_ticket_horas -3
                valor_ticket_horas_extras = (horas_extras_ticket *3) +15
                print(f"O valor a ser pago é R${valor_ticket_horas_extras} ")
                print("Obrigado volte sempre")
                

    num_vagas = num_vagas -1
else: print("Opção invalida")

    




































