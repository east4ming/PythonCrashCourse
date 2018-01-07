filename = r"""e:\WorkSpace\PythonCrashCourse\10_files_exceptions\alice.txt"""

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = 'Sorry, the file {} does not exist.'.format(filename)
else:
    # 计算文件大致包含多少个单词
    # words 为所有单个单词组成的一个列表
    words = contents.split()
    num_words = len(words)
    print('The file <{}> has about {} words.'.format(filename, num_words))
