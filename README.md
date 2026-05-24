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
 numbers = list(range(1, 11))
 It generates a list named numbers containing integers from 1 to 10 using range(1, 11).
 first_five = numbers[:5]
 It uses numbers[:5] to create a new list, first_five, containing the first five elements [1, 2, 3, 4, 5].
 reversed_list = first_five[::-1]
  It uses the step-based slice [::-1] to create reversed_list, which flips the order of those first five elements to [5,  4, 3, 2, 1].
