"""T-Shirt.

接收一个尺码以及要印到 tshirt 上的字样;
打印一个句子, 说明以上信息.
"""

def tshirt(size='L', font='I love Python'):
    """Display T-Shirt Size and Font."""
    print('The T-Shirt\'s size is {}, and its font is "{}".'.format(size, font))

# 大号默认字样
tshirt()
# 中号默认字样
tshirt('M')
# 其他字样, 大小无关紧要
tshirt(font='I don\'t repair computer!')
