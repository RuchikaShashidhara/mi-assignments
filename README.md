# mi-assignments

#### Team Members: Kavya, Ruchika and Sonam

#### Requirements: numpy, pandas and scikit-learn
<br/>

## Assignment 1 - ID3 Attribute Selection 

### Implementation file: 
```Assignment1.py```  

### Instructions to run sample tests:

```python3 DT_SampleTestCase.py```

```python3 test_cases.py``` 
<br/>

### Functions defined:

1) ```get_entropy_of_dataset(df)``` returns the Entropy of the enitre dataset  

2) ```get_entropy_of_attribute(df,attribute)``` returns the Entropy of the attribute provided as parameter

3) ```get_information_gain(df,attribute)``` returns the Information Gain of the attribute provided as parameter 

4) ```get_selected_attribute(df)``` returns the Attribute with highest Information Gain
<br/><br/>

## Assignment 2 - Search Algorithms

### Implementation file: 
```Assignment2.py```

### Instructions to run sample tests:

```python3 sample_test_case.py```

```python3 test_cases.py```
<br/>

### Functions defined: 
1) ```get_selected_attribute(cost, heuristic, start_point, goals)``` returns all lexicological first path traversals [[],[],[]] for each - A-star, UCS and DFS traversals

2)  ```A_star_Traversal(cost, heuristic, start_point, goals)``` returns lexicological first A star path

3)  ```UCS_Traversal(cost, start_point, goals)``` returns lexicological first UCS path

4)  ```DFS_Traversal(cost, start_point, goals)``` returns lexicological first DFS path
<br/><br/>

## Assignment 3 - Designing an Artificial Neural Network for Classification of LBW Cases from scratch

### Implementation files:

```Neural_Net.py```

```data_preprocessing.py```

### Instructions to run: 

```python3 data_preprocessing.py```

```python3 Neural_Net.py```
<br/>

### Steps taken for Data Preprocessing:

* The dataset was read into a dataframe using pandas.

* The columns "Community", "Delivery Phase", "Education" were dropped, as there was less co-relation with Result Column. "Delivery Phase" and "Education" also had the same attribute values for more than 94% of the data.

* The missing values(NaNs) in the "Weights" column was replaced with the mean of its respective category (1 or 0 of Result).

* The missing values(NaNs) in the other numeric columns - "Age", "HB", "BP" was replaced with the mean of its column.

* The outliers present in the "Age" & "BP" columns was scaled down to fit between the range (Q1 - 1.5IQR, Q3 + 1.5IQR). This was implemented in the scale_outlier function.

* Residence = 2 was also labelled as Residence = 0 to get Binary Labelled Column (Before: Residence(1,2), After: Residence(1,0)). The missing values(NaNs) in the "Residence" column was replaced with its Mode = 1.

* Finally, all the data in each coulmn was Normalized using Min-Max Scaling by the function - min-max-scaling and was saved as the final preprocessed CSV file.

### ANN Design:

The architecture of the Neural Network consists of 3 Layers in total - 1 Input Layer, 1 Hidden Layer and 1 Output Layer. The new preprocessed dataset consists of 6 input variable columns - "Age", "Weight", "HB", "IFA", "BP", "Residence" and 1 output variable coulmn - "Result". So, the first Input Layer consists of 7 nodes, 6 inputs from the dataset and 1 as calculated bias node. The hidden layer consists of 20 nodes which uses the tanh function as the activation function and the Output Layer consists of 1 node in which if the probability > 0.6, it is predicted as 1 (Result is LBW case) else it is predicted as 0 (Result is not an LBW case). The output uses the sigmoid function as the activation function. We have also implemented the loss/cost function using the implemenation of the Binary Cross Entropy and we have also implemnted the Adam Optimizer for solving.   

Hyperparameters for the current model:

* alpha(learning rate): 1e-5
* beta_1(exponential decay rate for the first moment estimates) = 0.9
* beta_2(The exponential decay rate for the second-moment estimates) = 0.99
* epsilon = 1e-8
* Minibatch size: 67
* Max Epochs: 40000  

### Functions defined: 

1) ```fit(self,X,Y)``` function that trains the neural network by taking x_train and y_train samples as input

2) ```predict(self,X)``` predict function that performs a simple feed forward of weights and outputs yhat values (yhat is a list of the predicted value for df X)

3) ```CM(y_test,y_test_obs)``` function to print confusion matrix, where y_test is list of y values in the test dataset and y_test_obs is list of y values predicted by the model
<br/><br/>


