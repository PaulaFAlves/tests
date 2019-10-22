import unittest
from count_days import count, count_months

class CountTests(unittest.TestCase):
	def test_when_38_in_days(self):
		self.assertEqual(count(38), 13870)

	def test_when_12_in_days(self):
		self.assertEqual(count(12), 4380)

	def test_when_5_in_days(self):
		self.assertEqual(count(5), 1825)

	def test_when_38_in_months(self):
		self.assertEqual(count_months(38), 456)

	def test_when_12_in_months(self):
		self.assertEqual(count_months(12), 144)

	def test_when_5_in_months(self):
		self.assertEqual(count_months(5), 60)



"""
		if __name__ == '__main__':
	assert count(38) == 13870
	assert count(12) == 4380
	assert count(5) == 1825
	
	
	assert count_months(38) == 456
	assert count_months(12) == 144
	assert count_months(5) == 60
"""