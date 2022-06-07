# EDA: exploratory data analysis
# getting familiar with your data
# for example: summarize it using
# - statistics (like average, standard deviation, etc.)
# - visualizations (like line charts, bar charts, histograms, etc.)
# - mining techniques (like looking for patterns, relationships,
# groups, etc.)

# goals of data visualization
# 1. clearly and accurately represent data
# 2. be creative, while trying to increase readability
# and understanding
# 3. label axes, units, and points of interest

# we are going to use the matplotlib library for our visualizations
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def line_chart_example(x_ser, y_ser):
    # x_ser and y_ser are parallel
    plt.plot(x_ser, y_ser, c="green", lw=5, label="Population") # c for color
    # lw for line width
    plt.plot(x_ser, y_ser * 2, c="purple", lw=7, ls="--", label="Population x2")
    # ls is for line style

    # lets increase the readability of our chart
    plt.ylabel("Population (in millions)") # in millions is the units
    plt.xlabel("City Class")
    plt.title("Chinese Population Analysis")
    plt.legend()

    # right before plt.savefig(), I recommend calling plt.tight_layout()
    # to make sure everything gets layed out nicely
    plt.tight_layout()
    plt.savefig("line_example.png") # fig is short for figure (the chart)
    # many popular image file formats that matplotlib supports
    # example: .png, .jpg, .pdf, etc.

def scatter_chart_example(x_ser, y_ser):
    plt.figure() # call for a new "figure"
    # (chart, visualization)
    plt.scatter(x_ser, y_ser, s=300, marker="x")
    # s for size
    plt.savefig("scatter_example.png")

def bar_chart_example(x_ser, y_ser):
    plt.figure()
    plt.bar(x_ser, y_ser)
    plt.savefig("bar_example.png")

def pie_chart_example(values_ser, labels_ser):
    plt.figure()
    plt.pie(values_ser, labels=labels_ser, autopct="%1.1f%%") # auto percent labels
    plt.savefig("pie_example.png")

def histogram_chart_example(values_ser1, values_ser2):
    plt.figure()
    # default number of bins (rectangles/bars)
    # is 10
    # alpha is the transparency of the bars
    plt.hist(values_ser1, bins=30, alpha=0.5)
    plt.hist(values_ser2, bins=30, alpha=0.5)
    plt.ylabel("Count (Frequency) of each x-axis bin")
    plt.savefig("histogram_example.png")

df = pd.read_csv("merged.csv")
# grab the total population for each class (Large, Medium, and Small)
grouped_by_class = df.groupby("Class")
class_pop_ser = grouped_by_class["Population"].sum()
print(class_pop_ser)

# we will do examples of a few different types of charts (visualizations)
# 1. line
# great for numeric (y) data points that can be interopolated between numeric
# (x) data points
line_chart_example(class_pop_ser.index, class_pop_ser)

# 2. scatter
# great for LOTS of numeric (y) data points that should not be interpolated
# between categorical (x) data points 
scatter_chart_example(class_pop_ser.index, class_pop_ser)

# 3. bar
# great for FEWER numeric (y) data points that should not be interpolated
# between categorical (x) data points 
bar_chart_example(class_pop_ser.index, class_pop_ser)

# 4. pie
# great for numeric data that represent parts (percentages) 
# of a whole (total)
pie_chart_example(class_pop_ser, class_pop_ser.index)

# 5. histograms
# great for showing the distribution (shape) of numeric data
# by showing the counts of values in "bins" (sections of the data)
# we need more data
# so let's randomly generate some "normally distributed" data
mean = 100 # center of distribution
stdev = 25 # how spread out the data is from the mean
num_samples = 1000 # how many data points
rand_data1 = np.random.normal(mean, stdev, num_samples)
# the larger the standard deviation, the shorter and wider
# the histogram shape
rand_data2 = np.random.normal(mean, stdev / 2, num_samples)
histogram_chart_example(rand_data1, rand_data2)