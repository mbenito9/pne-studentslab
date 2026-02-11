text = "  Hello, World! Welcome to Python Programming.  "

new = text.strip()
print("Stripped text:", new)
lst_w = new.split(" ")
count = 0
for i in lst_w:
    count += 1
print("Total number of words:", count)
print("Capitalized string:", new.title())
print(new.startswith("Hello"))
print(new.endswith("ing."))
print("Index:", new.find("Python"))
print(" - ".join(lst_w))

