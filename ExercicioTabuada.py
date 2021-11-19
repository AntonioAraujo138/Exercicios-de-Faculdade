#Tabuada de núm informado pelo usuário


num = int(input('Você quer fazer a tabuado de qual número (0 a 9)? '))

for c in range (0, 11):
    print(f'{num} x {c} = {c * num} ')