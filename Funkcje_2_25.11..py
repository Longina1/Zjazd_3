

def welcome(name, age):
    if age <= 0:
        print('Invalid age')
    elif age <= 10:
        print("You need your parent's consent first")
    elif age <= 20:
        print(f'Hi {name}')
    else:
        if name[-1] == 'a':
            print(f'Dzień dobry Szanowna Pani {name}')
        else:
            print(f'Dzień dobry Szanowny Panie {name}')


username = input('Enter your name ')
age = int(input('Enter your age '))

welcome(username, age)

welcome('Nina', 20)

   # import random
    #name_list = ['Nina', 'Ania', 'Ola']
    #welcome(name_list[1], random.randint(12, 30))


