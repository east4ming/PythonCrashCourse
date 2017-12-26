"""T-Shirt.

接收一个尺码以及要印到 tshirt 上的字样;
打印一个句子, 说明以上信息.
"""

def tshirt(size, font):
    """Display T-Shirt Size and Font."""
    print('The T-Shirt\'s size is {}, and its font is "{}."'.format(size, font))

tshirt('XXL', 'Life Is Short, I User Python.')
tshirt(font='I don\'t repair computer!', size='L')
