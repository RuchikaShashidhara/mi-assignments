# mi-assignments
This repository contains the assignments submitted for the course Machine Intellignce UE18CS303 offered by PES University.

## Assignment 1 - Decision Tree Classifier

| Requirements  | Implementation file | Sample Test Validation file |
| --------------| ------------------- | --------------------------- |
| numpy         | Assignment1.py      | DT_SampleTestCase.py        |
| pandas        |                     | test_cases.py               |               

### Instructions to run:
```python3 DT_SampleTestCase.py```

```python3 test_cases.py```

### Parameters:

df - pandas dataframe consisting of the dataset

attribute - string attribute, a certain coulmn name of the panadas dataframe

### Functions defined:
1) ```get_entropy_of_dataset(df)``` returns Entropy of the enitre dataset  

2) ```get_entropy_of_attribute(df,attribute)``` returns Entropy of the attribute provided as parameter

3) ```get_information_gain(df,attribute)``` returns Information Gain of the attribute provided as parameter 

4) ```get_selected_attribute(df)```  returns Attribute with highest info gain



## Assignment 2 - Search Algorithms

| Requirements  | Implementation file | Sample Test Validation file |
| --------------| ------------------- | --------------------------- |
| -             | Assignment2.py      | sample_test_case.py         |            
|               |                     | test_cases.py               | 

### Instructions to run:
```python3 sample_test_case.py```

```python3 test_cases.py```

### Parameters:

n - Number of nodes in the graph
m - Number of goals ( Can be more than 1)
1 <= m <= n

cost[n][n] - Cost matrix for the graph of size (n+1)x(n+1)
(The 0th row and 0th column is not considered as the starting index is from 1 and not 0)

heuristic[n] - Heuristic list for the graph of size 'n+1'
(Ignore 0th index as nodes start from index value of 1)

start_point - single start node

goals[m] - list of size 'm' containing 'm' goals to reach from start_point

### Functions defined: 
1) ```get_selected_attribute(cost, heuristic, start_point, goals)``` Returns all lexicological first path traversals [[],[],[]] for each - A-star, UCS and DFS traversals
2)  ```A_star_Traversal(cost, heuristic, start_point, goals)``` Returns lexicological first A star path
3)  ```UCS_Traversal(cost, start_point, goals)``` Returns lexicological first UCS path
4)  ```DFS_Traversal(cost, start_point, goals)``` Returns lexicological first DFS path

