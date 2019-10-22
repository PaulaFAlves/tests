def count(years):
	c = years * 365
	return c

def count_months(years):
	d = years * 12
	return d

assert count(38) == 13870


assert count_months(38) == 456