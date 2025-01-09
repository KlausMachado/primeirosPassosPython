import random

def main():
    while True:
        print("-------------------------------------------------------------------")
        print("Bem-vindo ao jogo de adivinhação!")
        print("Estou pensando em um número entre 1 e 10.")
        print("-------------------------------------------------------------------")
        
        # Gera o número aleatório
        numero_secreto = random.randint(1, 10)
        
        #contador de tentativas inicia em 0
        tentativas = 0
        
        # Inicializa a variável do chute
        acertou = False
        
        while not acertou:
            try:
                chute = int(input("Qual o seu chute? "))
                tentativas += 1 #incrementa a tentativas a cada loop
                
                if chute == numero_secreto:
                    print(f"Parabéns! Você acertou em {tentativas} tentativas!")
                    acertou = True
                elif chute > numero_secreto:
                    print("Uh! Foi quase, mas o número em que eu pensei é menor.")
                    print("\nTente novamente")
                else:
                    print("Uh! Foi quase, mas o número em que eu pensei é maior.")
                    print("\nTente novamente")
            except ValueError:
                print("Por favor, insira um número válido.")
                print("\nTente novamente")
        
        # Pergunta se o usuário quer jogar novamente
        continuar = input("Deseja jogar novamente? (s/n): ").strip().lower()
        if continuar != 's':
            print("Até a próxima!")
            break

main()