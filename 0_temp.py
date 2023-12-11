

def welcome(name, age, sex = 'f'):
    if age <=15:
        print('You are under age.')
    if age <= 20:
        print(f'Hi {name}')
    else:
        if sex = 'f':
            print(f'Dzień dobry Szanowna Pani {name}')
        else:
            print(f'Dzień dobry Szanowny Panie {name}')


username = input('Enter your name ')
age = int(input('Enter your age '))

welcome(username, age)

welcome('Nina', 20, female)


shopping_list = {
    'Carrot': 4.5,
    'Cheese': 9.99,
    'Butter': 10,
    'Butter': 13

}

print(shopping_list)


string = 'mum.dad.cat.dog'
string = string.split('.') # dzieli na listę
print(string)
