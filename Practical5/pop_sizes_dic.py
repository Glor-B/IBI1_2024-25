# create two dictionaries
country_nation = {
    'England': 'UK','Wales': 'UK', 'Northern Ireland': 'UK', 'Scotland': 'UK',
    'Zhejiang': 'China', 'Fujian': 'China', 'Jiangxi': 'China', 'Anhui': 'China', 'Jiangsu': 'China'
}
country_pop = {
    'England': 57.11,'Wales': 3.13, 'Northern Ireland': 1.91, 'Scotland': 5.45,
    'Zhejiang': 65.77, 'Fujian': 41.88, 'Jiangxi': 45.28, 'Anhui': 61.27, 'Jiangsu': 85.15
}
# create 2 empty dictionaries as the output dictionary
country_pop_UK = {}
province_pop_China = {}
# create empty lists to draw pie charts
UK_xlabel = []
UK_y = []
China_xlabel = []
China_y = []
# check if one coutry/province is from UK or China
for key in country_nation:
    if country_nation[key] == 'UK':
        # add that to the dictionary
        country_pop_UK[key] = country_pop[key]
        # add that to the lists
        UK_xlabel.append(key)
        UK_y.append(country_pop[key])
    else:
        province_pop_China[key] = country_pop[key]
        China_xlabel.append(key)
        China_y.append(country_pop[key])
print(UK_y)
print(China_y)
""" print(UK_xlabel)
print(UK_y) """
# Draw the pie chart
import matplotlib.pyplot as plt
# First, plot the pie chart for UK
explode = (0, 0, 0, 0)
plt.pie(UK_y, explode = explode, labels = UK_xlabel, autopct = '%1.1f%%')
plt.title('Distribution of population sizes in UK')
plt.axis('equal')
plt.show()
# Then, plot the pie chrat for China
explode = (0, 0, 0, 0, 0)
plt.pie(China_y, explode = explode, labels = China_xlabel, autopct = '%1.1f%%')
plt.title('Distribution of population sizes in China')
plt.axis('equal')
plt.show()