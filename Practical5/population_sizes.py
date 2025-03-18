#The following finish task1: sorting
import pandas as pd
# set the dataframe
df = pd.DataFrame(
    {
        "Country/Province":[
            'England','Wales', 'Northern Ireland', 'Scotland', 'Zhejiang', 'Fujian', 'Jiangxi', 'Anhui', 'Jiangsu'
        ],
        "Nation":[
            'UK', 'UK', 'UK', 'UK', 'China', 'China', 'China', 'China', 'China'
        ],
        "Population":[
            57.11, 3.13, 1.91, 5.45, 65.77, 41.88, 45.28, 61.27, 85.15
        ]
    }
)
#Sort according to nation
UK_country = df[ df['Nation'] == 'UK']
China_province = df[ df['Nation'] == 'China' ]
#print the results
print(UK_country)
print(China_province)


#The following create a pie chart
import matplotlib.pyplot as plt
# First, plot the pie chart for UK
# Convert dataframe to list
labels_UK = UK_country['Country/Province'].tolist()
#print(labels)
sizes_UK = UK_country['Population'].tolist()
#print(sizes)
explode = (0, 0, 0, 0)
plt.pie(sizes_UK, explode = explode, labels = labels_UK, autopct = '%1.1f%%')
plt.title('Distribution of population sizes in UK')
plt.axis('equal')
plt.show()
# Then, plot the pie chrat for China
# Jst to previous steps again
labels_China = China_province['Country/Province'].tolist()
sizes_China = China_province['Population'].tolist()
explode = (0, 0, 0, 0, 0)
plt.pie(sizes_China, explode = explode, labels = labels_China, autopct = '%1.1f%%')
plt.title('Distribution of population sizes in China')
plt.axis('equal')
plt.show()