def define_valor():
	while True:
		a = int(input('Digite um numero: '))
		b = int(input('Digite outro numero: '))
		print_result(mdc(a, b))
		r = input('Deseja continuar? (S/N) ')
		if r in 'Nn':
			break
	return a, b



def mdc(a, b):
	rest = None
	while rest is not 0:
		rest = a % b
		a = b
		b = rest

	return a


def print_result(a):
	print('O MDC entre é', a)


define_valor()


assert mdc(30,75) == 15
assert mdc(5, 20) == 5
assert mdc(90, 130) == 10
assert mdc(-20, 20) == 20