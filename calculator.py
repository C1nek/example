def plus(x, y):
    return x + y

def minus(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        print('Division on 0 not correct!')
    else:
        return x / y

def result(x, y, act):
    if act == '+':
        return plus(x,y)
    elif act == '-':
        return minus(x,y)
    elif act == '*':
        return multiplication(x,y)
    elif act == '/':
        return division(x,y)
    else: print('Not correct action (+,-,*,/)')

x = int(input('Enter first number\n'))
y = int(input('Enter second number\n'))
act = input('Enter action of numbers\n')

print('result = ', result(x, y, act))
