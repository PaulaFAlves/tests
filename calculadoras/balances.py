import time


def number_of_companies():
	companies = int(input('Digit the number of companies: '))
	
	while True:
		months = int(input('Digit number of months: '))
		if number_of_months(months) == 'Invalid number':
			print('Number of month invalid. Try again.')
		else:
			break

	total = 0
	count = 1
	while count <= companies:
		print('**** Company: {}'.format(count))
		calculate_result(months)
		count += 1


def number_of_months(months):
	if months > 12 or months <= 0:
		return 'Invalid number'
	else:
		return months


def calculate_result(n):
	months = int(n)
	total = 0 
	count = 1
	while count <= months:
		partial = int(input('Month: {} \nResult: '.format(count)))
		total += partial
		count += 1
	print('**** Total: R$', total , ' >>> ', financial_results(total))
	time.sleep(1)


def financial_results(n):
	result = n
	msg = str
	if result == 0:
		msg = 'Indiferente'
	elif result > 0:
		msg = 'Lucro'
	elif result < 0:
		msg = 'Prejuízo'
	return msg


number_of_companies()	


assert financial_results(0) == 'Indiferente'
assert financial_results(100) == 'Lucro'
assert financial_results(-100) == 'Prejuízo'

assert number_of_months(13) == 'Invalid number'
assert number_of_months(-3) == 'Invalid number'
assert number_of_months(12) == 12



