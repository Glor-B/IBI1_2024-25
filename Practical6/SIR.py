# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# define basic variables
N = 10000 # total number of people
S = 9999 # susceptible individuals
I = 1 # infected people
R = 0 # recovered infected people
beta = 0.3 # infection probability
gamma = 0.05 # recovery probability

# create arrays for each variables
S_re = [S]
I_re = [I]
R_re = [R]

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
    random_I = np.random.choice(range(0,2), S, p = [1 - pI, pI])
    """ or j in random_I:
        if j == 1:
            new_I += 1 """
    new_I = sum(random_I)
    I = I - new_R + new_I
    S -= new_I
    # append the new number in each list
    S_re.append(S)
    I_re.append(I)
    R_re.append(R)

""" print(S_re)
print(I_re)
print(R_re) """

# plot the figure for the result
plt.figure(figsize = (6,4), dpi = 150)
plt.plot(S_re)
plt.plot(I_re)
plt.plot(R_re)
plt.xlabel('Times')
plt.ylabel('Number of people')
plt.title('SIR mode')
plt.legend(['susceptible', 'infected', 'recovered'])
plt.show()