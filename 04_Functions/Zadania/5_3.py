###
# Allows to enter and print employee data. Due to personal
# data protection, you can determine whether information about
# the employee's salary will be printed
#
from . import keyboard as kb

# Reads employee's data from keyboard
first_name = kb.input_string('Enter name: ')
last_name = kb.input_string('Enter last name: ')
age = kb.input_integer('Enter your age: ')
salary = kb.input_real('Enter your salary: ')
is_salary_hidden = kb.input_boolean('Hide salary? (y/n)')

# Prints employee's record
print('DATA RECORD')
print('===========')
print(f'Name: {first_name} {last_name}')
print(f"Employee is {age} years old.")
if not is_salary_hidden:
    print(f'Salary: {salary}')