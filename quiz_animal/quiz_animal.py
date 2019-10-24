# PROCESSAMENTO
cachorro = {'nome':'cachorro', 
					'patas': 4,
					'voa': 'n',
					'pêlos': 's',
					'nada': 'n'}

galinha = {'nome':'galinha', 
					'patas': 2,
					'voa': 's',
					'pêlos': 'n',
					'nada': 'n'}

baleia = {'nome':'baleia', 
					'patas': 0,
					'voa': 'n',
					'pêlos': 'n',
					'nada': 's'}

passaro = {'nome':'passaro', 
					'patas': 2,
					'voa': 's',
					'pêlos': 'n',
					'nada': 'n'}



# INPUT


respostas = []
respostas.append(input('Quiz animal!\nQuantas patas ele tem? '))
respostas.append(input('Esse animal voa? (s/n)'))
respostas.append(input('Esse animal tem pelos? (s/n)'))
respostas.append(input('Esse animal nada? (s/n)'))


# OUTPUT 

print(respostas)

if respostas[0] == '4':
	if respostas[1] == 'n':
		if respostas[2] == 's':
			if respostas[3] == 'n':
				print('É um cachorro!')
elif respostas[0] == '2':
	if respostas[1] == 's':
		if respostas[2] == 'n':
			if respostas[3] == 'n':
				print('É uma galinha!')
		else:
			print('É um pássaro!')
else:
	print('É uma baleia')



