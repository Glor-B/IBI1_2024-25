import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# Show the third column (the year) for the first 10 rows (inclusive).
task1 = dalys_data.iloc[0:10,2]
# The 10th year is 1999

# Find every row where the Year is “1990”
ls = []
for i in dalys_data.loc[ : , "Year"]:
    if i == 1990:
        ls.append(True)
    else:
        ls.append(False)
print(dalys_data.iloc[ls , : ])

# Compute the mean DALYs in the UK and France
uk = dalys_data.loc[dalys_data.Entity == "United Kingdom", "DALYs"].mean()
France = dalys_data.loc[dalys_data.Entity == "France", "DALYs"].mean()
print(uk, France)
# The mean DALYs in the UK was greater than France

# Create a plot showing the DALYS over time in the UK.
uk = dalys_data.loc[dalys_data.Entity=="United Kingdom", ["DALYs", "Year"]]
plt.plot(uk.Year, uk.DALYs, 'r+')
plt.xticks(uk.Year,rotation=-90)
plt.show()

# question.txt
print(dalys_data[dalys_data["DALYs"] > 650000])