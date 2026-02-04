def fibon(x):
    lst = []
    for i in range(0, x):
        if i == 0:
            lst.append(0)
        elif i == 1:
            lst.append(1)
        else:
            total = lst[(i - 2)] + lst[(i - 1)]
            lst.append(total)
    return lst[-1]

n = 0
while n < 15:
    n += 5
    print(fibon(n), end =' ')