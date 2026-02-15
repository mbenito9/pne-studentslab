def average(lst):
    total = 0
    sum = 0
    for i in lst:
        sum += i
        total += 1
    return round(sum / total, 1)

def get_status(avg):
    if avg >= 5.0:
        result = "PASS"
    else:
        result = "FAILED"
    return result

if __name__ == "__main__":
    students = [
        {"name": "Ana", "grades": [8.5, 7.0, 9.0]},
        {"name": "Luis", "grades": [5.0, 4.5, 6.0]},
        {"name": "Maria", "grades": [9.5, 9.0, 10.0]},
        {"name": "Pedro", "grades": [3.0, 4.0, 2.5]},
        {"name": "Sofia", "grades": [7.0, 7.5, 8.0]},
    ]

    pas = 0
    fail = 0
    for i in students:
        name = i["name"]
        grades = i["grades"]
        ave = average(grades)
        status = get_status(ave)
        print(f"{name}: {ave} -> {status}")
        if status == "FAILED":
            fail += 1
        else:
            pas += 1
    print(f"Results: {pas} passed, {fail} failed")
