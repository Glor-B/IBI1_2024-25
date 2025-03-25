# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# create a dataframe to store infected data
df = pd.DataFrame(
    {
    }
)
# print(df)

# run for each vaccination rate
for vac_rate in range(0,110,10):
    # define basic variables
    N = 10000 # total number of people
    # infected people
    if vac_rate == 100:
        I = 0
    else:
        I = 1
    R = 0 # recovered infected people
    beta = 0.3 # infection probability
    gamma = 0.05 # recovery probability
    S = 9999
    # creat a list to store number of infected people in each circumstance
    I_re = [I]
    label = str(vac_rate) + '%'
    # calculate the changed susceptible individuals
    S -= S * vac_rate / 100
    # loop for 1000 time points
    for i in range (0, 1000):
        # randomly pick infected -> recovered
        # for every individuals infected,0 is unrecover, 1 is recover, the recovery probability is gamma
        random_R = np.random.choice(range(0,2), I, p = [1-gamma, gamma])
        new_R = sum(random_R)
        """ for r in random_R:
        if r == 1:
            new_R += 1 """
        R += new_R
        # randomly pick susceptible -> infected
        # the infected probability is beta * proportion of infected people in a population, 0 is uninfected, 1 is infected
        pI = beta * I / N
        random_I = np.random.choice(range(0,2), int(S), p = [1 - pI, pI])
        """ for j in random_I:
        if j == 1:
            new_I += 1 """
        new_I = sum(random_I)
        I = I - new_R + new_I
        S -= new_I
        I_re.append(I)
        #print(I)
    # add the infected people into dataframe
    df[label] = pd.Series(I_re)
    #print(S)
#print(df)
df.plot(title = 'SIR model with different accination rates', xlabel = 'Time', ylabel = 'Number of people')
plt.show()