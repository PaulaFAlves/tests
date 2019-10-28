def saque(valor):
	valor_total = valor
	notas = [100, 50, 10, 5, 1]
	qtds = []

	for nota in notas:
		qtd = valor // nota
		valor -= nota * qtd
		qtds.append(qtd)

	qtds = reversed(qtds)

	print_notas(valor_total, *qtds)

def print_notas(total, notas1, notas5, notas10, notas50, notas100):

	template = 'R$ {:.>10}: {:>1} notas.'
	print('Valor do saque: R$', str(total))

	if notas100 != 0:
		print(template.format('100', notas100))
	if notas50 != 0:
		print(template.format('50', notas50))
	if notas10 != 0:
		print(template.format('10', notas10))
	if notas5 != 0:
		print(template.format('5', notas5))
	if notas1 != 0:
		print(template.format('1', notas1))
  
   

valor = int(input('Quanto deseja sacar? '))
reposta = saque(valor)



if __name__ == "__main__":
	import doctest
	doctest.testmod()