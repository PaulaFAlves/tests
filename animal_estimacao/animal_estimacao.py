class AnimalEstimacao():
	def __init__(self, nome, especie, dono):
		self.nome = nome
		self.especie = especie
		self.dono = dono

	def __repr__(self):
		return str(self.nome) + ',' + str(self.especie) + ',' + str(self.dono)

	def correr(self):
		print('{0} está correndo.'.format(self.nome))	

	def brincar(self):
		print('{0} está brincanco.'.format(self.nome))

	def comer(self):
		print('{0} está comendo.'.format(self.nome))


class PeixeEstimacao(AnimalEstimacao):
	def __init__(self, nome, dono):
		super().__init__(nome, 'peixe', dono)

	def nadar(self):
		print('{0} está nadando.'.format(self.nome))

class PassaroEstimacao(AnimalEstimacao):
	def __init__(self, nome, dono):
		super().__init__(nome, 'pássaro', dono)

	def voa(self):
		print('{0} está voando.'.format(self.nome))
