# 类

## 创建和使用类

### 创建Dog类

#### __init__()

形参`self`必不可少, 还必须位于其他形参的前面.
python在调用`__init()`方法来创建实例时, 将自动传入实参self.
每个与类相关联的方法调用都自动传递实参self, 它是指向**实例**本身的引用, 让实例能够访问类中的**属性和方法**.
创建Dog实例时, 通过实参向Dog()传递名字和年龄, self会自动传递. 
`self.name = name`获取存储在形参name中的值, 并将其储存在变量name中, 然后该变量被关联到当前创建的实例.
通过实例访问的变量称为*属性*

> Python 2.7中类的定义:
> ```python
> class ClassName(object):
> ```

### 根据类创建实例

```python
my_dog = Dog('willie', 6)
print("My dog's name is {}.".format(my_dog.name.title()))
print("My dog is {} years old.".format(my_dog.age))
```

#### 访问属性

句点表示法: `my_dog.name`

#### 调用方法

```python
my_dog.sit()
my_dog.roll_over()
```

### 修改属性值

三种方法:

- 直接修改
- 通过方法修改属性值
- 通过方法对属性值进行递增
