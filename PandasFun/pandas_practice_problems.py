import pandas as pd

df =  pd.read_csv("basketball.csv", index_col=0)
print(df)

new_row = pd.Series(["G",12,20,1], index=df.columns)
new_row.name = "Joe Few"
df = df.append(new_row) # use ignore_index=True
# if no name for the series
print(df)

df["Class"] = ["Sr", "Jr", "Fr", "Fr", "Jr", "Fr", "So", "Fr", "Jr", "Sr", "Fr", "Sr", "Sr", "Fr"]
print(df)

class_counts_ser = df["Class"].value_counts()
print(class_counts_ser)

grouped_by_class = df.groupby("Class")
mean_pts_ser = grouped_by_class["PTS"].mean()
print(mean_pts_ser)

ppg_ser = df["PTS"] / df["GP"]
print(ppg_ser)
# lots of ways to do this...
print(ppg_ser[ppg_ser == ppg_ser.max()])