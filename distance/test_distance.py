import unittest
from distance import calc_distance

class DistanceTest(unittest.TestCase):
	def test_if_1_1_1_2(self):
		self.assertEqual(calc_distance(1,1,2,2), 1.4142)

	def test_if_2_2_4_4(self):
		self.assertEqual(calc_distance(2,2,4,4), 2.8284)