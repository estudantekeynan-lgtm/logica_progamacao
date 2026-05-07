# # # print("Hello world")
# # # manipulacao_arquivos = "Manipulação de arquivos e texto com Python Clean code PYTHON"
# # # print(manipulacao_arquivos.upper()) #Maiusculo
# # # print(manipulacao_arquivos.lower()) #minusculo
# # # print(manipulacao_arquivos.strip()) #Remove espaços
# # # print(manipulacao_arquivos.split()) # Divide a string em uma lista de palavras
# # # print(manipulacao_arquivos.replace("Python","Java")) #Substitui a palavra "Python" por "Java"
# # # print(manipulacao_arquivos.count("a")) #conta a quantidade de letras selecionadas
# # # print(manipulacao_arquivos.strip().count("Python"))
# # # print(manipulacao_arquivos.upper().count("PYTHON")) # Conta quantas vezes a letra "PYTHON" aparece na string e converte para maiúsculas
# # # print(manipulacao_arquivos.find("Python"))
# # # print(manipulacao_arquivos.title())
# # # print(manipulacao_arquivos.swapcase()) #converte maiuscalo para minuscolo e vice - verso
# # # print(manipulacao_arquivos.startswith("   Manipulação"))#Verificar se a string começa com "       Manipulação"
# # # print(manipulacao_arquivos.center(50, "*")) # Centraliza a string e preenche com "*" até atingir 50 caracteres
# # # print(manipulacao_arquivos.capitalize()) # Converte a primeira letra da string para maiúscula e o restante para minúscula


# # # Exercicio 1:
# # # Crie um algoritmo onde peça para inserir uma frase e deixa-a formatada com maiuscula e acrescente uma contagem de cada frase.

# # # frase= input("Insira uma frase ")
# # # print(frase.upper())
# # # print(frase.count(""))

# # #Manipulação de arquivos
# # #escrevendo arquivo
# # # with  open ("arquivo.txt","w") as exemplo:
# # #     exemplo.write("Exemplo clean code - aula 8 \n")
# # #     exemplo.write("Continuando a escrever\n")
# # # with open ("arquivo.py", "w") as python:
# #     # python.write('print("Exemplo de arquivos Python")')
# # # with open ("arquivo.py","r") as exemplo:
# # #     conteudo = exemplo.read()
# # # #     print(conteudo)
# # # with open ("arquivo.py","a") as python:
# # #     python.write('\nprint("Continuando a escrever no arquivo python")')
# # #     python.write('\nprint("Mais uma linha no arquivo python")')
# # #     python.write('\nprint("ultima linha do arquivo")')
# #     # a = append - Adiciona conteúdo ao final do arquivo, se o arquivo não existir, ele irá criar um novo arquivo.
# # # Manipulação de Sistema Operacional
import os #Biblioteca para manipulação de arquivos e diretórios
# # # Criando um diretorio
# # # os.mkdir("Teste")
# # os.rename("Teste","Aulas")

# os.rmdir("Aulas") #Excluir a pasta

# print(os.listdir())#lista os arquivos e pastas
# print(os.listdir(".."))#lista os arquivos da pasta pai
# print(os.listdir("C:\\"))#lista os arquivos e pasta do diretorio raiz

#Exercicio 2:
# Crie um algoritmo para criação de um arquivo que irá desligar o computador.
# with open ("desligar.bat","w") as desligar:
#     desligar.write('shutdown /s /t 20 /c "Desligando o pc"')

# with open ("Cancelar_Shutdown.bat","w") as cancelar:
#     cancelar.write("shutdown /a")

print(os.listdir(".."))
