# use n to calculate number of dots. Originally n is 0
n = 0
# i is the ith triangle
# for every triangle, calculate the triangular number
for i in range (1,11):
    # n is the (i-1)th triangular number
    # for the ith triange, thr triangular number will increase n
    n = n + i
    # print the result for every triangular number
    print("When n=", i, "the triangular number is", n)