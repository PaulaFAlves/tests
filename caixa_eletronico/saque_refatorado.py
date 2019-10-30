
notas = [100, 50, 20, 10, 2]
menor_nota = notas[-1]


def valor_desejado():
	# solicita o valor a ser sacado:
	# testa se valor < 10, invalido, pede para digitar novamente
	while True:
		valor = int(input('Valor do saque: '))
		if valor < menor_nota:
			print(f'Valor invalido! Saque mínimo: R${menor_nota}')
		elif valor % menor_nota != 0:
			print(f'Valor invalido! Somente notas de {notas}')
		else:
			break
	return valor


def saque(valor):
	d = {}
	for valor_nota in notas:
		qtd_notas = valor // valor_nota
	
		if qtd_notas != 0:
			valor -= qtd_notas * valor_nota
			d[valor_nota] = qtd_notas

	return d

def relatorio(notas_sacadas):
	print('SAQUE AUTORIZADO.')
	for valor, qtd in notas_sacadas.items():
		print(f'>> {qtd} notas de R${valor}.00')	


relatorio(saque(valor_desejado()))


# testes 
# assert q_100(10) == 0
# assert q_100(20) == 0
# assert q_100(50) == 0
# assert q_100(100) == 1

# assert q_50(10) == 0
# assert q_50(20) == 0
# assert q_50(50) == 1
# assert q_50(100) == 2

# assert q_20(10) == 0
# assert q_20(20) == 1
# assert q_20(50) == 2
# assert q_20(100) == 5

# assert q_10(10) == 1
# assert q_10(20) == 2
# assert q_10(50) == 5
# assert q_10(100) == 10