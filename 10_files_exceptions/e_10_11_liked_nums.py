"""Liked Nums.

提示用户输入喜欢的数字, 并存储到文件中(使用 json.dump() ).
从文件中读取该值, 并打印.
"""

import json

filepath = r'e:\WorkSpace\PythonCrashCourse\10_files_exceptions\favorite_num.json'

def store_like_num(filepath):
    """用户输入数字, 并存储."""
    num = input('Please input your favorite num: ')
    with open(filepath, 'w') as f_obj:
        json.dump(num, f_obj)

def print_like_num(filepath):
    """从文件中读取并打印该num."""
    try:
        with open(filepath) as f_obj:
            favorite_num = json.load(f_obj)
    except FileNotFoundError:
        pass
    else:
        print('Your favotie num is: {}'.format(favorite_num))

store_like_num(filepath)
print_like_num(filepath)
