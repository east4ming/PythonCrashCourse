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
