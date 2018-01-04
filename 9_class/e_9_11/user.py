"""Privileges.

编写一个 Privileges 类, 有一个属性 -- privileges.
由一个方法 -- show_privileges().
在 Admin 类中, 将一个 Privileges 实例作为其属性.
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


class Privileges():
    """Privileges."""
    def __init__(self, privileges):
        self.privileges = privileges
    def show_privileges(self):
        print('The User has these privileges: ')
        for privilege in self.privileges:
            print('- {}'.format(privilege))    


class Admin(User):
    """Admin."""
    def __init__(self, first_name, last_name, description):
        super().__init__(first_name, last_name, description)
        self.privileges = Privileges(['can add post', 'can delete post', 'can ban user'])
