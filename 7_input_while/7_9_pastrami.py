"""Pastrami.

创建一个 sandwich_orders 的列表. 再创建一个 finished_sandwiches 的空列表. 
遍历第一个列表, 并打印消息: "I made your tuna sandwich.". 并将其移动到第二个列表.
所有都完成后, 打印一条消息, 显示第二个列表的内容.

Pastrami 卖完了, 使用while 循环删除 sandwich_orders 的 pastrami.
"""

print('I\'m sorry. Pastrami sold out.\n')
sandwich_orders = ['tuna', 'pastrami', 'ham', 'pastrami', 'chicken', 'bacon', 'pastrami']
finished_sandwiches = []
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print('I made your {} sandwich.'.format(current_sandwich))
    finished_sandwiches.append(current_sandwich)
print('\nI have made these sandwiches: ')
print('\t', finished_sandwiches)
