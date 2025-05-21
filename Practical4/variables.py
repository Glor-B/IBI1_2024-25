# a is time for woal to the bus stop
a = 15
# b is time for bus journey
b = 75
# c is the total time for walking to the office
c = a + b
# d is time for driving to office
d = 90
# e is time for walking to car park
e = 5
# f is the total time for driving to the office
f = d + e

if c > f:
    print('Walking + bus is lower')
elif c == f:
    print('The two methods cost the same amount of time')
else:
    print("Bus only is faster.")
# c < f, so walking to office is slightly faster.

X1 = True
Y1 = True
W1 = X1 and Y1
print(W1)

X2 = True
Y2 = False
W2 = X2 and Y2
print(W2)

X3 = False
Y3 = False
W3 = X3 and Y3
print(W3)

X4 = False
Y4 = True
W4 = X4 and Y4
print(W4)

# If X is True and Y is True, W is True.
# If X is True and Y is False, W is False.
# If X is False and Y is True, W is False.
# If X is False and Y is False, W is False.