from Plik import *

if not username_available(username):
    print('User identified')
    if login_successful(username):
        print('Programm continues')
    else:
        exit()
else:
    add_user(username)
print(user_database)
