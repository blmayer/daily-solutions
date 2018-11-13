"""
    This problem was asked by Uber.

    Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

    For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

    Follow-up: what if you can't use division?
"""

# Get input
array = input("Enter a list of space separated numbers:\n")

# Tranform array into an array
array = [int(x) for x in array.split(" ")]

# Give expected return
prod = 1
for i in array:
    prod = prod*i

print([int(prod/x) if x !=0 else 0 for x in array])
