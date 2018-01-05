file_dir = 'c:/Users/8000619804/WorkSpace/PythonCrashCourse/10_files_exceptions/pi_million_digits.txt'

with open(file_dir) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input('Enter your birthday, inthe form mmddyy: ')
if birthday in pi_string:
    print('Your birthday appers in the first million digits of pi!')
else:
    print('Your birthday does not appear in the first million digits of pi.')
