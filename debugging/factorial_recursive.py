#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of a non-negative integer.

    The factorial of a number n, denoted as n!, is the product of all positive
    integers less than or equal to n. For example, 5! = 5 * 4 * 3 * 2 * 1 = 120.
    The factorial of 0 is defined as 1.

    Parameters:
    n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
    int: The factorial of n (n!).
    """
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    else:
        # Recursive call to calculate factorial
        return n * factorial(n-1)

# Retrieve the argument passed in the command line and convert it to an integer
f = factorial(int(sys.argv[1]))

# Print the result of the factorial
print(f)
