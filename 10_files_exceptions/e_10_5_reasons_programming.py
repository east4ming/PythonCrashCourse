"""The Reasons like programming.

while loop.
询问用户为何喜欢编程.
每当用户输入一个原因, 都将其添加到一个存储所有原因的文件中.
"""

with open('./10_files_exceptions/reasons_programming.txt', 'a') as file_object:
    while True:
        reason = input('Why do you like programming? ')
        if reason == 'q':
            break
        file_object.write('{}\n'.format(reason))
