"""Guest Book.

while loop. 提示用户输入名字.
输入名字后在屏幕打印问候语, 并将访问记录添加到 guest_book.txt 中.
确保每个记录占一行.
"""

with open('./10_files_exceptions/guest_book.txt', 'a') as file_object:
    while True:
        guest = input('Please input your name: ')
        if guest == 'q':
            break
        file_object.write('{}\n'.format(guest))
