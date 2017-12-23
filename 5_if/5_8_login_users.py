users = ["casey", "east4ming", "eve", "like", "admin"]
for user in users:
    if user == "admin":
        print("Hello " + user + ", would you like to see a status report?")
    else:
        print("Hello " + user + ", thank you for logging in again.")
