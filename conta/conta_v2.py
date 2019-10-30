
def saldo():
	saldo = 100
	return saldo

def deposita(x):
	s = saldo()
	return s + x

def saca(x):
	s = saldo()
	return s - x

assert deposita(20) == 120
assert deposita(30) == 130
assert deposita(50) == 150

assert saca(20) == 80
assert saca(50) == 50
assert saca(100) == 0