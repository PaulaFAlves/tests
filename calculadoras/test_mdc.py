import unittest

class Test_mdc(unittest.TestCase):
	def test_with_30_and_45(self):
		result = mdc.calc_mdc(30, 45)
		expected = 15
		self. assertEqual(expected, result)

	def test_with_5_and_20(self):
		result = mdc.calc_mdc(5, 20)
		expected = 5
		self.assertEqual(expected, result)

	def test_with_90_and_130(self):
		result = mdc.calc_mdc(90, 130)
		expected = 10
		self.assertEqual(expected, result)

	def test_with_minus20_and_20(self):
		result = mdc.calc_mdc(-20, 20)
		expected = 20
		self.assertEqual(expected, result)



