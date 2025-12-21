"""Task 1: Dictionary of Student Marks
Creating a dictionary with student names and marks"""
student_marks = {
    "Amit": 85,
    "Riya": 92,
    "Karan": 78,
    "Neha": 88
}
# Taking input from user
name = input("Enter student name: ")
# Retrieving and displaying marks
if name in student_marks:
    print(f"Marks of {name}: {student_marks[name]}")
else:
    print("Student not found in the dictionary.")