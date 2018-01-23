"""Common Words.

找一些文学作品的txt文件并分析, 分析某一个单词出现了多少次.
"""

def count_words(filepath):
    try:
        with open(filepath) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        print('Sorry, the filepath {} does not exist.'.format(filepath))
    else:
        counts = contents.lower().count('love')
        print(counts)

dir = r"""e:\WorkSpace\PythonCrashCourse\10_files_exceptions"""
filename = 'alice.txt'
filepath = dir + '\\' + filename
count_words(filepath)
