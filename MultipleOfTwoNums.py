"""
Problem 1

Multiple of x and y under z

Sample Question:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def multipleOfTwoNums(x=3, y=5, max_value=1000):
    
    sum = []

    x_range = max_value // x
    y_range = max_value // y

    for i in range(x_range):
        if (x * (i+1) < max_value):
            sum = sum.append(x * (i+1))

    for j in range(y_range):
        if (y * (j+1) < max_value):
            sum = sum.append(y * (y+1))

    return(sum)

print(multipleOfTwoNums(x=3, y=5, max_value=1000))

