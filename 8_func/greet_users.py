def greet_users(names):
    """向列表中的每位用户都发出问候."""
    for name in names:
        msg = 'Hello, ' + name.title() + '!'
        print(msg)

usernames = ['hahaa', 'ty', 'magrot']
greet_users(usernames)
