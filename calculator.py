def plus(x, y):
    return x + y


def minus(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    if y == 0:
        print('Division on 0 not correct!')
        return 0
    else:
        return x / y


def result(x, y, act):
    if act == '+':
        return plus(x, y)
    elif act == '-':
        return minus(x, y)
    elif act == '*':
        return multiplication(x, y)
    elif act == '/':
        return division(x, y)
    else:
        print('Not correct action (+,-,*,/)')


def check_digit(_):
    if _.isdigit() is not True:
        return 1


def check_act(_):
    ch_a = ["+", "-", "*", "/"]
    for n in ch_a:
        if n != _:
            continue
        else:
            return _


data = {'x': 'Enter first number\n', 'y': 'Enter second number\n',
        'act': 'Enter action\n'}

for _ in data:

    temp = input(data[_])

    if data[_] == 'Enter action\n':

        while check_act(temp) == None:
            print('Not correct action (only +,-,*,/)\n')
            temp = input(data[_])

    else:
        while check_digit(temp) == 1:
            print('Need only number!\n')
            temp = input(data[_])

    data[_] = temp

print('Result = ', round(result(int(data['x']), int(data['y']), data['act']), 2))
