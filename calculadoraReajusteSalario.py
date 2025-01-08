def valor_aumento(salario, aumento):
    return float(salario * aumento / 100)

def novo_salario(salario, aumento):
    return float(salario * aumento / 100 + salario)
    
def main():
    while True:
        salario = float(input("\nQual o salario do funcionario? "))
        aumento = 15        
                
        if salario <= 1250:            
            print(f"O novo valor do salario será de R${novo_salario(salario, aumento):.2f}, o valor do aumento foi de R${valor_aumento(salario, aumento):.2f}.")
        if salario > 1250:
            aumento = 10                
            print(f"O novo valor do salario será de R${novo_salario(salario, aumento):.2f}, o valor do aumento foi de R${valor_aumento(salario, aumento):.2f}.")
        
        novoCalculo = input("\nGostaria de realizar um novo calculo? (s/n)")
        if novoCalculo.lower() != "s":
            print("Até a próxima")
            break
main()
