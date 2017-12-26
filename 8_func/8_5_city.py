"""Describe City.

一个函数, 接收城市的名字和所属国家. 
并打印一个简单的句子, 如: 钓鱼岛在中国. 
国家的形参有默认值. 
为三座城市调用该函数, 且有一座不是默认国家. 
"""

def describe_city(name, country='China'):
    """Describe City."""
    print('{} is in {}.'.format(name, country))

describe_city('Fishing Island')
describe_city('Shanghai')
describe_city('New York', 'USA')
