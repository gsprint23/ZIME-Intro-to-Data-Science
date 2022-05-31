import numpy as np
import pandas as pd

# load the data
df = pd.read_csv("pd_hoa_activities.csv")
print(df.head()) # df.tail()
print(df.shape)

# explore the data
print("number of participants:", df.shape[0] // 9) 
# 9 because 9 is the number of tasks per participant id
df.replace("?", np.NaN, inplace=True)
print(df.isnull().sum())

# let's remove the rows with missing values
df.dropna(inplace=True)
print("after dropping rows with missing values")
print(df.isnull().sum())
print(df.shape)
# reset the index to 0, 1, 2, ...
df.reset_index(inplace=True, drop=True)
print(df.tail())

# clean the class column
class_ser = df["class"].copy() # so I don't get a warning
# about setting a value on a slice
for i in range(len(class_ser)):
    curr_class = str(class_ser.iloc[i])
    print(curr_class)
    # let's convert them all to be lowercase
    # "hoa" and "pd"
    curr_class = curr_class.lower()
    if "hoa" in curr_class or "healthy" in curr_class:
        class_ser.iloc[i] = "hoa"
    # task: replace all the parkinson's related class values
    # with "pd"
    # then overwrite the "class" column with class_ser
    
print(class_ser.value_counts())

# check column types