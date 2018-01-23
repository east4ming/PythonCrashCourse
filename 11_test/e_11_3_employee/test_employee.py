import unittest

from employee import Employee

class TestAnonymousSurvey(unittest.TestCase):
    """针对Employee类的测试."""

    def setUp(self):
        """创建一个员工对象和一个加薪额度, 供使用的测试方法使用."""
        self.salary = 500000
        self.one_employee = Employee('casey', 'cui', self.salary)
        self.inc_salary = 300000
    
    def test_give_default_raise(self):
        """测试默认加薪额度."""
        self.one_employee.give_raise()
        self.assertEqual(self.one_employee.salary, self.salary+5000)
    
    def test_give_custom_raise(self):
        """测试自定义加薪额度."""
        self.one_employee.give_raise(self.inc_salary)
        self.assertEqual(self.one_employee.salary, self.salary+self.inc_salary)

unittest.main()
