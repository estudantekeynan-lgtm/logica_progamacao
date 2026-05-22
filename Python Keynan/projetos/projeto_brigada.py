# #Contexto
# #O Serviço Especializado em Engenharia de Segurança e em Medicina do Trabalho
# (SESMT) precisa automatizar o controle de treinamentos obrigatórios (como CIPA,
# Brigada de Incêndio e NR-35) e a entrega de Equipamentos de Proteção Individual (EPIs).
# Objetivo
# Desenvolva um programa em Python que gerencie o status de conformidade dos
# funcionários de uma empresa.

# RF: Armazenamento de dados, verificação de EPI, e liste os EPI Se o treinamento tiver mais de 2 anos, exiba a mensagem: "Treinamento Vencido! Encaminhar para reciclagem." Caso contrário, exiba: "Treinamento Válido." Exiba na tela um resumo com o total de funcionários cadastrados e quantos
# estão com treinamentos em dia.

# RFN: Criar uma função que receba o ano do último treinamento da Brigada de
# Incêndio.

EPI_eletrica = [
    "capacete de segurança classe B",
    "luvas isolantes de borracha",
    "luvas de cobertura",
    "calçado dielétrico",
    "vestimenta de proteção ATPV",
    "óculos de segurança",
    "protetor facial contra arco elétrico",
    "cinturão de segurança com talabarte",
    "protetor auricular",
]

EPI_trabalho_altura = [
    "capacete de segurança com jugular",
    "cinturão de segurança tipo paraquedista",
    "talabarte em Y com absorvedor de energia",
    "dispositivo trava-quedas",
    "calçado de segurança com biqueira",
    "luvas de proteção",
    "óculos de segurança",
    "protetor auricular",
]

ano_atual = 2026
funcionarios_cadastrados = 0
funcionarios_em_dia = 0

print("Bem-vindo ao sistema de controle de treinamentos e EPIs do SESMT!")

while True:
    print("\nMenu:")
    print("1. Verificar treinamento da Brigada de Incêndio")
    print("2. Sair")

    escolha = input("Digite o número da opção desejada: ").strip()

    if escolha == "1":
        nome = input("Qual é o seu nome?: ").strip()
        setor = input(
            "Qual é o seu setor?\n"
            " 1- Elétrica\n"
            " 2- Altura\n"
            " 3- Brigada\n"
            "Digite a opção: "
        ).strip()

        if setor == "1":
            setor_nome = "Elétrica"
            epis_necessarios = EPI_eletrica
        elif setor == "2":
            setor_nome = "Trabalho em Altura"
            epis_necessarios = EPI_trabalho_altura
        elif setor == "3":
            setor_nome = "Brigada"
            epis_necessarios = []
        else:
            print("Opção de setor inválida. Tente novamente.")
            continue

        if epis_necessarios:
            print(f"Os EPIs necessários para o setor {setor_nome} são:")
            for e in epis_necessarios:
                print(f" - {e}")
        else:
            print(f"Não há lista de EPIs específica para o setor {setor_nome}.")

        verificar_EPI = input("Seus EPIs estão válidos?\n1- Sim\n2- Não\nDigite: ").strip()

        if verificar_EPI != "1":
            print("Você não está apto a este serviço.")
            continue

        while True:
            ano_ultimo_treinamento = input(
                f"{nome}, digite o ano do último treinamento da Brigada de Incêndio: "
            ).strip()
            if ano_ultimo_treinamento.isdigit():
                ano_ultimo_treinamento = int(ano_ultimo_treinamento)
                break
            print("Ano inválido. Por favor digite um valor numérico.")

        funcionarios_cadastrados += 1
        if ano_atual - ano_ultimo_treinamento > 2:
            print("Treinamento Vencido! Encaminhar para reciclagem.")
        else:
            print("Treinamento Válido")
            funcionarios_em_dia += 1

        print(
            f"Resumo: {funcionarios_cadastrados} funcionário(s) cadastrados, "
            f"{funcionarios_em_dia} com treinamento em dia."
        )

    elif escolha == "2":
        print("Encerrando o programa. Até mais!")
        break
    else:
        print("Opção inválida. Digite 1 ou 2.")

