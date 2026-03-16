import numpy as np
from random import seed


class NeuralNetwork:

    def __init__(self, layer_sizes):
        """
        Neural Network initialization.
        Given layer_sizes as an input, you have to design a Fully Connected Neural Network architecture here.
        :param layer_sizes: A list containing neuron numbers in each layers. For example [3, 10, 2] means that there are
        3 neurons in the input layer, 10 neurons in the hidden layer, and 2 neurons in the output layer.
        """
        # TODO (Implement FCNNs architecture here)
        # for having a random number

        # shows the number of each layer
        self.input_layer=layer_sizes[0]
        self.hidden_layer=layer_sizes[1]
        self.output_layer=layer_sizes[2]

        # it is a 3D array
        # (first is the node number of first layer , second is the node number of second layer and the third one is the weight)
        self.weight_1_2=np.random.randn(self.hidden_layer, self.input_layer)
        self.weight_2_3=np.random.randn(self.output_layer, self.hidden_layer)
        self.bias_1_2=np.zeros(self.hidden_layer)
        self.bias_2_3=np.zeros(self.output_layer)

        # array = np.random.randint(10, size=(2, 3))
        # for i in range(0,self.input_layer):
        #     for j in range(0,self.hidden_layer):
        #         self.weight_1_2[(i+1,j)]=random()
        pass

    def activation(self, x):
        """
        The activation function of our neural network, e.g., Sigmoid, ReLU.
        :param x: Vector of a layer in our network.
        :return: Vector after applying activation function.
        """
        # TODO (Implement activation function here)
        x=(1 / (1 + np.exp(-x)))
        return x
        pass

    def forward(self, x):
        """
        Receives input vector as a parameter and calculates the output vector based on weights and biases.
        :param x: Input vector which is a numpy array.
        :return: Output vector
        """
        # TODO (Implement forward function here)
        x=np.array(x)
        output_1_2=self.activation(np.add(np.array(np.dot(self.weight_1_2,x)),self.bias_1_2))
        output_1_2 = np.array(output_1_2)
        output_2_3=self.activation(np.add(np.dot(self.weight_2_3,output_1_2),self.bias_2_3))
        output_2_3 = np.array(output_2_3)




        # for i in range(0,self.hidden_layer):
        #     output_1_2[i]=self.activation(float((-1) * float(self.weight_1_2[(0,i)])))
        # for i in range(0,self.hidden_layer):
        #     for j in range(0, len(x)):
        #         output_1_2[i]+= self.activation(float(self.weight_1_2[(j, i)]) * float(x[j]))
        # res1=[]
        # for i in output_1_2:
        #     if(i>=0):
        #         res1.append(1)
        #     else:
        #         res1.append(0)


        # output_2_3={}
        # for i in range(0,self.output_layer):
        #     output_2_3[i]=self.activation(float((-1) * self.weight_2_3[(0,i)]))
        # for i in range(0,self.output_layer):
        #     for j in range(0, len(res1)):
        #         output_2_3[i] += self.activation(float(self.weight_2_3[(j+1, i)] * res1[j]))
        #
        # res2=[]
        # for i in output_2_3:
        #     if(i>=0):
        #         res2.append(1)
        #     else:
        #         res2.append(0)
        return output_2_3
        pass
