"""
Given a number of companies and a number of months,

With the following information:
	- Number of companies
	- Number of months
	- Finantial results in each month

Calculate the total finantial result in the period, for each company,
and say if it has achieved profit, loss or the result was indiferent.

Make sure the number of month that was informed by the user is valid.

"""

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
		msg = 'Indiferent'
	elif result > 0:
		msg = 'Profit'
	elif result < 0:
		msg = 'Loss'
	return msg


number_of_companies()	


assert financial_results(0) == 'Indiferent'
assert financial_results(100) == 'Profit'
assert financial_results(-100) == 'Loss'

assert number_of_months(13) == 'Invalid number'
assert number_of_months(-3) == 'Invalid number'
assert number_of_months(12) == 12



