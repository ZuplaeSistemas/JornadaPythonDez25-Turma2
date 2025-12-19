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

print(funcionario1)
print(funcionario1['idade'])

funcionario1['nome'] = 'Marcos'
print(funcionario1)

del funcionario1['ativo']
print(funcionario1)

funcionario1['endereco'] = 'Rua A, n10'
print(funcionario1)
