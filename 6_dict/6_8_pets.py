"""Pets


创建多个字典, 使用宠物名称命名. 包含宠物类型/主人名字. 
将这些字典存到pets的列表中. 并遍历该列表. 将宠物信息打印出来.
"""
wangcai = {
    'type': 'dog',
    'master': 'zhaoyi' 
}
xiaoqiang = {
    'type': 'roach',
    'master': 'tangbohu'
}
xiaotian = {
    'type': 'dog',
    'master': '2ndMan God'
}
pets = [wangcai, xiaoqiang, xiaotian]

for pet in pets:
    print('Pet:')
    for t, m in pet.items():
        print('\t{}: {}'.format(t.title(), m))
