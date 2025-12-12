from calculos import soma,subtracao, multiplicacao, divisao
from ftela import cabecalho_rodape

cabecalho_rodape('Calculadora', 30)

numero1 = float(input('Digite o primeiro numero: '))
numero2 = float(input('Digite o segundo numero: '))

soma(numero1, numero2) #argumentos numero1 e numero2
subtracao(numero1, numero2)
multiplicacao(numero1, numero2)
divisao(numero1, numero2)

cabecalho_rodape('Fim programa', 30)