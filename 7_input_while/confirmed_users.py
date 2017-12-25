unconformed_users = ['alice', 'brian', 'candace']
conformed_users = []
while unconformed_users:
    current_user = unconformed_users.pop()
    print('Verifying user: {}'.format(current_user.title()))
    conformed_users.append(current_user)
print('\nThe following users have been confirmed: ')
for conformed_user in conformed_users:
    print('\t{}'.format(conformed_user.title()))
