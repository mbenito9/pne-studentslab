lst = []
for i in range(0, 11):
    if i == 0:
        lst.append(0)
    elif i == 1:
        lst.append(1)
    else:
        total = lst[(i - 2)] + lst[(i - 1)]
        lst.append(total)
print(lst)