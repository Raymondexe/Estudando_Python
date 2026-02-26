# === Exercício Fila === :
# – Implemente um programa que contemple uma fila de contatos para um call center;
# – As opções do programa devem ser:
#   • Inserir Contato:
#       – Deve solicitar ao usuário os dados e incluir o contato na fila;
# • Próximo Contato:
    # – Deverá pegar o Contato do Inicio da Fila, removê-lo e mostrar os seus dados na tela para o usuário efetuar
# o contato com o cliente.
# • Sair.


class Queue:
    def __init__ (info):
        info.items = []

    def isEmpty(info):
        print("Nenhum contato no momento")
        return info.items == []
    
    def push(info, items):
        info.items.append(items)

    def enqueue(info, contato):
        info.items.insert(0, contato)
        
    def dequeue(info):
        if info.items == []:
            print("A fila está vazia")
            return None
        else:
            return info.items.pop(0)
    
    def breaking():
        print(" === SAINDO === ")

   
fila = Queue()

while True:
    print("Bem vindo(a), Caller")
    escolha = int(input("Escolha: 1 - Solicitar Dados, 2 - Próximo Contato, 3 - Sair "))

    if escolha == 1:
        nomeUser = input("\nInsira o seu nome: " )
        idUser = input("\nInsira o seu id: " )
        telefoneUser = input("\nInsira o seu telefone: ")
        emailUser = input("\nInsira o seu email: ")

        contato = {
            "nomeUser" : nomeUser,
            "idUser" : idUser,
            "telefoneUser" : telefoneUser,
            "emailUser" : emailUser,
        }
        
        fila.enqueue(contato)
        print(contato)
         
    elif escolha == 2:
       contato = fila.dequeue()
       print(contato)
        
    elif escolha == 3:
        print(" === SAINDO ===")
        break
        
    else:
        print("Opção inválida")



