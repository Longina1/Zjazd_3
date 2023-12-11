special_characters = set(',./\':;[]')
print(special_characters)

password = input('Enter your password: ')
if len(set(password) & special_characters) > 0:
    print('A special character has been used')
else:
    print('No special character')
