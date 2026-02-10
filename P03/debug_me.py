# --- Find the error!


def g(a, b):
    return a - b


def f(a, b, c, d):
    t0 = a + b - g(a, 0)
    t1 = g(c, d)
    t3 = 2 * (t0 / t1)
    return t0 + 2*t1 + t3*t3


# -- Main program
print("Result 1: ", f(5, 2, 5, 0))
#print("Result 2: ", f(0, 2, 3, 3))
print("Result 3: ", f(1, 3, 2, 3))
print("Result 4: ", f(1, 9, 22.0, 3))


#The error is located in line11. Is of ZerodivisionError, and it is caused when the value t1 is 0.
#This will happen any time parameters c and d of function f are the same.