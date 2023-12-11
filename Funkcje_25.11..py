def welcome():
    print('.....................')
    print('Welcome to the meeting')
    print('File with logs updated')


def customised_welcome1(name):
    print('Welcome ', name)
    print(f'Welcome {name}')

while True:
    decision = input('Shall the welcome phrase be used? Y/N ')
    if decision.lower() == 'y':
        welcome()
    else:
        print('No welcome phrase')
        break


name = input('Enter your name ')
customised_welcome1(name)
print('................')
customised_welcome1('Nina')


