run = True

users = []

while run:
    command = input("command >> ")

    if command == "exit":
        run = False
    
    if command == "new user":
        name = input("Nome: ")
        users.append(name)

    if command == "list users":
        for user in users:
            print(user)
    
    if command == "show user":
        index = int(input("Index: "))
        print(users[index])