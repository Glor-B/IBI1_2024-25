import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# Show the third column (the year) for the first 10 rows (inclusive).
task1 = dalys_data.iloc[0:10, 2:4]
print(task1)
# 79890.55 DALYs were recorded in 1992 in Afghanistan.

# Find every row where the Year is “1990”
ls = []
for i in dalys_data.loc[ : , "Year"]:
    if i == 1990:
        ls.append(True)
    else:
        ls.append(False)
print(dalys_data.iloc[ls , 3])

# Compute the mean DALYs in the UK and France
china = dalys_data.loc[dalys_data.Entity=="China", ["DALYs", "Year"]]
max = china.max()
min = china.min()
print(max, min)
# The maximum year is 2019, the minimum year is 1990

# Create a plot showing the DALYS over time in the UK.
plt.plot(china.Year, china.DALYs, 'b+')
plt.xticks(china.Year,rotation=-90)
plt.show()

# question.txt
print(dalys_data[dalys_data["DALYs"] > 650000])