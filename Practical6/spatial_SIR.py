# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
# make array of all susceptible population
population = np.zeros( (100, 100) )
outbreak = np.random.choice(range(0, 100), 2)
population[outbreak[0], outbreak[1]] = 1


#define the intial parameters
beta = 0.3
gamma = 0.05
timepoint = int(input('Enter the timepoint you want to check: '))
print(outbreak)


# check whether neighbors are recovered
def neighbor_check(target): 
    S = []
    I = []
    R = []
    # create a array for neighbor
    up = target[1] - 1
    low = target[1] + 1
    right = target[0] +1
    left = target[0] -1
    if left <0:
        left += 1
    if right > 99:
        right -= 1
    if up < 0:
        up += 1
    if low > 99:
        low -= 1
    # neighbors = population[up : low + 1, left : right + 1 ]
    # find the neighbor in population
    # define the exact location of neighbor point
    x = up
    while x <= low:
        y = left
        while y <= right:
            # store the location of each types of the neighbor of this point in each list
            neighbor = population[x, y]
            if neighbor == 0:
                S.append((x, y))
            elif neighbor == 1:
                I.append((x, y))
            else:
                R.append((x, y))
            y += 1
        x +=1
    return(S, I, R)

def loop(S, I, R):
    # recover infected individuals
    random_R = np.random.choice(range(0,2), len(I), p = [1 - gamma, gamma])
    #print(random_R)
    # i is the index of recovered people in random_R list
    for i in range(0, len(random_R)):
        if random_R[i] == 1:
            # for every recovered index, check them in I 
            loc = I[i] # loc is the location of individuals that should recover
            population[loc] = 2
#print(population)
    # infect unrecovered neighbor
    random_I = np.random.choice(range(0, 2), len(S), p = (1 - beta, beta))
    #print(random_I)
    for i in range(0, len(random_I)):
        if random_I[i] == 1:
            # for every recovered index, check them in I 
            loc = S[i] # loc is the location of individuals that should recover
            population[loc] = 1
    return(population)
#print(population)  





for i in range (0, timepoint):
    # select all the infected point in population
    infection = np.where(population == 1)
    target = list(zip(infection[0], infection[1]))
    loop_situation = 0 # record if loop has functioned
    for j in target:
            #print(population[x,y])
            if population[j[0], j[1]] == 1:
                # check the neighbor of this infected point
                S, I, R = neighbor_check(j)
                # print(S, I, R)
                # recover infected individuals & infect S individuals, and store them in the population
                population = loop(S, I, R)
                
# print(population)

# plot the picture
plt.figure(figsize = (6,4), dpi = 150)
plt.imshow(population, cmap='viridis', interpolation='nearest') 
plt.show()