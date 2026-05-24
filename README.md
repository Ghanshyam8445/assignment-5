**Description of first task(1.py)**
student_marks = { 'Amit': 85, 'Riya': 92, 'Karan': 78, 'Neha': 88 }
This initializes a dictionary named student_marks. In Python, a dictionary stores data in key-value pairs. Here, the student names are the keys and their numerical marks are the values.
name = input('Enter student name: ')
The program pauses and asks the user to type a student's name, storing the text they enter inside the name variable.
if name in student_marks:
This conditional statement checks if the name the user typed exists as a key in the student_marks dictionary.
print(f'Marks of {name}: {student_marks[name]}')
If the student exists, the program accesses their specific value using student_marks[name] and prints it using an f-string for clear formatting.
else:
    print('Student not found in the dictionary.')
If the user types a name that isn't stored in the dictionary, the else block triggers, notifying the user that the student is not in the database.
**Description of Second task(2.py)**
