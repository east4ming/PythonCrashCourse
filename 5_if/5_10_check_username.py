current_users_temp = ["zhaoyi", "qianer", "sunsan", "LISI", "zhouwu"]
current_users = []
for current_user in current_users_temp:
    current_users.append(current_user.lower())
print(current_users)
new_users = ["Lisi", "ZhouWu", "wuliu", "zhengqi", "wangba"]
for new_user in new_users:
    if new_user.lower() in current_users:
        print("The username \"" + new_user + "\" is already exist. Please input another username!")
    else:
        print("Congratulations! The username \"" + new_user + "\" is available.")
