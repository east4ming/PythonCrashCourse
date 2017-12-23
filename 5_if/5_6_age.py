while True:
    age = int(input("Your age: "))
    if age < 2:
        print("You are a baby.")
    elif age < 4:
        print("You are studying walking.")
    elif age < 13:
        print("You are a child.")
    elif age < 20:
        print("You are a young man.")
    elif age < 65:
        print("You are a man.")
    else:
        print("You are a old man.")
