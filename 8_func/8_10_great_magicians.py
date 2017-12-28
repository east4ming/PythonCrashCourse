"""Great Magicians.

创建一个魔术师名字的列表, 并打印.
修改该列表, 都加上"the Great"前缀.
"""
def show_magicians(magicians):
    """Magicians list print."""
    for magician in magicians:
        print(magician)

def make_great(magicians):
    """Make Great Magicians."""
    length = len(magicians)
    for i in range(length):
        magicians[i] = 'the Great ' + magicians[i]

magicians = ['zhaoyi', 'qianer', 'sunsan', 'lisi']
make_great(magicians)
show_magicians(magicians)
