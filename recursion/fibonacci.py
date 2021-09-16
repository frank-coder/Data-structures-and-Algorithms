"""
    This function calculates the fibonacci
    sequence for a given number n
"""
def fibonacci(n):
    assert n >= 0 and int(n) == n,"Fibonacci cannot be negative or non integer "
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# Calling with wrong input
print("--- First test with positive int ---")
print(fibonacci(10))
print("---Second test with 0---")
print(fibonacci(0))
print("---Third test with negative int---")
print(fibonacci(-5))

