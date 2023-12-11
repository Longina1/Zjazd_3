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

for number in names: # gdy nazwa słownika, szuka po kluczach
    print(names[number])

for number in names:
    print(number)

for value in names.keys():
    print(key)

for value in names.values():
    print(value)

if 'Asia' in names.values():
    pass #if nie może być puste, z pass zostanie puste, ale nie będzie błędu
