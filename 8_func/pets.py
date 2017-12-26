def describe_pet(animal_type, pet_name):
    """Describe Pet's Info."""
    print('I have a {0}.\nMy {0}\'s name is {1}.'.format(animal_type, pet_name.title()))

# 位置实参
describe_pet('hamster', 'harry')
# 关键字实参
describe_pet(pet_name='harry', animal_type='hamster')
# 默认值
def describe_pet_1(pet_name, animal_type='dog'):
    """Describe Pet's Info."""
    print('I have a {0}.\nMy {0}\'s name is {1}.'.format(animal_type, pet_name.title()))
## 调用方式1
describe_pet_1('harry')
describe_pet_1(pet_name='harry')
## 调用方式2
describe_pet_1('harry', 'hamster')
describe_pet_1(pet_name='harry', animal_type='hamster')
describe_pet_1(animal_type='hamster', pet_name='harry')

