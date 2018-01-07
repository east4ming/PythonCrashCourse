import json

filepath = r'e:\WorkSpace\PythonCrashCourse\10_files_exceptions\username.json'

with open(filepath) as f_obj:
    username = json.load(f_obj)
    print('Welcome back, {}!'.format(username))
