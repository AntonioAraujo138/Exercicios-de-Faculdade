print('============================================')
print('========== Somar Dois Números ==============')
print('=============================================')


n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

soma = n1 + n2

print('A soma vale: ', soma)
print()

#outra forma de fazer a soma com o format
print('====================================')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

soma = n1 + n2

print('A soma de {} mais {} é igual á {} '.format(n1, n2 , soma))
print()

#sem a função INT não vai ocorrer a soma
n1 = input('Digite um número: ')
n2 = input('Digite outro número: ')
soma = n1 + n2
print('A soma vale: ', soma)
print()

print('Não a soma nessa parte, por não ter a variável (INT) em seu código.')
print()