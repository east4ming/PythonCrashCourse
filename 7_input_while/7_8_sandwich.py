"""Sandwich Orders.

创建一个 sandwich_orders 的列表. 再创建一个 finished_sandwiches 的空列表. 
遍历第一个列表, 并打印消息: "I made your tuna sandwich.". 并将其移动到第二个列表.
所有都完成后, 打印一条消息, 显示第二个列表的内容.
"""

sandwich_orders = ['tuna', 'ham', 'chicken', 'bacon']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print('I made your {} sandwich.'.format(current_sandwich))
    finished_sandwiches.append(current_sandwich)
print('I have made these sandwiches: ')
print('\t', finished_sandwiches)
