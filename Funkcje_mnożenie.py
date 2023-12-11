print(10 * 1.1)
print(10 * 1.1 * 10)
print(10 * 10 * 1.1)

def multiply(x, y):
    result = round(x * y)
    return result


print(multiply(100, 1.1) + 12)


def division(x, y):
    if y == 0:
        print('Division by zero. Returned valued: 1.')
        return 1
    else:
        return x / y


print(division(5,0))
