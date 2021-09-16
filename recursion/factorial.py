#! /usr/bin/python3

"""
    Function returns the factorial of any number n
    this function utilises recursion
"""

def factorial(n):
    assert n >= 0 and int(n) == n,"Factorial cannot be negative or non integer "
    if n in [0,1]:
        return n
    else:
        return n * factorial(n-1)

print("--- First test with positive int ---")
print(factorial(4))
print("--- Second test with positive int ---")
print(factorial(0))
print("--- Third test with non int ---")
print(factorial("4"))
print("--- Fourth test with negative int ---")
print(factorial(-4))

