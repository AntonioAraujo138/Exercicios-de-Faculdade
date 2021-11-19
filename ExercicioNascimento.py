#Ano de nascimento de 5 Pessoas


ano_atu = 2021
conta = 0
for c in range(1, 6):
    ano_nasc = int(input('Digite o seu Ano de Nascimento? '))
    idade = ano_atu - ano_nasc
    print(f'Você tem {idade} anos.')
    if idade >= 60:
        conta = conta + 1
        print(f'Você ja esta idoso.')
    else:
        print(f'Você é jovem.')

print(f'O total de idosos é {conta}.')
