"""Guest.

用户输入名字.
将名字存入 guest.txt 中.
"""

with open('./10_files_exceptions/guest.txt', 'w') as file_object:
    guest = input('Please input your name: ')
    file_object.write(guest)
