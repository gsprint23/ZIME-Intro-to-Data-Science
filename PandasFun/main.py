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



