import json

FILEPATH = r'e:\WorkSpace\PythonCrashCourse\10_files_exceptions\username.json'

def get_stored_username():
    """如果存储了用户名, 就获取它."""
    try:
        with open(FILEPATH) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """提示用户输入用户名."""
    username = input('What is your name? ')
    with open(FILEPATH, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def verify_username(username):
    """Verify Username."""
    print('Are you {}?'.format(username))
    results = input('Please reply "y" or "n": ')
    if results == 'y':
        return True
    else:
        return False

def greet_user():
    """问候用户, 并指出其名字."""
    username = get_stored_username()
    if username and verify_username(username):
        print('Welcome back, {}!'.format(username))
    else:
        username = get_new_username()
        print('We will remember you when you come back, {}!'.format(username))    

greet_user()
