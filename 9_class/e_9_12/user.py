"""User.

user module.
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
