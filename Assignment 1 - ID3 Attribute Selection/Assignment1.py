import numpy as np
import pandas as pd
import random


'''Calculate the entropy of the enitre dataset'''
def get_entropy_of_dataset(df):
    # Initialize Entropy(S)
    entropy = 0

    # Return 0 if dataset is empty
    if df.empty:
        return entropy

    # Obtain the column of desicion to be taken(generic - last columnn)
    lastColName = df.columns[-1]
    # Obtain list of unique target values
    target_values = df[lastColName].unique()

    # Sumation of -pi*log(pi)
    for tar_val in target_values:
        pi = df[lastColName].value_counts()[tar_val] / len(df[lastColName])
        if(pi == 0):
            continue
        entropy += -(pi * np.log2(pi))

    # Return Entropy(S) of dataset
    return entropy


'''Return entropy of the attribute provided as parameter'''
def get_entropy_of_attribute(df,attribute):
    # Initialize Attribute Entropy(A)
    entropy_of_attribute = 0

    # Return 0 if dataset is empty
    if df.empty:
        return entropy_of_attribute

    try:
        # Obtain the column of desicion to be taken(generic - last columnn)
        lastColName = df.columns[-1]
        # Obtain list of unique target values
        target_values = df[lastColName].unique()
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
                pi_num = len(df[attribute][df[attribute] == att_val][df[lastColName] == tar_val])
                # Find pi
                pi = pi_num / pi_den
                # Accumulate Feature Entropy(A=att_val)
                if(pi == 0):
                    continue
                entropy_of_feature += -(pi * np.log2(pi))

            # Accumulate Attribute Entropy(A=att_val)
            entropy_of_attribute += (((pi_den/len(df)) * entropy_of_feature))

    except KeyError:
        print("Attribute:", attribute, "not in dataset")

    # Return Attribute Entropy(A)
    return entropy_of_attribute


'''Return Information Gain of the attribute provided as parameter'''
def get_information_gain(df,attribute):
    # Initialize Information Gain(S,A)
    information_gain = 0

    try:
        # Information Gain(S,A) of attribute A = Dataset Entropy(S) - Attribute Entropy(A)
        information_gain = get_entropy_of_dataset(df) - get_entropy_of_attribute(df,attribute)

    except KeyError:
        print("Attribute:", attribute, "not in dataset")

    return information_gain


''' Return Attribute with highest info gain'''
def get_selected_attribute(df):

    # Return 0 if dataset is empty
    if df.empty or len(df.columns) == 1:
        return (dict(),'')

    # Obtain list of attributes, assuming the last column is the decision taken.
    attributes = list(df)[:-1]

    # Calculate information gain for each attribute
    attribute_information_gain = list(map(lambda x:get_information_gain(df,x),attributes))

    # Pair attributes with its respective information gain
    information_gains = dict(zip(attributes,attribute_information_gain))

    # Choose the attribute with the maximum information gain
    max_info_gain_index, _ = max(enumerate(attribute_information_gain),key = lambda x:x[1])
    selected_column = attributes[max_info_gain_index]

    '''
    Return a tuple with the first element as a dictionary which has IG of all columns
    and the second element as a string with the name of the column selected

    example : ({'A':0.123,'B':0.768,'C':1.23} , 'C')    '''

    return (information_gains,selected_column)

