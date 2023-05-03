# array
meu_array = [1, 2, 3, 4, 5]

print(meu_array[1]) 

# lista encadeada
class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        
minha_lista = No(1)
minha_lista.proximo = No(2)
minha_lista.proximo.proximo = No(3)
minha_lista.proximo.proximo.proximo = No(4)
minha_lista.proximo.proximo.proximo.proximo = No(5)

# Percorrendo a lista encadeada e imprimindo os valores
no_atual = minha_lista
while no_atual != None:
    print(no_atual.valor)
    no_atual = no_atual.proximo


# Adicionando um elemento ao final do array
meu_array.append(6)
print(meu_array) 

# Adicionando um elemento ao final da lista encadeada
novo_no = No(6)
no_atual = minha_lista
while no_atual.proximo != None:
    no_atual = no_atual.proximo
no_atual.proximo = novo_no

# Percorrendo a lista encadeada e imprimindo os valores
no_atual = minha_lista
while no_atual != None:
    print(no_atual.valor)
    no_atual = no_atual.proximo

# Para inserir um elemento no começo de um array, utilizei o método 'insert()'
# Python, passando o índice 0 como primeiro argumento e o elemento que queremos 
# adicionar como segundo argumento.

meu_array = [1, 2, 3, 4, 5]
meu_array.insert(0, 0)
print(meu_array) 

import timeit

# Calcula do tempo de execução 
tempo = timeit.timeit(stmt='meu_array.insert(0, 999)', globals=globals(), number=1000)

print(f'Tempo de execução: {tempo:.6f} segundos')

tempo2 = timeit.timeit(stmt='novo_no = No(6)\nno_atual = minha_lista\nwhile no_atual.proximo != None:\n    no_atual = no_atual.proximo\nno_atual.proximo = novo_no', globals=globals(), number=1000)

print(f'Tempo de execução: {tempo2:.6f} segundos')




