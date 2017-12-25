# 7. 用户输入和while循环

## input

### 编写清晰的程序

有时候, 提示可能会超过一行. 在这种情况下, 可将提示存储在一个变量中, 再将该变量传递给函数 input().

```python
prompt = 'If you tell us who you are, we can personalize the messages you see.'
prompt += '\nWhat is your first name? '
name = input(prompt)
```

### int()来获取数值输入

使用函数 input() 时, Python将用户输入解读为**字符串**. `age = int(input("How old are you?"))`

> **Python 2.7** 
> `raw_input()`

## while 循环简介

```python
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
```

在while循环中定义一个退出值, 只要用户输入的不是这个值, 程序就接着运行.

```python
prompt = '\nTell me something, and I will repeat it back to you:'
prompt +='\nEnter "quit" to end the program.\n'
message = ''
while message != 'quit':
    message = input(prompt)
    print(message)
```

上个例子有个小问题, 会将单词'quit'也打印出来. 修复如下:

```python
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
```

### 使用标志

在复杂程序中, 很多不同的事件都会导致程序停止运行. 在这种情况下, 可以定义一个变量, 用于判断整个程序是否处于活动状态. 这个变量就是**标志**.

```python
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
```

### 使用break退出循环

```python
while True:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print(message)
```

### 在循环中使用 continue

返回循环开头, 并根据条件测试结果决定是否继续执行循环.
只打印奇数的例子:

```python
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue
    print(num)
```

## 使用 while 循环来处理列表和字典

在for循环中**不应该修改列表**. 否则将导致Python难以跟踪其中的元素.
要在遍历列表的同时对其进行修改, 可使用while循环.
通过将while循环同列表/字典结合起来使用, 可收集/存储并组织大量输入, 供以后查看和显示.

示例如下: 利用list的pop()和append().

```python
unconformed_users = ['alice', 'brian', 'candace']
conformed_users = []
while unconformed_users:
    current_user = unconformed_users.pop()
    print('Verifying user: {}'.format(current_user.title()))
    conformed_users.append(current_user)
print('\nThe following users have been confirmed: ')
for conformed_user in conformed_users:
    print('\t{}'.format(conformed_user.title()))
```

### 删除包含特定值的所有列表元素

使用列表的remove()

```python
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
print(pets.count('cat'))
while 'cat' in pets:
    pets.remove('cat')
print(pets)
```

### 使用用户输入来填充字典

```python
responses = {}

polling_active = True

while polling_active:
    name = input('\nWhat\'s your name? ')
    response = input('Which mountain would you like to climb someday? ')

    responses[name] = response

    repeat = input('Would you like to let another person respond? (yes/no) ')
    if repeat == 'no':
        polling_active = False

print('\n--- Poll Results ---')
for name, response in responses.items():
    print('{} would like to climb {}.'.format(name, response))
```
