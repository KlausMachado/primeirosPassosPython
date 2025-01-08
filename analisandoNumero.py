 def main():
    while True:
        n = int(input("Digite um numero entre 0 e 9999: "))
        numeroStr = str(n).replace(" ", "")
        print("Analizando o numero")
        print(f"Digitos: {len(numeroStr)}")
        print(f"Dezenas: {int(n / 10)}")
        print(f"Centenas: {int(n / 100)}")
        print(f"Milhar: {int(n / 1000 )}")
        
        
        continuar = input("Deseja analisar outro numero? (s\n) ")
        if continuar.lower() != 's':
            print("Até a próxima")
            break
main()