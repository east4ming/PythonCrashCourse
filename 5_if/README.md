# 5. `if`

- 检查是否相等: `==` 或不相等: `!=`
- 检查多个条件: `and` `or`
- 检查特定值是否在列表中: `in` 或不在: `not in`
- `if-elif-else` **依次**检查每个条件测试, 直到遇到通过了的条件测试. 测试通过, 执行紧跟其后的代码, 并跳过余下的测试.
- `if-elif` 语句块可以省略`else`.
- 要测试多个条件. 可以写多个`if`语句来判断. 如下所示:
    ```python
    requested_toppings = ["mushrooms", "extra cheese"]
    if "mushroom" in requested_toppings:
        print("Adding mushrooms.")
    if "pepperoni" in requested_toppings:
        print("Adding pepperoni.")
    if "extra cheese" in requested_toppings:
        print("Adding extra cheese.")
    print("\nFinished making your pizza!")
    ```
- 在特定情况下, 需要先判断列表是否为空. 如下所示:
    ```python
    requested_toppings = []
    if requested_toppings:
        for requested_toppings in requested_toppings:
            print("Adding " + requested_topping + ".")
        print("\nFinished making your pizza!")
    else:
        print("Are you sure you want a plain pizza?")
    ```
- 在特定情况下, 需要使用多个列表. 一个循环, 一个判断. 
    > 见 5_10_check_username.py
- PEP8建议: 在比较运算符两边各添加一个空格.
