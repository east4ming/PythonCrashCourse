"""Sandwich.

接受顾客要在三明治中添加的一系列食材.
只有一个形参, 并打印一条消息.
"""
def sandwich(*foods):
    """接受一系列食材并打印."""
    print('\nThe sandwitch contains: ')
    for food in foods:
        print('- {}'.format(food))

sandwich('chicken', 'lettuce', 'cheese')
sandwich('beef', 'tomato', 'sweet chili sauce')
sandwich('pork', 'cuke', 'salad dressing')
