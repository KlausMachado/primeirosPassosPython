def main():
    while True:
        try:
            n = int(input("Digite um número entre 0 e 9999: "))
            
            # Converte o número para string para análise
            numeroStr = str(n).replace(" ", "")
            
            # Verifica se o número é par ou ímpar
            paridade = "par" if n % 2 == 0 else "ímpar"
            
            # Exibe as informações
            print("\nAnalisando o número...")
            print(f"Digitos: {len(numeroStr)}")
            print(f"Dezenas: {int(n / 10)}")
            print(f"Centenas: {int(n / 100)}")
            print(f"Milhar: {int(n / 1000)}")
            print(f"Este número é {paridade}.")
        
        except ValueError:
            print("Por favor, insira um número válido.")
        
        # Pergunta se o usuário quer continuar
        continuar = input("\nDeseja analisar outro número? (s/n): ").strip().lower()
        if continuar != 's':
            print("Até a próxima!")
            break

main()
