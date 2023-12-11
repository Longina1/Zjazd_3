def add_user(username):
    while True:
        password1 = input('Enter your password ')
        password2 = input('Repeat your password ')
        if password1 == password2:
            user_database[username] = password1
            break
        else:
            print('Passwords do not match.')


def login_successful(username):
    password = input('Enter your password ')
    if password == user_database[username]:
        print('Correct password')
        return True
    else:
        print('Incorrect password')
        return False


def username_available(username):
    username = input('Enter your username ')
    if username not in user_database:
        print('Username already in use.')
        return True
    else:
        return False

def suggest_name(name):
    return name + 1
