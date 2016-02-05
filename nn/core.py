

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
	

if __name__ == '__main__':
	
	pass
	
	
	