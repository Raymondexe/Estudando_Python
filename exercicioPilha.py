class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, tarefa):
        self.items.append(tarefa)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return "Não há tarefas na pilha."


pilha = Stack()

while True:
    escolha = int(input(
        "\nO que deseja fazer?\n"
        "1 - Inserir tarefa\n"
        "2 - Obter próxima tarefa\n"
        "3 - Sair\n"
        "Escolha: "
    ))

    if escolha == 1:
        tarefa = input("Digite a tarefa: ")
        pilha.push(tarefa)
        print("Tarefa adicionada!")

    elif escolha == 2:
        print("Próxima tarefa:", pilha.pop())

    elif escolha == 3:
        print(" === Saindo === ")
        break

    else:
        print("Opção inválida.")