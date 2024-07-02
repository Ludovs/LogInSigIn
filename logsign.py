import json
import array

data_file = open("data.json", "r")
data = json.load(data_file)

def ask_username():
    print("Username: ")
    username = input("---> ") ##do username compatibility
    if len(username) <= 3:
        print("The username must be longer than 3 characters")
        ask_username()
    if len(username) > 20:
        print("The username must not be longer than 20 characters")
        ask_username()
    return username

def ask_password():
    print("Password: ")
    password = input("--->")
    return password

def sign_in_action():
    usrnme = ask_username()
    psswrd = ask_password()
    print("You are now signed in as "+usrnme)
    data.append([usrnme, psswrd])
    with open("data.json", "w") as file:
        json.dump(data, file)
    ask_action()

def ask_action():
    print("What would you like to do?")
    print("[S] Sign in, [L] Log in")
    action = input("---> ")

    match action.lower():
        case "s":
            sign_in_action()
        case "l":
            print("Username: ")
            username = input("---> ")
            for user in data:
                if user[0] == username:
                    print("Accessing username......")
                    print("Password: ")
                    password = input("---> ")
                    for user in range(0, len(data)-1):
                        if data[user][0] == username:
                            if data[user][1] == password:
                                print("You logged in as "+username)
                                return
                            else:
                                print("Password not correct")
                                ask_action()
                else:
                    continue
            print("Noexistent username")
            ask_action()

        case _:
            print("This action is not valid")
            ask_action()
ask_action()
