"""
    This problem was recently asked by Google.

    Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

    For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

    Bonus: Can you do this in one pass?
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

