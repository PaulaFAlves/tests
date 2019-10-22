def calc_distance(x1, y1, x2, y2):
	d = ((x2 - x1) ** 2 + (y2 - y1 ) ** 2) ** (1/2)
	return round(d,4)