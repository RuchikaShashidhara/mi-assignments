Course: Machine Intelligence (UE18CS303)

Assignment: Designing Artificial Neural Networks for Classification of LBW Cases from Scratch
Team Name: PESU-MI_0046_1282_1445

File Structure:

PESU-MI_0046_1282_1445/
|
| - data/
|   | - LBW_Prepocessed.CSV
|
| - src/
|   | - LBW_Preprocessed.csv
|   | - data_preprocessing.py
|   | - neural_net.py
|   
| - README.txt 
 

Steps to run the Neural Net implementation:
python3 neural_net.py

Data Preprocessing is taken care only by simple numpy & pandas methods

> The dataset was read into a dataframe using pandas

> The columns "Community", "Delivery Phase", "Education" were dropped, as there was less co-relation with Result Column.
"Delivery Phase" and "Education" also had the same attribute values for more than 94% of the data.

> The missing values(NaNs) in the "Weights" column was replaced with the mean of its respective category (1 or 0 of Result).

> The missing values(NaNs) in the other numeric columns - "Age", "HB", "BP" was replaced with the mean of its column.

> The outliers present in the "Age" & "BP" columns was scaled down to fit between the range (Q1 - 1.5IQR, Q3 + 1.5IQR). 
This was implemented in the scale_outlier function we defined.

> We also labelled Residence = 2 as Residence = 0 to get Binary Labelled Column (Before: Residence(1,2), After: Residence(1,0))
The missing values(NaNs) in the "Residence" column was replaced with its Mode = 1

> Finally, all the data in each coulmn was Normalized using Min-Max Scaling by the function we defined - min-max-scaling

