from funcoes import*

print("\nBem-vindo ao jogo Pedra,Papel ou Tesoura!")
while True:
    escolha = modo() 
    if escolha == "1":
        contramaquina()
    elif escolha == "2":
        doisJogadores()
    elif escolha == "3":
        print("Programa encerrado......")
        time.sleep(1)
        limpar_tela()
        break
    else:
        print("Opção inválida. Tente novamente.")
        limpar()

