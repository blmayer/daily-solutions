"""
    This problem was asked by Airbnb.

    Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

    For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

    Follow-up: Can you do this in O(N) time and constant space?
"""

# Get input
array = input("Input list of number (space separated):\n")
k = int(input("Input a number:\n"))

# Tranform array into an array
array = [int(x) for x in array.split(" ")]

# Give expected return
diffs = []
for n in array:
    if n in diffs:
        print("True")
        exit(0)
    else:
        diffs.append(k - n)

print("False")
exit(1)

