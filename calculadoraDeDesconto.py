def main():
    while True:
        preco = float(input("Qual o valor do produto? "))
        for p in range(5, 30, 5):
            desconto = preco * p / 100
            valor_final = preco - desconto
            print(f"O valor total é de {preco}, com o desconto de {p}% o valor final será {valor_final}")

        novoDesc = input("Quer calcular novamente? (s/n)")    
        if novoDesc.lower() != "s":
            print("Até a proxima")
            break
main()    
