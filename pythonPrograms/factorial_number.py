# recursion method
def factorial_number(a):
    return 1 if (a == 1 or a == 0) else a * factorial_number(a - 1)


print(factorial_number(5))
