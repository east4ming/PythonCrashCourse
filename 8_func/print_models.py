def print_models(unprinted_models, completed_models):
    """
    模拟打印每个设计, 直到没有未打印的设计为止
    打印每个设计后, 都将其移动到列表 completed_models中.
    """
    while unprinted_models:
        current_model = unprinted_models.pop()
        print('Printing model: ' + current_model)
        completed_models.append(current_model)

def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print('\nThe following models have been printed:')
    for completed_model in completed_models:
        print('\t{}'.format(completed_model))

unprinted_models = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_models, completed_models)
show_completed_models(completed_models)
