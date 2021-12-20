"""
    Function for exponentiation using recursion
"""
def power(base,exp):
    assert exp >= 0 and int(exp)== exp,"Exponent cannot be non integer"
    if exp == 0:
        return 0
    if exp == 1:
        return base
    else:
        return base * power(base, exp-1)

print("-- First test case --")
print(power(2,5))
print("-- Second test case --")
print(power(0,5))
print("-- Third test case --")
print(power(-2,2))
print("-- Fourth test case --")
print(power(2,1.2))