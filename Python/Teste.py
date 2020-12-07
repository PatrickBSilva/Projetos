print ('Olá! O Programa foi executado com sucesso.')
print ('')
while True:
    print ('Digite: 1 para efetuar uma venda.')
    print ('Digite: 2 para cadastrar um novo cliente.')
    print ('Digite: 3 para verificar as vendas de um cliente.')
    decisao = int(input('Qual opção deseja? '))

    if decisao == 1:
        #print (lista de clientes)
        cliente = input('Qual o código ou nome do cliente? ')
        while True:
            #print (lista de produtos + 'outros')
            objeto = input('Qual o produto a ser vendido? ')
            preço = float(input('Qual o valor do kg? '))
            peso = float(input('Qual o peso do produto em kilogramas? '))
            valortotal = preço*peso
            print ('Produto: {}, Valor do kg: {} R$, Peso: {} kg, Valor total: {:.2f} R$'.format(objeto,preço,peso,valortotal))
            confirmar = input('Está tudo certo? Para confirmar a venda, digite SIM, para voltar ao início, digite NÃO. : ')
            if confirmar == 'SIM' or confirmar == 'sim':
                #lista do cliente.append
                print ('O valor total é de {:.2f}. A venda foi guardada na aba do cliente.'.format(valortotal))
            else:
                break
            repetir = int(input('Deseja efetuar outra venda? Digite 1 para repetir. Digite 2 para voltar ao início. '))
            if repetir == 2:
                break