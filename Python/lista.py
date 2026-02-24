# Exercício FATEC ZL - Manipulação de dados
    # Variáveis com letras aleatórias apenas para estudos. 

# === Lista ===

L = []
print(type (L))
L = [10, 15, 20, 25, 30] # Lista com 5 elementos
print(L) # Print lista
print(L[2]) # Print do segundo elemento da lista (começa em 0 (10))
print(len(L)) # Tamanho da lista

print("\n-----------------\n")


# Fatiamento
print("Fatiamento")
A = [1, 3, 5, 9, 11, 13, 15, 17, 19, 21, 23] 
print (A [0:3]) # 0 ~ 3 (Posição Inicial : Posição Final)
print (A [4:10]) # 4 ~ 9
print (A [:5]) # 0 ~ 5 (x : Posição Final)
print (A [5:]) # > 5 ( Posição Inicial : Vazio)
print (A [0:8:3]) #( Posição Incia: Final : Salto)
print (A [::4]) # (Vazio : Vazio: Salto)

print("\n-----------------\n")

print("Multiplicador de elemtento")
B = [3,7] * 3 # Pega o valor da array e repete X vezes
print (B)
V = [5] * 10
print (V)

print("\n-----------------\n")

print("Separador")
S = "Text"
L = list(S)
print (L) # Separou o texto por cada letra para a array

print("\n-----------------\n")

print("Split")
B = "5 7 8 8.8 12" # Separou o texto 
U = B.split()
print (U)
 
J = "5;7;8.8;12"
I = J.split(";") # Separou o conteúdo do texto da variável para uma lista
print (I)

print("\n-----------------\n")

print("=== IN/NOT IN === ")
L = [3, 6, 9] 
print (9 in L)
print (5 in L)
print (5 not in L) # Bolean
    # O operador IN permite 
    # verificar se um valor está presente em uma lista
    
print("\n-----------------\n")

print("=== Verificação IN/NOT IN ===")
Caes = ["Labrador" , "Poodle" , "Terrier"]
a = "Lassie"
if a in Caes:
    print ("Boa escolha")
else:
    print ("Não temos essa raça")
# Verifica se há a raça "Lassie", caso haja exibirá "Boa escolha", mas como não há exibirá "Não temos essa raça"


print("\n-----------------\n")
print("=== Insert + Append + Count + Index + Loop + Pop + Remove ===")
L = [3, 6, 9]
print (L)
 
L.insert(2, 15) # Adiciona um valor: Posição, Numero ADD
print (L)
 
L.append(6) # Adiciona um valor novo para a lista, joga para o final
print (L)

L.count(6) # Conta quantas vezes o valor aparece na lista
L.index(9) # Retorna a posição do vetor
L.pop(3)  # Remove o valor naquela posição
print (L)
 

L.remove(6) #  Remove o valor específico (6). 
print (L)


print("\n-----------------\n")
print(" === Extend + Reverse + Sort + Clear === ")
A = [22, 32, 42] # Concatena à lista L os dados de A
L.extend(A)
print (L)
 
L.reverse() #Inverso da lista L
print (L)
 
L.sort() # inverte na forma crescente
print (L)
 
L.sort(reverse=True) # Inverte na forma decrescente
print (L)
 
L.clear() #Limpa