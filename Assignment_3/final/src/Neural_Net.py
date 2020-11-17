import numpy as np
import pandas as pd
import math

def sigmoid(x):
  return [1 / (1 + math.exp(-ele)) for ele in x ]
  
def gradient_sigmoid(z, A, y):
    grad = (z-y)*A
    return grad

def gradient_tanh(z, y, w, A, i):
    w = np.array((z-y) * w)
    A_square = 1 - np.square(A)
    A_square = A_square.reshape(np.shape(A)[0],1)
    A = w * A_square    
    grad = A*i
    return grad

class layer():
    def __init__(self, input_units, output_units, alpha = 0.00001, activation = 'tanh'):
        
        self.input_units = input_units
        self.output_units = output_units
        self.activation = activation
        self.weights = np.random.normal(loc=0.0, 
                                        scale = np.sqrt(2/(input_units+output_units)), 
                                        size = (input_units,output_units))
        self.input = np.zeros(output_units)
        self.activated_output = np.zeros(output_units)
        self.forward_units = np.zeros(output_units)
        
        # adam optimiser : parameters
        self.alpha = alpha
        self.t = 0
        self.m = 0
        self.v = 0
        self.beta_1 = 0.9
        self.beta_2 = 0.99
        self.epsilon = 1e-8
        
    def forward_prop(self, inputs):

        forward_units = np.dot(inputs, self.weights)

        self.input = inputs.reshape(self.input_units)
        
        if self.activation == 'tanh':
            self.activated_output = np.tanh(forward_units)
            
        elif self.activation == 'relu':
            self.activated_output = np.maximum(0, forward_units)
            
        elif self.activation == 'logistic':
            self.activated_output = sigmoid(forward_units)
            
        elif self.activation == 'identity':
            self.activated_output = forward_units
        
        return self.activated_output
    
    def update_weights(self, grad):

        # adam optimiser
        grad = grad.reshape(self.weights.shape)
        self.m = self.beta_1*self.m + grad*(1-self.beta_1)
        self.v = self.beta_2*self.v + np.square(grad)*(1-self.beta_2)
        self.t += 1
        
        m_hat = self.m/(1 - pow(self.beta_1, self.t))
        v_hat = self.v/(1 - pow(self.beta_2, self.t))
        tmp = self.alpha*(m_hat/(np.sqrt(v_hat) + self.epsilon))
                          
		# updating the weights
        self.weights = self.weights - tmp          
    
    def loss_function(self, target):

		# loss function : binary cross entropy
        return [-(target*math.log(ele) + (1-target)*math.log(1-ele)) for ele in self.activated_output]
  
class Neural_Network:

	def __init__(self, size, activation):
		self.num_iters = 40000
		self.network = []
		self.layers = len(size)

		# creating the network 
		for i in range(self.layers-1):
			self.network.append(layer(size[i], size[i+1], activation = activation[i]))

	# X and Y are dataframes
	def fit(self,X,Y):
		# Function that trains the neural network by taking x_train and y_train samples as input
		for i in range(self.num_iters):

			for ind, inputs in enumerate(X):
				outputs = Y[ind]

				# forward propagation of inputs through all the layers
				for layer in self.network:
					inputs = layer.forward_prop(inputs)

				prediction = inputs  
				
				output_layer = self.network[1]
				hidden_layer = self.network[0]

				# backpropagation - updating the weights
				grad = gradient_tanh(prediction, outputs, output_layer.weights, hidden_layer.activated_output, X_train[ind])
				hidden_layer.update_weights(grad) 
				
				grad = gradient_sigmoid(prediction, output_layer.input, outputs)    
				output_layer.update_weights(grad) 
	
	def predict(self,X):
		# The predict function performs a simple feed forward of weights
		# and outputs yhat values 

		# yhat is a list of the predicted value for df X
		yhat = []
		for ind, inputs in enumerate(X):
			outputs = y[ind]

			# forward propagation of inputs through all the layers
			for layer in self.network:
				inputs = layer.forward_prop(inputs)
			
			prediction = inputs[0]
			if prediction > 0.5:
				yhat.append(1)
			else:
				yhat.append(0)
						
		return yhat

	def CM(self,y_test, y_test_obs):

		cm=[[0,0],[0,0]]
		fp=0
		fn=0
		tp=0
		tn=0		

		for i in range(len(y_test)):
			if(y_test[i]==1 and y_test_obs[i]==1):
				tp=tp+1
			if(y_test[i]==0 and y_test_obs[i]==0):
				tn=tn+1
			if(y_test[i]==1 and y_test_obs[i]==0):
				fp=fp+1
			if(y_test[i]==0 and y_test_obs[i]==1):
				fn=fn+1
				
		cm[0][0]=tn
		cm[0][1]=fp
		cm[1][0]=fn
		cm[1][1]=tp

		p= tp/(tp+fp)
		r=tp/(tp+fn)
		f1=(2*p*r)/(p+r)
		accuracy = (tp+tn)/(tp+tn+fp+fn)

		print("Confusion Matrix : ",cm)
		print(f"Precision : {p}")
		print(f"Recall : {r}")
		print(f"F1 SCORE : {f1}")
		print(f"Accuracy : {accuracy}")

if __name__ == "__main__":

	# Reading the cleaned dataset using Pandas
	df = pd.read_csv("LBW_Preprocessed.csv")

	# Creating Train-Test Splits of the dataset using .train_test_split() in Sklearn
	from sklearn.model_selection import train_test_split
	X = df.iloc[:,:-1].values
	y = df.iloc[:,-1:].values

	# Extra column filled with ones to account for the bias term
	X = np.insert(X, 0, np.ones(np.shape(X)[0]), axis=1)
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

	# Creating ANN with
	# 	7 inputs nodes
	# 	20 nodes in hidden layer, 'tanh' - activation function
	#	1 node in output layer, 'sigmoid' - activation function
	classifier = Neural_Network((6+1, 20, 1), ('tanh', 'logistic'))

	# Training the neural network on train dataset
	classifier.fit(X_train, y_train)

	print("\n\tTEST DATASET")
	# Using the trained neural network to predict
	prediction = classifier.predict(X_test)

	# prints the performance metrics
	classifier.CM(y_test, prediction)

	
	# Performance matric of the network on training dataset
	print("\n\tTRAIN DATASET")
	prediction = classifier.predict(X_train)
	classifier.CM(y_train, prediction)



	


