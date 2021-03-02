"""
Problem 1

Multiple of x and y under z

Sample Question:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def multipleOfTwoNums(x=3, y=5, max_value=100):
    
    sum = 0
    
    for i in range(max_value):
        if((i % x == 0) & (i % (x * y) != 0)):
            sum += i

    for i in range(max_value):
        if((i % y == 0) & (i % (x * y) != 0)):
            sum += i

    xy_range = max_value // (x * y)
    for i in range(xy_range):
        if (x * y * (i+1) < max_value):
            sum += x * y * (i+1)

    return(sum)

print(multipleOfTwoNums(x=3, y=5, max_value=1000))

