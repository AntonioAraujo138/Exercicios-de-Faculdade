print('Crescente de 1 a 10')
for c in range(1,11):
    #código
    print(c)
print(30*'*')

print('\n Descrevente de 10 a 1')
for c in range(10, 0, -1):  #[10,9,8,7,6,5,4,3,2,1]
    print(c)
print(30*'*')

print('\n Números Pares')
for c in range(0,11,2): #[0,2,4,6,8,10]
    print(c)
print(30*'*')

print('\n Números PARES inverso')
for c in range(10, -1, -2): #[10,8,6,4,2,0]
    print(c)
print(30*'*')

print('\n Interando em Strings')
nome = 'Antonio'
for c in nome:
    print(c)
print(30*'*')

print('\n Lista Nomes de Alunos')
lista_aulos = ['João', 'Maria', 'José', 'Antonio', 'Fulano']
for c in lista_aulos:
    print(c)
print(30*'*')

print('\n Printando um range()')
print(range(1,11))
print([1,2,3,4,5,6,7,8,9,10])
print(30*'*')

print('\n Exemplo de range com len()')
lista = ['Escova de dentes', 'Sabonete', 'Detergente', 'Arroz', 'Feijão', 'Óleo']
for c in range(0, len(lista)): # [0,1,2,3,4...]
    print('Indice', c)

for c in lista:
    print('Produtos: ',c)