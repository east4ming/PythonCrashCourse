"""Great Magicians.

创建一个魔术师名字的列表, 并打印.
修改该列表, 都加上"the Great"前缀.
"""
def show_magicians(magicians):
    """Magicians list print."""
    for magician in magicians:
        print(magician)

def make_great(magicians, great_magicians):
    """Make Great Magicians."""
    for magician in magicians:
        great_magicians.append('the Great ' + magician)

magicians = ['zhaoyi', 'qianer', 'sunsan', 'lisi']
great_magicians = []
make_great(magicians, great_magicians)
show_magicians(great_magicians)
