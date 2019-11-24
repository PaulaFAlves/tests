from random import randint

def n_random():
	"""Calculate factorial of a random number"""
	n = randint(0, 10)
	option1 = fatorial_option1(n)
	option2 = fatorial_option2(n)
	return option1, option2


def fatorial_option1(n):
	"""Calculate fatorial from n to 1"""
	if n == 0:
		result = 1
	else:
		result = n
		count = n -1
		while count > 1:
			result = result*count
			count -= 1
	return result

def fatorial_option2(n):
	"""Calculate fatorial from 1 to n"""
	if n == 0:
		result = 1
	else:
		result = 1
		count = 1
		while count <= n:
			result = result*count
			count += 1
	return result

print(n_random())


# tests

assert fatorial_option1(0) == 1
assert fatorial_option1(2) == 2
assert fatorial_option1(3) == 6
assert fatorial_option1(4) == 24

assert fatorial_option2(0) == 1
assert fatorial_option2(2) == 2
assert fatorial_option2(3) == 6
assert fatorial_option2(4) == 24




