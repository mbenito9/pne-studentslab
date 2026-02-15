student = {
    "name": "Carlos",
    "age": 22,
    "subjects": ["PNE", "Networks", "Databases"],
    "grades": {"PNE": 8.5, "Networks": 7.0, "Databases": 9.2}
}

name = student["name"]
subjects = student["subjects"]
dict_gr = student["grades"]
grade_db = dict_gr["Databases"]

if "PNE" in subjects:
    pne = True
else:
    pne = False

print(f"Name: {name}")
print(f"Number of subjects: {len(subjects)}")
print(f"Enrollment in PNE: {pne}")
print(f"Database grade: {grade_db}")

sum = 0
total = 0
for key, value in dict_gr.items():
    print(f"{key} = {value}")
    sum += value
    total += 1
average = round(sum / total, 2)

print(f"Average grade: {average}")

