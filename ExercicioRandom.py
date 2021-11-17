
import random
num = random.randint(0,10)
print (f'Número aleatório {num}')   #Aqui o num Random do PC

qtde = 0
palpite = 0

while palpite != num:
    palpite = int(input('Digite seu palpite (0..10): '))
    qtde = qtde + 1
print(f'O número era {num}, você deu {qtde} palpites.')
print('----- FIM do Programa -----')
print()