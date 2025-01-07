import time
import random

# Dados dos alunos
dados_alunos = [
    {"nome": "João Silva", "numero_matricula": 12345},
    {"nome": "Maria Oliveira", "numero_matricula": 12346},
    {"nome": "Carlos Souza", "numero_matricula": 12347},
    {"nome": "Ana Paula", "numero_matricula": 12348},
    {"nome": "Lucas Mendes", "numero_matricula": 12349},
    {"nome": "Fernanda Lima", "numero_matricula": 12350},
    {"nome": "Gabriel Nunes", "numero_matricula": 12351},
    {"nome": "Beatriz Santos", "numero_matricula": 12352},
    {"nome": "Ricardo Alves", "numero_matricula": 12353},
    {"nome": "Julia Costa", "numero_matricula": 12354},
    {"nome": "Pedro Rocha", "numero_matricula": 12355},
    {"nome": "Larissa Martins", "numero_matricula": 12356},
    {"nome": "Renato Faria", "numero_matricula": 12357},
    {"nome": "Camila Andrade", "numero_matricula": 12358}
]

def adicionar_aluno():
    nome = input("Qual o nome do aluno que gostaria de adicionar? ")
    numero_matricula = int(input("Qual a matricula do aluno que gostaria de adicionar? "))
    
    novo_aluno = {"nome": nome.title(), "numero_matricula": numero_matricula}
    dados_alunos.append(novo_aluno)
    print(f"Aluno {nome} adicionado com sucesso")

def deletar_aluno():
    try:
        matricula = int(input("Qual o número de matrícula do aluno que deseja deletar? "))
        
        aluno_para_remover = None
        for aluno in dados_alunos:
            if aluno['numero_matricula'] == matricula:
                aluno_para_remover = aluno
                break
                
        if aluno_para_remover:
            dados_alunos.remove(aluno_para_remover)        
            print(f"Aluno {aluno['nome']} removido com sucesso.")
        else:    
            print('Matricula não encontrada!.')    
    except ValueError:
        print("Numero de matricula invalido.")            

def alterar_aluno():
    try:
        matricula = int(input("Qual o número de matrícula do aluno que deseja alterar? "))
        
        for aluno in dados_alunos:
            if aluno['numero_matricula'] == matricula:
                dados_alunos.remove(aluno)
                novo_nome = input("Qual o nome do aluno que gostaria de adicionar? ")
                nova_matricula = int(input("Qual a matricula do aluno que gostaria de adicionar? "))
                
                aluno_alterado = {"nome": novo_nome.title(), "numero_matricula": nova_matricula}
                dados_alunos.append(aluno_alterado)
                
                print(f"Aluno {novo_nome} alterado com sucesso.")
                return
        print('Matricula não encontrada!.')    
    except ValueError:
        print("Numero de matricula invalido.")

def sortear():
    print("\nSorteando...")
    time.sleep(1) #pausa antes de executar o sorteio            
    sorteado = random.choice(dados_alunos) #metodo para sorteio
    print(f"O aluno sorteado foi: \nNome: {sorteado['nome']}\nMatricula: {sorteado['numero_matricula']}")

def reordenar_alunos():
    random.shuffle(dados_alunos)
    print("A lista de alunos foi reordenada aleatoriamente.")
    listar()
        
def listar():
    print("Aqui está a lista de alunos: ")
    for aluno in dados_alunos: 
        print(f"\n- {aluno['nome']}, matricula número: {aluno['numero_matricula']}")
    
def main():
    while True:
        print("\nBem vindo ao Sorteando um aluno")
        print("\nMenu")
        print("1 - listar alunos")
        print("2 - adicionar novo aluno")
        print("3 - deletar aluno")
        print("4 - alterar aluno")
        print("5 - sortear um aluno")
        print("6 - reordenar lista")
        print("7 - sair")
       
        opcao = input("Escolha uma opção: ").strip()
       
        if opcao == '1':
           listar()
        elif opcao == '2':
           adicionar_aluno()
        elif opcao == '3':
            deletar_aluno()
        elif opcao == '4':
            alterar_aluno()                
        elif opcao == '5':
           sortear()
        elif opcao =='6':
            reordenar_alunos()   
        elif opcao == '7':
            print('Até a proxima')
            break   
        else:
            print("Opção invalida")   
                                                    
        continuar = input("Deseja realizar outra operção? (s/n): ")
        if continuar.lower() != "s":
            print("Até a próxima")
            break
main()