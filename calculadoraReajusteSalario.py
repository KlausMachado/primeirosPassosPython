def main():
    while True:
        salario = float(input("Qual o salario do funcionario? "))
        aumento = float(input("Qual a porcentagem do aumento? "))
        valor_aumento = float(salario * aumento / 100)
        novo_salario = float(salario * aumento / 100 + salario)
    
        print(f"O novo valor do salario será de {novo_salario:.2f}, o valor do aumento foi de {valor_aumento:.2f}.")
        
        novoCalculo = input("Gostaria de realizar um novo calculo? (s/n)")
        if novoCalculo.lower() != "s":
            print("Até a próxima")
            break
main()
    