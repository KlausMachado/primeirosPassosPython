numero = int(input("Digite um numero para ver sua tabuada: "))

print(f"tabuada do {numero}: ")

for n in range(1, 11):
    print(f"{numero} X {n} = {numero * n}")
    
