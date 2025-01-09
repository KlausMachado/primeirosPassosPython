def main():
    while True:
        try:
            def verifica_triangulo():
                print("Digite os comprimentos das três retas:")
                print("Substitua a (,) por (.) ")
    
                # Entrada dos comprimentos
                r1 = float(input("Primeira reta: "))
                r2 = float(input("Segunda reta: "))
                r3 = float(input("Terceira reta: "))
    
                # Verifica a condição de existência de um triângulo
                if (r1 + r2 > r3) and (r1 + r3 > r2) and (r2 + r3 > r1):
                    print("As retas podem formar um triângulo!")
                else:
                    print("As retas NÃO podem formar um triângulo.")
            
            # Chamada da função
            verifica_triangulo()
        
        except ValueError:
            print("Por favor, insira um número válido.")
        
        # Verifica se o usuário deseja continuar
        continuar = input("\nDeseja verificar outro triângulo? (s/n): ").strip().lower()
        if continuar != 's':
            print("Até a próxima!")
            break

main()
