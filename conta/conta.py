class Conta():

	def __init__(self, numero, titular, saldo, limite):
		self.numero = numero
		self.titular = titular
		self.saldo = saldo
		self.limite = limite

	def cria_conta(self):
		conta = {
				numero : self.numero,
				titular: self.titular,
				saldo : self.saldo,
				limite : self.limite
		}
		return conta
	
	def deposita(self, valor):
		self.saldo += valor
	
	def saca(self, valor):
		self.saldo -= valor
	
	def __repr__(self):
		return 'numero: {} \nnome: {} \nsaldo: {}'.format(self.numero, self.titular, self.saldo)
	

if __name__ == "__main__":
	import doctest
	doctest.testmod()





	
		









































