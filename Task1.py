student_marks = {
    'Alice' : 85,
    'Bob' : 90,
    'Charlie' : 78,
    'David' : 92,
    'Eve' : 88
}

user_input = input("Enter a student name: ").capitalize()
if user_input in student_marks:
    print(f"{user_input}'s marks : {student_marks[user_input]}")
else:
    print("Student not found")


