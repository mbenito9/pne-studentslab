def limit_val(lst):
    min = lst[1]
    max = 0
    for i in lst:
        if i > max:
            max = i
        elif i < min:
            min = i
    return max, min

def average(lst):
    total = 0
    count = 0
    for i in lst:
        total += i
        count += 1
    return round(total / count, 1)
if __name__ == "__main__":
    temperatures = [15.5, 17.2, 14.8, 16.0, 18.3, 20.1, 19.5]
    for i in temperatures:
        index = temperatures.index(i)
        if index == 2:
            print("Temperature on Wednesday:", i)
    max, min = limit_val(temperatures)
    print(f"Maximum value: {max}; Minimum value: {min}")
    print(f"Average temperature:", average(temperatures))
    days = 0
    for j in temperatures:
        if j > 17:
            days += 1
    print("Days with temp > 17:", days)
    temperatures.sort()
    print(temperatures)