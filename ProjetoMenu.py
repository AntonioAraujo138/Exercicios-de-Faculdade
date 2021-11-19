def menu():
    print(5*'*', 'MENU', 5*'*' )
    print(5*'-', '[1] Cadastrar Produto', 5*'-')
    print(5*'-', '[2] Cadastrar Cliente', 5*'-')
    print(5*'-', '[3] Realizar Venda', 5*'-')
    print(5*'-', '[4] Estoque de Produto', 5*'-')
    print(5*'-', '[5] Sair', 5*'-' )
   

list_produto = []
list_cliente = []



def produto():
    while True:
        list_produto.append(input('Nome do Pruduto: '))
        list_produto.append(int(input('Quantidade: ')))
        volta = str(input('Voltar ao Menu [S/N]: '))
        if volta in 'Ss':
            break

def cliente():
    while True:
        list_cliente.append(input('Nome do Cliente: '))
        list_cliente.append(int(input('Telefone: ')))
        volta = str(input('Voltar ao Menu [S/N]: '))
        if volta in 'Ss':
            break

   
    

menu()
#executo oque ele quer fazer
op1 = input('Digite a opção: ')
produto()



menu()
op2 = input('Digite a opção: ')
print(list_produto)