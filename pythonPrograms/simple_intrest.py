p = int(input("Enter principle"))
r = int(input("Enter rate"))
t = int(input("Enter time"))
simple_intrest = (p * r * t) / 100
print(simple_intrest)


# function method

def SimpleIntrest(p, r, t):
    ("The principle is: ", p)
    ("The rate is: ", r)
    ("The time is: ", t)
    si = (p * r * t) / 100
    return si


print(SimpleIntrest(2, 4, 5))
