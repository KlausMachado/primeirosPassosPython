largura = float(input("Qual a largura da sua parede? "))
altura = float(input("Qual a altura da sua parede? "))

area = largura * altura
tinta = area / 2
print(f"Sua parede tem a dimensão de {largura}x{altura} e sua area é de {area}m")
print(f"Para pintar essa parede, você precisa de {tinta}l de tinta")
