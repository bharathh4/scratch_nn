import unittest
import sys
import os

from nn import *

class TestUtilities(unittest.TestCase):

	
	def test_label2vector(self):
		num_label = 2
		num_classes = 3
		self.assertEqual(label2vector(num_label, num_classes), [0, 0, 1])
		
	def test2_label2vector(self):
		num_label = 2
		num_classes = 3
		self.assertEqual(label2vector(num_label, num_classes), [0, 0, 1])

	def main(self):
		d1_0 = [1, 1, 0]
		d2_0 = [1, 2, 0]
		d3_0 = [2, 1, 0]
		d4_0 = [2, 2, 0]
	
		d1_1 = [1, 1, 1]
		d2_2 = [1, 2, 1]
		d3_3 = [2, 1, 1]
		d4_4 = [2, 2, 1]
		
		lb0_data = [d1_0, d2_0, d3_0, d4_0]
		lb1_data = [d1_1, d2_2, d3_3, d4_4]
		
		for data in lb0_data:
			print 'The label is %s' % data[-1]
			
		for data in lb1_data:
			print 'The label is %s' % data[-1]
	
	
if __name__ == '__main__':
    unittest.main()