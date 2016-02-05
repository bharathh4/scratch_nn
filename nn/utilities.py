from math import *

def label2vector(num_label, num_classes):
	zeros_list = [0 for _ in range(num_classes)]
	zeros_list[num_label] = 1
	return zeros_list
	
def get_labels(labelled_data):
	return [labelled_datum[-1] for labelled_datum in labelled_data]
	
def get_data(labelled_data):
	return [labelled_data[:-1] for labelled_data in labelled_data]
	
def multiply(weights, biases, inputs, outputs):
	y = []
	for ouput_index, output in enumerate(outputs):
		temp = []
		for input_index, input in enumerate(inputs):
			#print weights[0][input_index][ouput_index] * input + biases[1][ouput_index]
			temp.append(weights[0][input_index][ouput_index] * input)
		y.append(sum(temp) + biases[1][ouput_index])
	return y
	
def get_softmax(outputs):
	alist = [exp(output) for output in outputs]
	total = float(sum(alist))
	return [num/total for num in alist]
	
def compute_cross_entropy(computed_outputs, actual_outputs):
	return -sum([computed_output * log(actual_output) for computed_output, actual_output in zip(computed_outputs, actual_outputs)])