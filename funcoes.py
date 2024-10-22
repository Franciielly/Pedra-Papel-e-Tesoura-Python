import random
import os
import time

def limpar_tela(): #Função limpar tela
    os.system('cls' if os.name == 'nt' else 'clear')

def limpar(): #Função que chama a função limpar tela após dar enter
    enter = input("Pressione Enter para continuar....")
    time.sleep(1)
    limpar_tela()

def modo(): #Função que exibe modo de jogo
    modojogo = """
1 - contra máquina
2 - dois jogadores
3 - Sair
"""
    modo = input(modojogo + "Digite o modo do jogo: ")
    return modo

def contramaquina(): #Função para jogar contra o computador
    opcoes = ['pedra', 'papel', 'tesoura']
    pontosC = 0
    pontosJ = 0
    nome1 = "Computador"
    limpar()

    nome = input("Digite seu nome: ")
    limpar()

    while True:
        jogador = input(f"{nome}, escolha Pedra, Papel ou tesoura(ou Voltar para voltar ao menu inicial): ").lower()

        if jogador == "voltar":
            print("Retornando ao menu inicial......")
            time.sleep(1)
            limpar_tela()
            break
        elif jogador not in opcoes:
            print("Opção inválida. Tente novamente.")
            continue

        computador = random.choice(opcoes) #Função que sorteia algum elemento da lista opções

        print(f"\nO computador escolheu {computador}.\n")

        if computador == jogador:
            print("Empate!")
            

        elif jogador == "pedra" and computador == "tesoura" or jogador == "tesoura" and computador == "papel" or jogador == "papel" and computador == "pedra":
            print(f"{nome} venceu!")
            pontosJ += 1
    
        else: 
            print("Computador venceu!")
            pontosC += 1
        
        exibirPontos(nome1, nome, pontosC, pontosJ)
        limpar()

def exibirPontos(nome1, nome2, pontos1, pontos2): #Função que exibe pontos
    print(f"\n{nome1} = {pontos1}")
    print(f"{nome2} = {pontos2}")
 
def doisJogadores(): #Função para jogar duas pessoas
    opcoes = ['pedra', 'papel', 'tesoura']
    pontos1 = 0
    pontos2 = 0

    limpar()
    nome1 = input("Digite o nome do jogador 1: ")
    nome2 = input("Digite o nome do jogador 2: ")
    

    while True:
        jogador1 = input(f"{nome1}, escolha Pedra, Papel ou tesoura(ou Voltar para voltar ao menu inicial): ").lower()
        if jogador1 == "voltar":
            print("Retornando ao menu inicial......")
            time.sleep(1)
            limpar_tela()
            break
        elif jogador1 not in opcoes:
            print("Opção inválida. Tente novamente.")
            continue
        limpar_tela()

        print("Agora é vez do 2º jogador")
        limpar()

        jogador2 = input(f"{nome2}, escolha Pedra, Papel ou tesoura(ou Voltar para voltar ao menu inicial): ").lower()
        if jogador2 == "voltar":
            print("Retornando ao menu inicial......")
            time.sleep(1)
            limpar_tela()
            break
        elif jogador2 not in opcoes:
            print("Opção inválida. Tente novamente.")
            continue
        limpar_tela()

        print(f"{nome1} escolheu {jogador1}.")
        print(f"{nome2} escolheu {jogador2}.\n")

        if jogador1 == jogador2:
            print("Empate!")
        
        elif jogador1 == "pedra" and jogador2 == "tesoura" or jogador1 == "tesoura" and jogador2 == "papel" or jogador1 == "papel" and jogador2 == "pedra":
            print(f"{nome1} venceu!")
            pontos1 += 1
        
        else:
            print(f"{nome2} venceu!")
            pontos2 += 1
        
        exibirPontos(nome1, nome2, pontos1, pontos2)
        limpar()
