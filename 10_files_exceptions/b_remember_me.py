import json

# 如果以前存储了用户名, 就加载它
# 否则, 就提示用户输入用户名并存储
filepath = r'e:\WorkSpace\PythonCrashCourse\10_files_exceptions\username.json'
try:
    with open(filepath) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input('What is your name? ')
    with open(filepath, 'w') as f_obj:
        json.dump(username, f_obj)
        print('We will remember you when you come back, {}!'.format(username))        
else:
    print('Welcome back, {}!'.format(username))
