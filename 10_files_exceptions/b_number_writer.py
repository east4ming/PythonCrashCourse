import json

numbers = [2, 3, 5, 6, 8, 7658, 34]
filepath = r'e:\WorkSpace\PythonCrashCourse\10_files_exceptions\numbers.json'
with open(filepath, 'w') as f_obj:
    json.dump(numbers, f_obj)
