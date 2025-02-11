def main():
    while True:
        nome = str(input("Digite seu nome: "))
        print(f"Seu nome em maiusculas fica: {nome.upper()}")
        print(f"Seu nome em minusculas fica: {nome.lower()}")
        
        nome_sem_espaco = len(nome.replace(" ",""))
        print(f"Seu nome tem {nome_sem_espaco} letras")
        
        primeiro_nome = nome.split()[0]
        ultimo_nome = nome.split()[-1]
        print(f"O seu primeiro nome é {primeiro_nome} e ele tem {len(primeiro_nome)} letras")        
        print(f"O seu ultimo nome é {ultimo_nome} e ele tem {len(ultimo_nome)} letras")
        
        nome = nome.upper().replace(" ", "")
        a = "A"
        if a in nome:
            print(f"A letra A aparece {nome.upper().count(a)} vezes no seu nome")    
            print(f"A primeira letra A aparece na posição {nome.find(a) +1}")
            print(f"A última letra A aparece na posição {nome.rfind(a) +1}")
        
        if "SILVA" in nome:
            print("Você possui Silva no nome. ")    
        
        continuar = input("Deseja analisar outro nome? (s\n) ")
        if continuar.lower() != 's':
            print("Até a proxima!")
            break
main()