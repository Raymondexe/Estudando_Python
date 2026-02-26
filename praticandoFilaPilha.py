
print(" === Praticando  Fila === ")

escolha = int(input("Qual exercício quer ver? \n1 - Fila \n2 - Pilha \n3 - Fechar "))

while True:

    if escolha == 1:
        class Queue:
            def __init__ (self):
                self.items = []
            
            def isEmpty(self):
                return self.items == []
            
            def enqueue (self, items):
                self.items.insert(0,items)
            
            def dequeue(self):
                return self.items.pop()

            def size(self):
                return len(self.items)
            
        q = Queue()
        q.enqueue(4)
        q.enqueue('dog')
        q.enqueue(True)
        print("\nDeu certo:", q.size())
        break

    elif escolha == 2:
        print("\n === Praticando Pilha === \n")

        class Stack:
            def __init__ (self):
                self.items = []

            def isEmpty(self):
                return self.items == []
            

            def push (self, item):
                self.items.append(item)
            
            def pop(self):
                return self.items.pop()
            
            def size(self):
                return len(self.items)

            def peek(self):
                return self.items[len(self.items)-1]

        s=Stack()
        print(s.isEmpty())
        s.push(4)
        s.push('dog')
        print(s.peek())
        s.push(True)
        print(s.size())
        print(s.isEmpty())
        s.push(8.4)
        print(s.pop())
        print(s.pop())
        print(s.size())
        break
    
    elif escolha == 3:
        print(" === Saindo ===")
        break
        
    else:
        print("Opção inválida.")
        break


