def salvar_nome(nome):
    with open('aula008/arquivo.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'{nome}\n')

def ler_nomes():
    nomes = []
    with open('aula008/arquivo.txt', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if linha != '':
                nomes.append(linha)
    return nomes
