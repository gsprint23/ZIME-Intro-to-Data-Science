import pandas as pd # convention
# standard way to do something
# pd.

# pandas is short for "panel data"
# is built on top of numpy ("numerical
# python")
# 2 main reasons to use pandas for
# data science
# 1. really great built-in functionality
# for indexing, cleaning, statistics,
# etc.
# 2. label-based indexing (in addition
# to position-based indexing)

# there are 2 main objects in pandas
# 1. Series: 1D data (like a more
# powerful list)
# 2. DataFrame: 2D data (like a more
# powerful 2D list)

# let's start with Series
populations = [26.8, 21.1, 7.9, 2.6]
cities = ["Shanghai", "Beijing", \
          "Hangzhou", "Zibo"]
pop_ser = pd.Series(populations, index=cities)
print(pop_ser)
print()

# we can name a Series
# this is really helpful if we are going
# to insert this Series as a column
# later in a DataFrame
pop_ser.name = "Population"
print(pop_ser)
print()

# indexing/slicing (:)
# we can use a label to get a value
print(pop_ser["Beijing"])
print()
print(pop_ser[["Beijing", "Zibo"]])
print()
print(pop_ser["Beijing": "Zibo"])
print()
# start and stop labels are included
# we can still do position-based indexing
# with Series (use .iloc[])
# iloc -> integer location
print(pop_ser.iloc[1]) # same output as
# print(pop_ser["Beijing"])
# task: get the same output as
# print(pop_ser[["Beijing", "Zibo"]])
print("*", pop_ser.iloc[[1, 3]])
# then
# print(pop_ser["Beijing": "Zibo"])
# using .iloc
print("**", pop_ser.iloc[1:4])
# stop is excluded

# summary statistics
print("average population:", pop_ser.mean())
print("standard deviation population:", \
      pop_ser.std())
print()

# we can add new data to a Series
# very similar to how you add a new
# key:value pair to a dictionary
pop_ser["Liuzhou"] = 2.1
print(pop_ser)
print(len(pop_ser))
print(pop_ser.shape)
print()

# we can create an empty Series
pop_ser2 = pd.Series(dtype=float)
print(pop_ser2)
pop_ser2["Liuzhou"] = 2.1
print(pop_ser2)
print()

# let's start DataFrames
# we can make a DataFrame from a 2D list
# let's make a pop_df w/3 columns
# 1 column for City
# 1 column for Population
# 1 column Class (small, medium, large)
pop_data = [
    ["Shanghai", 26.8, "Large"],
    ["Beijing", 21.1, "Large"],
    ["Hangzhou", 7.9, "Medium"],
    ["Zibo", 2.6, "Small"]
]
header = ["City", "Population", "Class"]
pop_df = pd.DataFrame(pop_data, columns=header)
print(pop_df)

# indexing/slicing
# grab a column by its label (to get a Series)
pop_ser3 = pop_df["Population"]
print(type(pop_ser3))
print(pop_ser3)
# grab a column by its position
# (to get a Series)
pop_ser4 = pop_df.iloc[:, 1] # : to grab all
# rows, 1 to grab the Population column
print(pop_ser4)
# grab a single value
print(pop_df.iloc[0, 1])
pop_df = pop_df.set_index("City")
# sets City to be the row index (like key)
print(pop_df)
# grabbing row first (to get a Series)
print(pop_df.loc["Shanghai"]["Population"])
# grabbing column first (to get a Series)
print(pop_df["Population"]["Shanghai"])

# let's do join demo
# we have pop_df
# we need a second DataFrame
# let's make a file called regions.csv
# we will open this file with pandas
# to store its data in a DataFrame
regions_df = pd.read_csv("regions.csv",
                         index_col=0)
print(regions_df)
print()
# now let's join it with pop_df
# inner join by default
# merged_df = pop_df.merge(regions_df,
#                         on=["City"])
# outer join
merged_df = pop_df.merge(regions_df,
                         on=["City"],
                         how="outer")
print(merged_df)
print()
# let's save our merged_df to a CSV file
merged_df.to_csv("merged.csv")

# data aggregation: gathering and presenting
# data in a summarized form
# example: split-apply-combine
# (uses groupby)
# let's say we want to compute the
# average city population by class
# 1. split the data on an attribute
# (Class) to create subtables
grouped_by_class = merged_df.groupby("Class")
# 2. apply a function/operation (mean())
# to the data in each subtable
mean_pop_ser = grouped_by_class["Population"].mean()
# 3. combine the results from step #2
# into a summary table (Series)
mean_pop_ser.name = "Mean Population"
print(mean_pop_ser)
print()

# grab one of the subtables from
# step #1
large_df = grouped_by_class.get_group("Large")
print(large_df)
print()
# another way to do this
# using boolean indexing
large_df2 = \
    merged_df[merged_df["Class"] == "Large"]
print(large_df2)
print()

# just a few more DataFrame demos
# value_counts()
print(merged_df["Class"].value_counts())
print()
# sort_values()
merged_df = \
    merged_df.sort_values("Population",
                          ascending=False)
print(merged_df)
print()
# isnull()
# null meaning NaN (missing value)
# where the missing values are
print(merged_df.isnull())
print()
# number of missing values in each column
print(merged_df.isnull().sum())
print()
# number of missing values in the dataframe
print(merged_df.isnull().sum().sum())
