import math

def operacoes(x, y, operacao):
    if operacao == "1":
        if x < 0:
            return "Erro: Não é possível calcular a raiz quadrada de um número negativo."
        raizX, raizY = map(math.sqrt, (x, y))
        return f"A raiz quadrada de {x} e {y} é ({raizX:.2f}, {raizY:.2f})"
    elif operacao == "2":
        arredondandoXCima, arredondandoYCima = map(math.ceil, (x, y))
        arredondandoXBaixo, arredondandoYBaixo = map(math.floor, (x, y))
        return (f"Arredondando os valores para cima: ({arredondandoXCima}, {arredondandoYCima}), "
                f"para baixo: ({arredondandoXBaixo}, {arredondandoYBaixo})")
    elif operacao == "3":
        if x <= 0 or y <= 0:
            return "Erro: Logaritmos naturais requerem valores positivos."
        logaritimoX, logaritimoY = map(math.log, (x, y))
        return f"O logaritmo dos valores são ({logaritimoX:.2f}, {logaritimoY:.2f})"
    elif operacao == "4":
        hipotenusa = math.hypot(x, y)
        return f"A hipotenusa de {x} e {y} é {hipotenusa:.2f}"
    elif operacao == "5":
        senX, senY = map(math.sin, (x, y)) 
        cosX, cosY = map(math.cos, (x, y)) 
        tanX, tanY = map(math.tan, (x, y)) 
        return (f"O seno de x e y é ({senX:.2f}, {senY:.2f}), o cosseno é ({cosX:.2f}, {cosY:.2f}) "
                f"e a tangente é ({tanX:.2f}, {tanY:.2f})")     
    else:
        return "Erro: Operação inválida."
     
def main():
    while True:
        print("\nEscolha uma operação:")
        print("1: Raiz quadrada")
        print("2: Arredondando valores")
        print("3: Logaritmo natural")
        print("4: Hipotenusa")
        print("5: Seno, cosseno e tangente")
        
        operacao = input("Qual operação gostaria de realizar? (1-5): ")
        
        if operacao not in {"1", "2", "3", "4", "5"}:
            print("Erro: Operação inválida. Tente novamente.")
            continue
        
        try:
            x = float(input("Digite o valor de x: "))
            y = float(input("Digite o valor de y: "))
            resultado = operacoes(x, y, operacao)
            print(resultado)
        except ValueError:
            print("Erro: Por favor, insira números válidos.")
        
        continuar = input("\nGostaria de calcular outro número? (s/n): ").lower()
        if continuar != "s":
            print("Até a próxima!")
            break

main()