class Employee():
    """Employee class.
    
    接受名/姓/年薪, 存储在属性中
    方法: give_raise() 默认年薪增加 5000美元, 也能增加其他数值
    """
    
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
    def give_raise(self, inc_salary=5000):
        self.salary += inc_salary
