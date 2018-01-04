import user

class Privileges():
    """Privileges."""
    def __init__(self, privileges):
        self.privileges = privileges
    def show_privileges(self):
        print('The user has these privileges: ')
        for privilege in self.privileges:
            print('- {}'.format(privilege))    


class Admin(user.User):
    """Admin."""
    def __init__(self, first_name, last_name, description):
        super().__init__(first_name, last_name, description)
        self.privileges = Privileges(['can add post', 'can delete post', 'can ban user'])
