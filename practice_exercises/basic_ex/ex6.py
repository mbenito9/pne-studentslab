def is_even(n):
    ev = n % 2 == 0
    return bool(ev)

def classify_triangle(a, b, c):
    if a == b and b == c:
        result = "equilateral"
    elif a == b or a == c or b == c:
        result = "isosceles"
    elif a != b and a != c and b != c:
        result = "scalene"
    return result

if __name__ == "__main__":
    flag = True
    while flag:
        i = input("Enter a number")
        if i != "stop":
            i = float(i)
            print(f"Number: {i} = {is_even(i)}")
        else:
            print("Program finished")
            break

    tri = True
    while tri:
        i = input("Enter the three sides of a triangle")
        if i != "stop":
            div = i.split(",")
            a = float(div[0])
            b = float(div[1])
            c = float(div[2])
            print(f"Triangle : ({a}, {b}, {c}) = {classify_triangle(a,b,c)}")
        else:
            tri = False
            print("Program stopped")