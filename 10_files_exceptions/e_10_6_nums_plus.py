"""Nums Plus.

提示用户输入两个数字, 并相加打印结果.
用户输入不是数字, 捕获 ValueError 异常, 并打印错误消息.
"""

print('Give me two numbers, and I will plus them.')
print('Enter "q" to quit.')

while True:
    first_num = input('Please input first number: ')
    if first_num == 'q':
        break
    second_num = input('Please input second number: ')
    if second_num == 'q':
        break
    try:
        f_num = float(first_num)
        s_num = float(second_num)
    except ValueError:
        print('You input a non-number, please input a number!')
    else:
        s = f_num + s_num
        print(s)
