def label2vector(num_label, num_classes):
	zeros_list = [0 for _ in range(num_classes)]
	zeros_list[num_label] = 1
	return zeros_list
	
def multiply(weights, biases, inputs):
	