# EDA: exploratory data analysis
# getting familiar with your data
# for example: summarize it using
# - statistics (like mean, standard deviation, sum, etc.)
# - visualizations (like line charts, bar charts,
# histograms, etc.)
# - data mining (like looking for patterns,
# relationships, groups, etc.)

# focus on visualizations
# 3 goals of visualizations
# 1. clearly and accurately represent data
# 2. be creative, while trying to to increase
# readability and understanding
# 3. label axes, units, and points of interest

# we are going to use the matplotlib library
# to visualize data as 2D charts
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def line_chart_example(x_ser, y_ser):
    # x_ser and y_ser are "parallel"
    # meaning same length and data in same order
    plt.plot(x_ser, y_ser,
             label="Population",
             c="green", # c is for color
             lw=5) # lw is for line width
    plt.plot(x_ser, y_ser * 2,
             label="Population x2",
             c="purple",
             ls="--") # ls is for line style

    # adding a legend to increase the readability
    # of our chart
    plt.legend()
    # more ways to increase readability
    # label things!
    plt.ylabel("Population (in millions)")
    plt.xlabel("City Class")
    plt.title("Chinese Population Analysis")
    # 2 main ways to see the chart
    # 1.
    # plt.show()
    # 2. 
    plt.savefig("line.png") # jpg, pdf, etc.

def scatter_chart_example(x_ser, y_ser):
    # we need to call plt.figure()
    # whenever we want a "new" figure
    # (chart, visualization)
    plt.figure()
    plt.scatter(x_ser,
                y_ser,
                s=300, # s is for size
                marker="x") # X instead of O
    plt.savefig("scatter.png")

def bar_chart_example(x_ser, y_ser):
    plt.figure()
    plt.bar(x_ser, y_ser)
    plt.savefig("bar.png")

def pie_chart_example(values_ser, labels_ser):
    plt.figure()
    plt.pie(values_ser,
            labels=labels_ser,
            autopct="%1.1f%%") # auto percent labels
    plt.savefig("pie.png")

def histogram_chart_example(values_ser1,
                            values_ser2):
    plt.figure()
    # default number of bins is 10
    plt.hist(values_ser1,
             bins=30,
             alpha=0.5) # transparency of bars
    plt.hist(values_ser2,
             bins=30,
             alpha=0.5)
    plt.ylabel("Count (Frequency) of each X-axis Bin")
    plt.savefig("histogram.png")

df = pd.read_csv("merged.csv")
print(df)
# grab the total population for each Class
# (Large, Medium, Small)
grouped_by_class = df.groupby("Class")
class_pop_ser = grouped_by_class["Population"].sum()
print(class_pop_ser)

# 1. line chart example
# great for numeric (y) data points that can be
# interpolated (or interpreted) between numeric
# (x) data points
line_chart_example(class_pop_ser.index, # Large, Medium, Small
                   class_pop_ser) # 47.9, 7.9, 2.6

# 2. scatter chart example
# great for LOTS of numeric (y) data points
# that should not be interpolated between
# categorical (x) data points
scatter_chart_example(class_pop_ser.index,
                      class_pop_ser)

# 3. bar chart example
# great for FEWER numeric (y) data points that should
# not be interpolated between categorical
# (x) data points
bar_chart_example(class_pop_ser.index,
                  class_pop_ser)

# 4. pie chart example
# great for numeric data that represents
# parts (percentages) of a whole (total)
pie_chart_example(class_pop_ser, # parts
                  class_pop_ser.index) # labels

# histogram example
# great for showing the distribution (shape)
# of numeric data
# by showing the counts of values in "bins"
# (sections of the data)
# for our example, we will need more data points
mean = 100 # center of distribution
stdev = 25 # how spread out the data is from
# the mean
num_datapoints = 1000
# normal (Gaussian) means "bell-shaped"
rand_data1 = np.random.normal(mean,
                              stdev,
                              num_datapoints)
# task: create another sample of data
# smaller standard deviation
# add its histogram to the same chart
# so there should be two histograms on the
# histogram.png
rand_data2 = np.random.normal(mean,
                              stdev / 2,
                              num_datapoints)
histogram_chart_example(rand_data1,
                        rand_data2)