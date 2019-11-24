from random import randint

def getnumber():
	answer = input('Would you like to digit a number (digit 1) or randomly generate a number (digit 2)? ')
	if answer == '2':
		n = randint(0, 100)
		squares(n)
	elif answer == '1' :
		n = int(input('Digit a number: '))
		squares(n)
	else:
		print('Invalid option.')


def squares(n):
	result = n * n
	return result

assert squares(-1) == 1
assert squares(0) == 0
assert squares(4) == 16
assert squares(10) == 100
assert squares(25) == 625
assert squares(100) == 10000