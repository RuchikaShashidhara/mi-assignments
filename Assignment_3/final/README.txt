Course: Machine Intelligence (UE18CS303)

Assignment #3: Designing Artificial Neural Networks for Classification of LBW Cases from Scratch
Team Name: PESU-MI_0046_1282_1445

File Structure:

PESU-MI_0046_1282_1445/
|
| - data/
|   | - LBW_Prepocessed.CSV
|
| - src/
|   | - LBW_Preprocessed.csv
|   | - Data_Preprocessing.py
|   | - Neural_Net.py
|   
| - README.txt 
 

Steps to run the Neural Net implementation:
Install the following dependencies:
numpy, pandas, sklearn

For using the Neural Network for predictions, simply run:
python3 src/neural_net.py

For creating the cleaned datset again, place the original uncleaned dataset in src folder & run 
python3 src/data_preprocessing.py


Data Preprocessing is taken care only by simple numpy & pandas methods:

> The dataset was read into a dataframe using pandas.

> The columns "Community", "Delivery Phase", "Education" were dropped, as there was less co-relation with Result Column.
"Delivery Phase" and "Education" also had the same attribute values for more than 94% of the data.

> The missing values(NaNs) in the "Weights" column was replaced with the mean of its respective category (1 or 0 of Result).

> The missing values(NaNs) in the other numeric columns - "Age", "HB", "BP" was replaced with the mean of its column.

> The outliers present in the "Age" & "BP" columns was scaled down to fit between the range (Q1 - 1.5IQR, Q3 + 1.5IQR). 
This was implemented in the scale_outlier function we defined.

> We also labelled Residence = 2 as Residence = 0 to get Binary Labelled Column (Before: Residence(1,2), After: Residence(1,0))
The missing values(NaNs) in the "Residence" column was replaced with its Mode = 1.

> Finally, all the data in each coulmn was Normalized using Min-Max Scaling by the function we defined - min-max-scaling 
and was saved as the final preprocessed CSV file.


Neural Network Implementation:

The architecture of the Neural Network consists of 3 Layers in total - 1 Input Layer, 1 Hidden Layer and 1 Output Layer.
The new preprocessed dataset consits of 6 input variable columns - "Age", "Weight", "HB", "IFA", "BP", "Residence" and 
1 output variable coulmn - "Result". So, the first Input Layer consists of 7 nodes, 6 inputs from the dataset and
1 as calculated bias node. The hidden layer consists of 20 nodes which uses the tanh function as the activation function
and the Output Layer consists of 1 node in which if the probability > 0.6, it is predicted as 1 (Result is LBW case)
else it is predicted as 0 (Result is not an LBW case). The output uses the sigmoid function as the activation function.
We have also implemented the loss/cost function using the implemenation of the Binary Cross Entropy function and we have
also implemnted the Adam Optimizer for solving.

Hyperparameters for the current model:

> alpha(learning rate): 1e-5
> beta_1(exponential decay rate for the first moment estimates) = 0.9
> beta_2(The exponential decay rate for the second-moment estimates) = 0.99
> epsilon = 1e-8
> Minibatch size: 67
> Epochs: 40000

Key Features of our design:
Our neural network can use "any number of nodes" in the "hidden layers" and can use any of the "activation functions" -
"tanh", "relu", "sigmoid"/"logistic", and "identity". We also input 1 extra node for bias for better learning of the neural network.
The hyperparamters can also be changed for other NN models by mentionaing it while calling the NN object.



