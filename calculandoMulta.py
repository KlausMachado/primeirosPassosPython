import random

def main():
    while True:
        try:
            # Solicita a velocidade e o limite ao usuário
            limite = int(input("Qual o limite de velocidade permitido? "))
            velocidade = int(input("Qual a velocidade atual do carro? "))            
            
            if velocidade <= 0:
                print("Velocidade invalida!")    
            elif velocidade <= limite:
                print("Você está dentro da velocidade permitida, faça uma boa viagem!")                   
            elif velocidade > limite:
                multa = (velocidade - limite) * 7
                print("\nMULTADO!")
                print(f"Você está acima do limite de velocidade. O valor da multa é R${multa:.2f}.")             
            
        except ValueError:
            print("Por favor, insira um número válido para a velocidade.")
        
        # Pergunta se o usuário quer verificar multa novamente
        continuar = input("\nDeseja verificar se há multa novamente? (s/n): ").strip().lower()
        if continuar != 's':
            print("Até a próxima!")
            break

main()