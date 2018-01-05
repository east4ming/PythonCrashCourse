file_dir = 'c:/Users/8000619804/WorkSpace/PythonCrashCourse/10_files_exceptions/learning_python.txt'

print('First :')
with open(file_dir) as file_object:
    contents = file_object.read()
    print(contents)

print('Second :')
with open(file_dir) as file_object:
    for line in file_object:
        print(line)

print('Third :')
with open(file_dir) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line)
