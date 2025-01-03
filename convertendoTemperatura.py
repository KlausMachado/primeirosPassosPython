def main():
    while True:
        temperaturaC = float(input("Qual a temperatura em ºC: "))
        temperaturaF = 9 * temperaturaC / 5 + 32
        print(f"A temperatura de {temperaturaC}ºC, corresponde a {temperaturaF}ºF ")

        novoDesc = input("Quer realizar outra converção? (s/n)")    
        if novoDesc.lower() != "s":
            print("Até a proxima")
            break
main()    
