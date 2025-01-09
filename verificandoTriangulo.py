        def main():
            while True:
               try:
                   def verifica_triangulo():
                        print("Digite os comprimentos das três retas:")
            
                        # Entrada dos comprimentos
                        r1 = float(input("Primeira reta: "))
                        r2 = float(input("Segunda reta: "))
                        r3 = float(input("Terceira reta: "))
            
                        # Verifica a condição de existência de um triângulo
                        if (r1 + r2 > r3) and (r1 + r3 > r2) and (r2 + r3 > r1):
                            print("As retas podem formar um triângulo!")
                        else:
                            print("As retas NÃO podem formar um triângulo.")
                
                except ValueError:
                       print("Por favor, insira um número válido") 
                    # Chamada da função
                    verifica_triangulo()
                
                    # Verifica se o usuário deseja continuar
                    continuar = input("Deseja verificar outro triângulo? (s/n): ").strip().lower()
                    if continuar != 's':
                        print("Até a próxima!")
                        break
        
        main()