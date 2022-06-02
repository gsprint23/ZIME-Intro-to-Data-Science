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

df = pd.read_csv("merged.csv")
# grab the total population for each class (Large, Medium, and Small)
grouped_by_class = df.groupby("Class")
class_pop_ser = grouped_by_class["Population"].sum()
print(class_pop_ser)

# we will do examples of a few different types of charts (visualizations)
# 1. line
line_chart_example(class_pop_ser.index, class_pop_ser)

# 2. scatter
scatter_chart_example(class_pop_ser.index, class_pop_ser)

# 3. bar

# 4. pie

# 5. histograms