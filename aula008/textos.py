from arquivo_texto import salvar_nome, ler_nomes


nome = input('Digite o seu nome: ')
salvar_nome(nome)

nomes = ler_nomes()

for n in nomes:
    print('Nome: ', n)