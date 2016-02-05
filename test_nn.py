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
	
		d1_1 = [7, 1, 1]
		d2_2 = [7, 2, 1]
		d3_3 = [8, 1, 1]
		d4_4 = [8, 2, 1]
		
		label_0_data = [d1_0, d2_0, d3_0, d4_0]
		label_1_data = [d1_1, d2_2, d3_3, d4_4]
		
		
		#print weights[0][0][0], weights[0][1][0], weights[0][0][1], weights[0][1][1]
		#print biases[1][0], biases[1][1]
		#[[[], []], [[], []]]
		
		
		labelled_data = label_0_data + label_1_data
		layers = get_layers(num=2)
		num_inputs = len(labelled_data[0][:-1])
		num_outputs=2
		weights, biases = get_default_weights_biases(layers, num_inputs=num_inputs, num_outputs=num_outputs)
		avg_error = get_error(labelled_data, weights, biases)
		print avg_error
		
			
if __name__ == '__main__':
    unittest.main()