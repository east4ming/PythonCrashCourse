"""Pizza Toppings.

编写一个循环, 提示用户输入一系列的披萨配料. 并打印出来.
并在用户输入"quit"时结束循环.
"""

# Total 3 projects.
# 1. 直接判断输入
pizza_topping = ''
while pizza_topping != 'quit':
    pizza_topping = input('Please input the pizza topping: ')
    if pizza_topping != 'quit':
        print('We will add this topping:{} to the pizza.'.format(pizza_topping))

# 2. 使用Break
while True:
    pizza_topping = input('Please input the pizza topping: ')
    if pizza_topping == 'quit':
        break
    else:
        print('We will add this topping:{} to the pizza.'.format(pizza_topping))

# 3. 标志
flag = True
while flag:
    pizza_topping = input('Please input the pizza topping: ')
    if pizza_topping == 'quit':
        flag = False
    else:
        print('We will add this topping:{} to the pizza.'.format(pizza_topping))
