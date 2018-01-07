"""Cats and Dogs.

创建2个文件 cats.txt dogs.txt , 在第一个文件中至少存储三只猫的名字, 第二个是至少三条狗的名字.
读取这些文件, 并将其内容打印到屏幕. 文件不存在时, 捕获 FileNotFound 错误, 并打印消息.
"""

def read_print(filename):
    try:
        with open(filename) as f_obj:
            lines = f_obj.readlines()
    except FileNotFoundError:
        # print('The file {} does not exist.'.format(filename))
        pass
    else:
        for line in lines:
            print(line)

dir = r"""e:\WorkSpace\PythonCrashCourse\10_files_exceptions"""
filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    f_path = dir + '\\' + filename
    read_print(f_path)
