from datetime import date

def main():
    while True:
        try:
            ano = int(input("Digite o ano que deseja verificar se é bissexto. Coloque 0 para analisar o ano atual: "))
            
            # Verifica o ano atual se for 0
            if ano == 0:
                ano = date.today().year
            
            # Verifica se é bissexto
            if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                print(f"O ano {ano} é BISSEXTO.")
            else:
                print(f"O ano {ano} NÃO é BISSEXTO.")
        
        except ValueError:
            print("Por favor, insira um número válido.")
        
        # Pergunta se o usuário quer continuar
        continuar = input("\nDeseja analisar outro ano? (s/n): ").strip().lower()
        if continuar != 's':
            print("Até a próxima!")
            break

main()