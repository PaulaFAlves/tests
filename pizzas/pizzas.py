
cadastro = [{'nome': 'Renato', 'Marguerita' : 4, 'Quatro queijos' : 5, 'Escarola' : 4, 'Portuguesa' : 5, 'Frango com Catupiry' : 4, 'Napolitana' : 3 },
 			{'nome': 'Marcelo', 'Marguerita' : 2, 'Quatro queijos' : 2, 'Escarola' : 1, 'Portuguesa' : 3, 'Frango com Catupiry' : 5, 'Napolitana' : 2},
 			{'nome': 'Lenon', 'Marguerita' : 4, 'Quatro queijos' : 5, 'Escarola' : 2, 'Portuguesa' : 1, 'Frango com Catupiry' : 1, 'Napolitana' : 3 },
 			{'nome': 'Renata', 'Marguerita' : 4, 'Quatro queijos' : 5, 'Escarola' : 1, 'Portuguesa' : 1, 'Frango com Catupiry' : 3, 'Napolitana' : 4},
 			{'nome': 'Washington', 'Marguerita' : 1, 'Quatro queijos' : 1, 'Escarola' : 2, 'Portuguesa' : 3, 'Frango com Catupiry' : 4, 'Napolitana' : 3},
 			{'nome': 'Tino', 'Marguerita' : 1, 'Quatro queijos' : 5, 'Escarola' : 1, 'Portuguesa' : 4, 'Frango com Catupiry' : 3, 'Napolitana' : 2 },
 			{'nome': 'Luca', 'Marguerita' : 5, 'Quatro queijos' : 4, 'Escarola' : 3, 'Portuguesa' : 4, 'Frango com Catupiry' : 3, 'Napolitana' : 2 }]  




marguerita = []
quatro_queijos = []
escarola = []
portuguesa = []
frango = []
napolitana = []

n = 0
while n < len(cadastro):
	if (cadastro[n]['Marguerita']) == 5 or (cadastro[n]['Marguerita']) == 4:
		marguerita.append(cadastro[n]['nome'])
	if (cadastro[n]['Quatro queijos']) == 5 or (cadastro[n]['Quatro queijos']) == 4:
		quatro_queijos.append(cadastro[n]['nome'])
	if (cadastro[n]['Escarola']) == 5 or (cadastro[n]['Escarola']) == 4:
		escarola.append(cadastro[n]['nome'])
	if (cadastro[n]['Portuguesa']) == 5 or (cadastro[n]['Portuguesa']) == 4:
		portuguesa.append(cadastro[n]['nome'])
	if (cadastro[n]['Frango com Catupiry']) == 5 or (cadastro[n]['Frango com Catupiry']) == 4:
		frango.append(cadastro[n]['nome'])
	if (cadastro[n]['Napolitana']) == 5 or (cadastro[n]['Napolitana']) == 4:
		napolitana.append(cadastro[n]['nome'])	
	n += 1



print('Quem gosta muito de Marguerita? ', marguerita)
print('Quem gosta muito de Quatro queijos? ', quatro_queijos)
print('Quem gosta muito de Escarola? ', escarola)
print('Quem gosta muito de Portuguesa? ', portuguesa)
print('Quem gosta muito de Frango com Catupiry? ', frango)
print('Quem gosta muito de Napolitana? ', napolitana)



