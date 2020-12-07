def exibir_menu():
    print('''Escolha uma opção:

    1. Cadastrar uma pessoa
    2. Listar pessoas cadastradas
    3. Procurar dados de uma pessoa
    ''')
def cadastrar(pessoas):
    nome = input('Digite o Nome ')
    CPFCNPJ = input('Digite CPF/CNPJ ')
    RG = int(input('Digite o RG '))
    telefone = int(input('Digite Telefone'))
    pessoas.append((nome, CPFCNPJ, RG, telefone))
def listar(pessoas):
    for pessoa in pessoas:
        nome, CPFCNPJ, RG, telefone = pessoa
        print(f'Nome: {nome}, CPF/CNPJ: {CPFCNPJ}, RG: {RG}, telefone: {telefone}')
def buscar(pessoas):
    nome_desejado = input('Nome ou CPF/CNPJ ')
    for pessoa in pessoas:
        nome, CPFCNPJ, RG, telefone = pessoa
        if nome or CPFCNPJ == nome_desejado:
            print(f'Nome: {nome}, CPF/CNPJ: {CPFCNPJ}, RG: {RG}, telefone: {telefone}')
            break
    else:
        print(f'Pessoa com nome ou CPF/CNPJ {nome_desejado} não encontrada')
def main():
    pessoas = []

    while True:
        exibir_menu()
        opcao = int(input('Opção? '))
        if opcao == 1:
            cadastrar(pessoas)
        elif opcao == 2:
            listar(pessoas)
        elif opcao == 3:
            buscar(pessoas)
        else:
            print('Opção inválida')
main()