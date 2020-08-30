'''
Assume df is a pandas dataframe object of the dataset given
'''
import numpy as np
import pandas as pd
import random

'''Calculate the entropy of the enitre dataset'''
def get_entropy_of_dataset(df):
    # Initialize Entropy(S)
    entropy = 0

    # Obtain list of unique target values, here 'yes' or 'no'
    target_values = df.play.unique()

    # Sumation of -pi*log(pi)
    for tar_val in target_values:
        pi = df.play.value_counts()[tar_val] / (len(df.play) + np.finfo(float).eps)
        entropy += -(pi * np.log2(pi + np.finfo(float).eps))

    # Return Entropy(S) of dataset
    return entropy



'''Return entropy of the attribute provided as parameter'''
def get_entropy_of_attribute(df,attribute):
    # Initialize Attribute Entropy(A)
    entropy_of_attribute = 0

    # Obtain list of unique target values, here 'yes' or 'no'
    target_values = df.play.unique()
    # Obtain list of unique features/values of attribute
    attribute_values = df[attribute].unique()

    for att_val in attribute_values:
        # Initialize Feature Entropy(A=att_val) or Sv
        entropy_of_feature = 0
        # Find pi denominator
        pi_den = len(df[attribute][df[attribute] == att_val])

        # Sumation of pi*log(pi) of Sv or Feature Entropy(A=att_val)
        for tar_val in target_values:
            # Find pi numerator
            pi_num = len(df[attribute][df[attribute] == att_val][df.play == tar_val])
            # Find pi
            pi = pi_num / (pi_den + np.finfo(float).eps)
            # Accumulate Feature Entropy(A=att_val)
            entropy_of_feature += -(pi * np.log2(pi + np.finfo(float).eps))

        # Accumulate Attribute Entropy(A=att_val)
        entropy_of_attribute += -((pi_den/len(df) * entropy_of_feature))

    # Return Attribute Entropy(A)
    return np.absolute(entropy_of_attribute)



'''Return Information Gain of the attribute provided as parameter'''
def get_information_gain(df,attribute):
    # Information Gain(S,A) of attribute A = Dataset Entropy(S) - Attribute Entropy(A)
	information_gain = get_entropy_of_dataset - get_entropy_of_attribute(df,attribute)
	return information_gain



''' Returns Attribute with highest info gain'''
def get_selected_attribute(df):

	information_gains={}
	selected_column=''

	'''
	Return a tuple with the first element as a dictionary which has IG of all columns
	and the second element as a string with the name of the column selected

	example : ({'A':0.123,'B':0.768,'C':1.23} , 'C')
	'''

	return (information_gains,selected_column)



'''
------- TEST CASES --------
How to run sample test cases ?

Simply run the file DT_SampleTestCase.py
Follow convention and do not change any file / function names

'''