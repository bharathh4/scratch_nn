from nn.utilities import *

def get_layers(num=2):
	return [[] for _ in range(num)] 
	
def get_default_weights_biases(layers, num_inputs=2, num_outputs=2):
	weights, biases = [], []
	for layer in layers:
		w= [[1 for _ in range(num_outputs)] for _ in range(num_inputs)]
		weights.append(w)
		
	for layer in layers:
		b = [1 for _ in range(num_outputs)]
		biases.append(b)
	return weights, biases
	
def get_error(labelled_data, weights, biases):

	num_outputs = len(biases[0])
	outputs = [0 for _ in range(num_outputs)]

	errors = []
	for item in labelled_data:
		features, label = item[:-1], item[-1]
		softmax_output = get_softmax(multiply(weights, biases, features, outputs))
		num_classes = 2
		needed_output = label2vector(label, num_classes)
		errors.append(compute_cross_entropy(needed_output, softmax_output))
	total_error = sum(errors)
	avg_error = total_error/len(errors)
	return avg_error
	

if __name__ == '__main__':
	pass