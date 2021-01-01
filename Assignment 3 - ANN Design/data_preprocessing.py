'''
Data Preprocessing
'''
import numpy as np
import pandas as pd

# Normalization & Scaling Functions using simple Numpy & Pandas methods

# Outlier Scaling using .quantile() Pandas methods
def scale_outlier(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    min_bound = Q1 - 1.5*IQR
    max_bound = Q3 + 1.5*IQR
    df[column] = np.where(df[column] > max_bound, max_bound, df[column])
    df[column] = np.where(df[column] < min_bound, min_bound, df[column])

# Min-Max Scaling using .min() and .max() Pandas methods
def min_max_scaling(df):
    df_norm = df.copy()
    for column in df_norm.columns:
        df_norm[column] = (df_norm[column] - df_norm[column].min()) / (df_norm[column].max() - df_norm[column].min())
    return df_norm

# Data preprocessing of the input dataframe using only simple Numpy & Pandas methods
def preprocess_data(df):

    # Drop the columns Delivery Phase(1: 90, 2: 2, NaN: 4), Education(5: 93, NaN: 3), Community(Less Co-relation with Result)
    df = df.drop(["Community", "Delivery phase", "Education"], axis = 1)

    # Replacing Nan of Weights with the Mean of its respective Result category
    mean_0 = (df.loc[df['Result'] == 0])['Weight'].mean()
    mean_1 = (df.loc[df['Result'] == 1])['Weight'].mean()

    df["Weight"] = np.where((df["Result"] == 0) & (df["Weight"].isna()), mean_0, df["Weight"])
    df["Weight"] = np.where((df["Result"] == 1) & (df["Weight"].isna()), mean_1, df["Weight"])

    # Filling all other Numeric Columned NaN Values with Mean
    df["Age"] = df["Age"].fillna(df["Age"].mean())
    df["HB"] = df["HB"].fillna(df["HB"].mean())
    df["BP"] = df["BP"].fillna(df["BP"].mean())

    # Taking care of Outliers by replacing with its IQR, Min-Max for Age & BP columns
    scale_outlier(df, "Age")
    scale_outlier(df, "BP")

    # Labelling Residence = 2 as Residence = 0 to get Binary Labelled Column (Before: Residence(1,2), After: Residence(1,0))
    df["Residence"] = np.where(df["Residence"] == 2, 0, df["Residence"])
    # Filling NaN with Mode = 1
    df["Residence"] = df["Residence"].fillna(1)

    # Converting all other values to float
    df["IFA"] = df["IFA"].astype(float)
    df["Result"] = df["Result"].astype(float)

    # Performing Normalization of the dataset (into ranges from 0 to 1) using Pandas
    df = min_max_scaling(df)

    return df


if __name__ == "__main__":

    # Reading the dataset using Pandas
    df = pd.read_csv("LBW_Dataset.csv")

    # Preprocessing & Cleaning the dataset
    df = preprocess_data(df)

    # Saving the cleaned dataset as a csv
    df.to_csv("LBW_Preprocessed.csv", header=True, index=False)









