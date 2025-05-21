# create the dictionary (task 1)
language_pop = {'JavaScript': 62.3, 'HTML': 52.9, 'Python': 51, 'SQL': 51, 'TypeScript': 38.5}
print(language_pop)

# The folowing create a bar graph for given data (task 2)
# import the package
import matplotlib.pyplot as plt
import numpy as np
#create the bar graph
plt.bar(list(language_pop.keys()), list(language_pop.values()))
#set the x-label, y label & tittle
plt.xlabel('language type')
plt.ylabel('users percentage')
plt.title('Percentage of developers who use the top 5 programming languages globally')
plt.yticks(np.arange(0, 71, 10))
#show the graph
plt.show()

# The folowing showa the percentage of users when asked one language type (task 3)
# ask for an input and transfrom it to a string
request = str(input('Enter the language:'))
# check if answer is in the dictionary
if request in language_pop:
    # If in the dictionary, then print the answer
    print(language_pop[request], '%')
else:
    print('Sorry, this language is not in the dictionary :(')