# O predio possui 10 andares, sendo o térreo o andar 0. O elevador pode se mover para cima e para baixo , e tem a capacidade  de transportar até 5 pessoas.
# O elevador começa no andar 0 e pode ser chamado por qualquer pessoa em qualquer andar.
# o elevador deve se mover para o andar onde a pessoa chamou, e depois para o andar destino da pessoa.
# o elevador deve exibir mensagens indicando o andar atual, o número de pessoas no elevador, e as ações realizadas (subindo,descendo,parando). O programa deve continuar rodando até que usúarios decida encerrar



#Levantamento de requisitos
#-RF:
#qualquer pessoa pode chama-lo de qualquer andar, Deve se mover para o andar que a pessoa chamou , e depois parar nop andar desejado, número maximo de pessoas e O elevador pode se mover para cima e para baixo

#RFN:
#O elevador começa no andar 0,  o elevador deve exibir mensagens indicando o andar atual, o número de pessoas no elevador, e as ações realizadas (subindo,descendo,parando)



andares_predio = 10
import time

while True:
    print("Bem vindo ao elevador")
    pessoas = int(input("Qual é o número de pessoas no elevador? "))
    if pessoas <=5:

    
        andar_atual = int(input("Qual é o seu andar atual? "))
    
        time.sleep(1)
        andar_desejado = int(input("Qual é o seu andar desejado? "))
        
        
        if  andar_atual < andar_desejado:
            def subir (locomocao = andar_desejado - andar_atual):
                return locomocao
            passando = andar_atual
            for i in range (subir()):
                passando +=1
                time.sleep(0.5)
                print(f"subindo ↑↑↑ andar atual: {passando}")            
                         
            
                time.sleep(1)
        elif andar_atual >andar_desejado:
            def descer (locomocao_baixo = andar_atual - andar_desejado):
                return locomocao_baixo
            passando = andar_atual
            for i in range(descer()):
                passando -=1
                time.sleep(0.5)
                print(f" descendo ↓↓↓  andar atual: {passando}")
                
    else: print(f"Por favor desça pelo menos {pessoas -5} pessoas!")
    