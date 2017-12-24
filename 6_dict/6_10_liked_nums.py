"""Liked Nums

修改6-2的程序, 让每个人都有多个喜欢的数字. 
然后将每个人的名字及其喜欢的数字打印出来.
"""

liked_nums = {
    'yangxin': [2, 3],
    'yaoyanping': [9, 10],
    'cuikaidong': [2, 4],
    'lihaoyu': [3,],
    'liqiang': [8, 9, 10],
}
for name, nums in liked_nums.items():
    print('{} likes these nums: '.format(name.title()))
    for num in nums:
        print('\t{}'.format(num), end='\t')
    print()
