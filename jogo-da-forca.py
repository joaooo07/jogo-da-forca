import random

def menu():
    # chute não está sendo usado, então vou removê-lo
    # palavras é uma lista de palavras para escolher
    palavras = ['paralelepipido', 'leptospirose']

    print('=========================================================')
    print("             Bem Vindo ao jogo da Forca. ")
    print('=========================================================')
    print('(1) - Para Escolher a Propria Palavra. ')
    print('(2) - Para o Computador Escolher uma Palavra Armazenada. ')
    opcao = int(input("Digite aqui: "))

    if opcao == 1:
        # Obter a palavra escolhida pelo usuário
        palavra = input("Digite a palavra escolhida: ")

        # Criar uma lista para armazenar as letras chutadas
        guessed_letters = ["_"] * len(palavra) #Cria uma lista de Underline
        #com o mesmo comprimento da string palavra.

        # Imprimir a palavra inicial com underscores
        for letra in range(len(palavra)): #Para cada letra dentro de palavra
            print("_", end=" ")           #Troque a Letra Por UnderLine
        print()                           #Print Vazio Pula Uma Linha

        # Loop do jogo
        while True: #Enquando a Condição for Verdadeira.
            # Obter o chute do usuário
            letra = input("Digite uma letra: ") 

            # Verificar se o input é uma letra única
            if len(letra) != 1:
                print("Você deve digitar apenas uma letra!")
                continue

            # Verificar se a letra está na palavra
            if letra in palavra:
                # Revelar a letra correta
                for i, l in enumerate(palavra):
                    if l == letra:
                        guessed_letters[i] = letra
                print("Parabéns, você acertou uma letra!")
            else:
                print("Erro, letra não encontrada!")

            # Imprimir a palavra atualizada
            for letra in guessed_letters:
                print(letra, end=" ")
            print()

            # Verificar se o usuário ganhou
            if "_" not in guessed_letters:
                print("Parabéns, você ganhou!")
                break

    elif opcao == 2:
        # Escolher uma palavra aleatória da lista
        palavra = random.choice(palavras)
        print("A palavra escolhida é:", palavra)

        # Mesmo loop do jogo acima
        guessed_letters = ["_"] * len(palavra)
        while True:
            letra = input("Digite uma letra: ")
            if len(letra) != 1:
                print("Você deve digitar apenas uma letra!")
                continue
            if letra in palavra:
                for i, l in enumerate(palavra):
                    if l == letra:
                        guessed_letters[i] = letra
                print("Parabéns, você acertou uma letra!")
            else:
                print("Erro, letra não encontrada!")
            for letra in guessed_letters:
                print(letra, end=" ")
            print()
            if "_" not in guessed_letters:
                print("Parabéns, você ganhou!")
                break

    else:
        print("Opção invalida, tente novamente.")
        return menu()

menu()