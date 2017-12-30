"""User.

添加一个 login_attempts 的属性.
编写一个 increment_login_attempts() 方法, 将 login_attempts + 1
编写一个 reset_login_attempts() 方法, 将 login_attempts = 0
包含属性 first_name 和 last_name , 还有用户简介: 会存储其他属性.
定义一个 describe_user() 的方法, 打印用户信息;
定义一个 greet_user() 的方法, 发出问候.
"""


class User():
    """User."""
    def __init__(self, first_name, last_name, description):
        """Init User."""
        self.first_name = first_name
        self.last_name = last_name
        self.description = description
        self.login_attempts = 0
    
    def describe_user(self):
        """Print User Info."""
        print('The User Info: ')
        print('- first name: {}'.format(self.first_name))
        print('- last name: {}'.format(self.last_name))
        print('- description: {}'.format(self.description))
    
    def greet_user(self):
        """Greet User."""
        print('Good Morning, {}'.format(self.first_name))

    def increment_login_attempts(self):
        """ +1."""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """ = 0."""
        self.login_attempts = 0

user_0 = User('zhao', 'yi', 'Song Dynasty Master.')
# user_1 = User('SUn', 'er', 'Sun Wukong\'s another body.')
# user_2 = User('Qian', 'Er', 'Mr Money')
# user_0.describe_user()
# user_0.greet_user()
# user_1.describe_user()
# user_1.greet_user()
# user_2.describe_user()
# user_2.greet_user()
user_0.increment_login_attempts()
user_0.increment_login_attempts()
user_0.increment_login_attempts()
print(user_0.login_attempts)
user_0.reset_login_attempts()
print(user_0.login_attempts)
