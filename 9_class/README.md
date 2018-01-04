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

## 继承

一个类继承自另一个类时, 它将自动获得该类的所有方法和属性, 原有的类称为**父类**. 而新类称为**子类**.
子类继承父类的所有属性和方法, 同时还有自己的属性和方法. 

### 子类的 __init__()

> 见`b_electric_car.py`

### Python 2.7中的继承

```python
class Car(Object):
    pass

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super(ElectricCar, self).__init__(make, model, year):
        pass
```

### 重写父类的方法

> 见`b_electric_car.py`

### 将实例用作属性

> 见`b_electric_car_2.py`

## Python 标准库

> 有序字典: `collections.OrderedDict`
> 具体见`b_favorite_languages.py`

## 类编码风格

- 类命名: **驼峰命名法**
- 实例名和模块名都应该**小写**, 并在单词之间加上**下划线**
- 对于每个类, 都应紧跟在类定义后包含一个**文档字符串**. 简要描述类的功能, 并遵循文档字符串的格式约定.
- 每个模块也应包含一个**文档字符串**, 对其中的类可用于做什么进行描述
- 可使用**空行**组织代码, 但不要滥用. 
- 在**类**中, 可使用**一个空行**来分割**方法**.
- 在**模块**中, 使用**两个空行**来分隔**类**
- 需要同时导入**标准库**和自己编写的模块时, 先编写导入**标准库模块**的import语句, 再**添加一个空行**, 导入自己的模块.
