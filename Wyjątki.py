while True:
    try:
        age = int(input('Enter your age '))
        x = 5 / 0
        break
    except ValueError:
        print('Use the correct number format')
    except ZeroDivisionError:
        x = 0
        break
print(f'You will retire in {65 - age} years.')
