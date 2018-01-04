"""Admin.

继承 User 类. 添加一个 privileges 的属性, 用于存储由字符串组成的列表.
编写一个名为 show_privileges() 的方法, 显示管理员权限.
创建一个 Admin 实例, 并调用该方法.
"""

class User():
    """User."""
    def __init__(self, first_name, last_name, description):
        """Init User."""
        self.first_name = first_name
        self.last_name = last_name
        self.description = description
    
    def describe_user(self):
        """Print User Info."""
        print('The User Info: ')
        print('- first name: {}'.format(self.first_name))
        print('- last name: {}'.format(self.last_name))
        print('- description: {}'.format(self.description))
    
    def greet_user(self):
        """Greet User."""
        print('Good Morning, {}'.format(self.first_name))


class Admin(User):
    """Admin."""
    def __init__(self, first_name, last_name, description, privileges):
        super().__init__(first_name, last_name, description)
        self.privileges = privileges
    def show_privileges(self):
        print('The Admin User has these privileges: ')
        for privilege in self.privileges:
            print('- {}'.format(privilege))

admin = Admin('Casey', 'Tsui', 'The Admin User', ['can add post', 'can delete post', 'can ban user'])
admin.show_privileges()
admin.describe_user()
admin.greet_user()
