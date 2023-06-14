import pandas as pd

header1 = ["employee_number", "last_name", "salary"]
table1 = [
    [1001, "Smith", 62000],
    [1002, "Everest", 71000],
    [1003, "Anderson", 57500],
    [1004, "Franks", 54000],
    [1005, "Horvath", 42000]
]

header2 = ["employee_number", "dept_id"]
table2 = [
    [1001, 500],
    [1002, 50],
    [1003, 500],
    [1005, 501]
]

# How many instances and how many attributes does each table have?
# -> table 1: 5 instances and 3 attributes
# -> table 2: 4 instances and 2 attributes

# What are the key(s)?
# -> table 1: employee_number
# -> table 2: employee_number, dept_id (foreign key for another table likely)

# Write code to do the following:
#     Load each table into a `DataFrame`
df1 = pd.DataFrame(table1, columns=header1)
print(df1.shape)
df2 = pd.DataFrame(table2, columns=header2)
print(df2.shape)
df1.set_index("employee_number", inplace=True)
df2.set_index("employee_number", inplace=True)

#     Join the two tables using a full outer join
df = df1.merge(df2, on=["employee_number"], how="outer")
print(df)

#     Split-apply-combine to produce a `Series` with total salary paid per department
grouped_by_dept = df.groupby("dept_id")
salary_per_dept_ser = grouped_by_dept["salary"].sum()
print(salary_per_dept_ser)