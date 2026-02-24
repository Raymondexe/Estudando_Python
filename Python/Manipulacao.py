# 🐍 -  Manipulação de String

# Plus

texto = "sorvete de chocolate"
print(texto.upper())  # SORVETE DE CHOCOLATE (All maiúsculo )
print(texto.lower())  # sorvete de chocolate (All min)
print(texto.title())  # Sorvete De Chocolate (Primeira letra em maiúsculo)

print("-----------------")

## Procurando texto

frase = "Eu gosto de Python"
print("Python" in frase)  # True (Há a palavra "Python")
print("Python" not in frase) # False (NÃO há a palavra "Python")
print("Java" in frase)  # False (Não há a palavra "Java")


print("-----------------")

## Substituição de palavra

fraseSub = "Eu gosto de Java" # Frase inicial
nova = fraseSub.replace("Java", "Python") # Frase modificada, foi substituida a palavra "Java" por "Python"
print(nova) # Print (nova frase substituida)