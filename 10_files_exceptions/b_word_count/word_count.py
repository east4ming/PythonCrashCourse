def count_words(filename):
    """计算一个文件大致包含多少个单词."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = 'Sorry, the file "{}" does not exist.'.format(filename)
        print(msg)
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print('The file "{}" has about {} words.'.format(filename, num_words))

# filename = r'e:\WorkSpace\PythonCrashCourse\10_files_exceptions\alice.txt'
# count_words(filename)

dir = r'e:\WorkSpace\PythonCrashCourse\10_files_exceptions'
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    filepath = dir + '\\' + filename
    count_words(filepath)
