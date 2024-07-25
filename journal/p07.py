student_marks = {
    "Rahul": 95,
    "Priya": 97,
    "Abhishek": 93,
    "Tanya": 83,
    "Sunita": 99,
    "Ram": 98,
    "Priyanka": 96
}

for i in range(3):
    name = input("Enter student name: ")
    marks = int(input("Enter student marks: "))

    student_marks[name] = marks

student_marks.pop("Tanya")
student_marks["Ram"] = 94

best = (None, 0)
worst = (None, 100)
failed = 0

for name, marks in student_marks.items():
    if marks >= 75:
        print(name, marks, sep=": ")
    if marks < 40:
        failed += 1
    if marks > best[1]:
        best = (name, marks)
    if marks < worst[1]:
        worst = (name, marks)

print("Highest:", best)
print("Lowest:", worst)
