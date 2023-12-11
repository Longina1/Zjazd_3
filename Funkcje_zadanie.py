#wiek auta, liczba szkód, wiek kierowcy
# kwota składki

def insurance_premium (car_age, no_of_losses, driver_age):
    premium = 0
    premium += car_age * 20
    premium += no_of_losses * 200
    if driver_age < 25:
        premium += 100
 #   print(f'The insurance premium is {premium}.')
    return premium


premium = insurance_premium(10, 1, 24)

rent = 500
food = 700
cost_of_living = rent + food + premium
print(f'The cost of living is {cost_of_living} and the premium is {premium}.')
print('....................')

name = 'Oliwia'
if len(name) > 5:
    print('Your name is short')
else:
    print('Your name is short')

if insurance_premium(20, 5, 55) > 1000:
    print('You cannot afford it.')
else:
    print('The premium is acceptable.')
