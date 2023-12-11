#spis użytkowników i haseł
#dodawanie użytkownika do bazy
#sprawdzanie, czy username jest dostępne
#if username not available, propozycja włąsnej nazyw




def add_user(username):
    while True:
        password1 = input('Enter your password ')
        password2 = input('Repeat your password ')
        if password1 == password2:
            user_database[new_user] = password1
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
        print('Username available.')
        return True
    else:
        return False

user_database = {
    'Kamil': '123',
    'Oliwia': 'Oliwia123',
    'Patryk': 'Pat1'
}

new_user = input('Enter your username ')
#password1 = input('Enter your password ')
#password2 = input('Repeat your password ')



if username_available(new_user):
    add_user(new_user)
else:
    print('Username already in use.')
    if login_successful(new_user):
        print('Program continues')
    else:
        exit()

print(user_database)
