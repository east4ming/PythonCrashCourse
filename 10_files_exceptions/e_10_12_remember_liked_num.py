"""Remember Liked Nums.

将上个程序的两个函数合二为一.
如果存储了, 就显示;
否则提示用户输入, 并存储.
"""

import json

filepath = r'e:\WorkSpace\PythonCrashCourse\10_files_exceptions\favorite_num.json'

def store_like_num(filepath):
    """用户输入数字, 并存储."""
    num = input('Please input your favorite num: ')
    with open(filepath, 'w') as f_obj:
        json.dump(num, f_obj)

def read_like_num(filepath):
    """从文件中读取并打印该num."""
    try:
        with open(filepath) as f_obj:
            favorite_num = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return favorite_num


favorite_num = read_like_num(filepath)
if favorite_num:
    print('Your favorite num is: {}'.format(favorite_num))
else:
    store_like_num(filepath)
