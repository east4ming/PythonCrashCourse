file_dir = 'c:/Users/8000619804/WorkSpace/PythonCrashCourse/10_files_exceptions/pi_digits.txt'
with open(file_dir) as file_object:
    for line in file_object:
        print(line.rstrip())
