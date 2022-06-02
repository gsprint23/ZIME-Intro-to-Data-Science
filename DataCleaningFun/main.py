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
    # print(curr_class)
    # let's convert them all to be lowercase
    # "hoa" and "pd"
    curr_class = curr_class.lower()
    if "hoa" in curr_class or "healthy" in curr_class:
        class_ser.iloc[i] = "hoa"
    # task: replace all the parkinson's related class values
    # with "pd"
    elif "pd" in curr_class or "parkinson" in curr_class:
        class_ser.iloc[i] = "pd"
    else:
        print("unrecognized class:", curr_class)

# then overwrite the "class" column with class_ser
df["class"] = class_ser
print(df["class"].value_counts())

# check column types
for column in df.columns:
    print(column, df[column].dtype) # dtype for data type
    # object means string

# print the total seconds over all participants' tasks
print(type(df["duration"].sum())) # bug! the durations are strings
# so we get string concatentation (+), not number addition
# let's convert the duration column to integer type
df["duration"] = df["duration"].astype(int)
print(df["duration"].dtype)
print(type(df["duration"].sum()))

# finally, lets write out the cleaned dataframe to a file
# for later use
df.to_csv("pd_hoa_activities_cleaned.csv", index=False)