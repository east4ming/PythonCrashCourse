import json

filepath = r'e:\WorkSpace\PythonCrashCourse\10_files_exceptions\numbers.json'
with open(filepath) as f_obj:
    numbers = json.load(f_obj)

print(numbers)
