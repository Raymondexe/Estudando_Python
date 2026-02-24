# Exercício 01
# Insira o seu nome, exiba o nome em maiúsculo, minúsculo e qtd de letras
print("1 = Formatação de nome, \n2 - Inversor de palavra, \n3 - Contador de vogais, \n4 - Lista de Compras ")
opcao = int(input("Digite uma opção: "))

match opcao:
    case 1:
        print(" === Desafio 1 - Formatação de nome === ")
        nomeUser = input("Insira o seu nome: ")
        print("Seu nome em maiúsculo:", nomeUser.upper())
        print("Seu nome em minúsculo:",nomeUser.lower())
        print("O número de letras do seu nome é:", len(nomeUser))
        print("\n-----------------\n")

    case 2:
        print(" === Desafio 2 - Inversor de palavra")
        texto = input("Digite uma palavra: ")
        print("Invertido:", texto[::-1])
        print("\n-----------------\n")
        
    case 3:
        print(" === Desafio 3 — Contador de vogais === ")
        frase = input("Insira uma frase: ")
        contador = 0
        vogais = ["a", "e", "i", "o", "u"]
        for text in frase.lower():
            if text in vogais:
                contador += 1
                print("O número de vogais é:", contador)
                
                
    case 4:
        print(" === Desafio 4 — Lista de compras inteligente == ")

        listaCompra = []

        for i in range(5):
            item = input("Insira um item da lista: ")
            listaCompra.append(item)

        print("Itens na lista de compra:", listaCompra)
        print("Quantidade de itens:", len(listaCompra))
        listaCompra.sort()
        print("Itens em ordem alfabética:", listaCompra)
            
        
        
        