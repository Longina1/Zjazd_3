from Plik_z_definicjami import*


new_user = input('Podaj nazwe uzytkownika: ')
if not username_available(new_user):
    print('Użytkownik rozpoznany')
    if login_successful(new_user):
        print('dalsza czesc programu')
    else:
        exit()
else:
    add_user(new_user)
print(users_database)
