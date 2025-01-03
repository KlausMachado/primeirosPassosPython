def main():
    while True:
        quantidadeDias = float(input("Por quantos dias o cliente utilizou o automóvel? "))
        quilometragemPercorrida = float(input("Quantos KM o automóvel percorreu? "))
        valorPorDias  = quantidadeDias * 60.00
        valorPorKM = quilometragemPercorrida * 0.15
        print(f"O valor total está em R${valorPorDias + valorPorKM:.2f}. O valor por dias de uso foi de R${valorPorDias:.2f} e R${valorPorKM:.2f} foi o valor gasto por KM rodado.")

        novoDesc = input("Quer realizaro novo calculo? (s/n)")    
        if novoDesc.lower() != "s":
            print("Até a proxima")
            break
main()    