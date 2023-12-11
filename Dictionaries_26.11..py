#program, który przyjmuje i zwraca wszystkie dostępne informacje
# program przyjmuje imię i zwraca stan konta


def customer_name(customer_number):
    return names[customer_number]


def customer_balance(customer_number):
    return account_balance[customer_number]

def view_balance(customer_name):
    customer_number = names.keys(customer_name)
    return account_balance[customer_name]


names = {
    4123: 'Asia',
    1234: 'Kamil',
    8777: 'Bartosz'
}

account_balance = {
    4123: 2341,
    1234: 0,
    8777: 10000
}

print('To view your customer details enter your customer number.')
customer_number = int(input('Enter your customer number: '))
print(f'Your name recorded in the platform is {customer_name(customer_number)}.')
print(f'Your account balance is {customer_balance(customer_number)}.')

print('..........................')

print('To view your account balance enter your name.')
print('Enter your name: ')
print(f'Your account balance is: {view_balance(customer_name)}')


def view_balance(customer_name):
    customer_number = names.keys()
    return account_balance[customer_name]
