####dados = dict()
#dados['nome'] = str(input('Nome'))
#dados['RG'] = int(input('Registro Geral'))
#dados['CPF/CNPJ'] = int(input('CPF/CNPJ'))
#dados['telefone'] = int(input('Telefone'))
#print(dados)

listas= [[]]
while True:
    print ('Digite: 1 para Cadastrar pessoa.')
    print ('Digite: 2 para Lista de Cadastro.')
    print ('Digite: 3 para Procurar Pessoa Específica.')
    decisao = int(input('Qual opção deseja? '))
    if decisao == 1:
        usuarios = []
        nome = input('Digite o Nome')
        RG = input('Digite o RG')
        CPFCNPJ = input('Digite CPF/CNPJ')
        telefone = input('Digite Telefone')
        usuarios.append(nome)
        usuarios.append(RG)
        usuarios.append(CPFCNPJ)
        usuarios.append(telefone)
        listas.append(usuarios)
    elif decisao == 2:
        for mostrar in listas:
            try:
                print("Nome: %s - Idade: %s - ID: %s"%(mostrar[1],mostrar[2],mostrar[0]))
            except:
                print("Essa pessoa não possui algum dos valores a seguir: Nome, Idade, ID")

id = input("Digite o id da pessoa desejada: ")
for mostrar in listas:
    if id in mostrar:
        try:
            print("Nome: %s - Idade: %s - ID: %s"%(mostrar[1],mostrar[2],mostrar[0]))
        except:
            print("Essa pessoa não possui algum dos valores a seguir: Nome, Idade, ID")
