funcionario1 = {
    'nome': 'Maria'
    ,'sobrenome': 'Souza'
    ,'idade': 19
    ,'salario': 1950.99
    ,'ativo': True
}
funcionario2 = {
    'nome': 'Joao'
    ,'sobrenome': 'Silva'
    ,'idade': 81
    ,'salario': 18950.99
    ,'ativo': False
}

funcionarios = [funcionario1, funcionario2]

for f in funcionarios:
    print(f['nome'])