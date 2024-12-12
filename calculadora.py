#exericios python cuso em video
#calculdora:
def calculadora(n1, n2, operacao):
    if operacao == "1":
        return n1 + n2
    elif operacao == "2":
        return n1 - n2
    elif operacao == "3":
        if n1 !=0 and n2 !=0:
            return n1/ n2
        else:
            print("Não é possivel dividir por zero")     
    elif operacao == "4":
        return n1 * n2
    elif operacao == "5":
        return n1 ** n2
    elif operacao == "6":
        soma = n1 + n2
        return soma / 2
def main():
    while True:
        n1 = float(input("Digite um valor: "))
        n2 = float(input("Digite outro valor: "))

        print("1. SOMA")
        print("2. SUBTRAÇÃO")
        print("3. DIVISÃO")
        print("4. MULTIPLICAÇÃO")
        print("5. POTENCIAÇÃO")
        print("6. MEDIA")
        operacao = input("Qual operação: ")
        
        resultado = calculadora(n1, n2, operacao)
        print(f"Resultado:{resultado} ")
    
        continuar = input("Deseja realizar outro calculo? (s/n): ")
        if continuar.lower() != "s":
            print("Até a proxima!")
            break
main()
