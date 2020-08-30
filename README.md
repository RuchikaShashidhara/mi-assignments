# mi-assignments
This repository contains the assignments submitted for the course Machine Intellignce UE18CS303 offered by PES University.

## Assignment 1 - Decision Tree Classifier

| Requirements  | Implementation file | Sample Test Validation file |
| --------------| ------------------- | --------------------------- |
| numpy, pandas | Assignment1.py      | DT_SampleTestCase.py        |

### Instructions to run:
```python3 DT_SampleTestCase.py```

### Functions defined:
1) get_entropy_of_dataset(df): Calculate the entropy of the enitre dataset
2) get_entropy_of_attribute(df,attribute): Return entropy of the attribute provided as parameter
3) get_information_gain(df,attribute): Return Information Gain of the attribute provided as parameter
4) get_selected_attribute(df): Returns Attribute with highest info gain
