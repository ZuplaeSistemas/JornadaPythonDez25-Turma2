nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

print(f'Ola, {nome}')

# se a pessoa for maior de idade, tem acesso
# se for menor de idade, nao tem acesso

#estrutura de decisao - if-else
if idade >= 18: # maior ou igual >=
    print('Parabens, voce tem acesso ao sistema')
else:
    print('Acesso negado!')