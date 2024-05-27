C = int(input('Input temperature in Celsius\n'))
n = input('Check "K" to Kelvin or "F" to Farad\n')

def Kelvin():
    k = round (C + 273.16, 2)
    return str(k)

def Farad():
    f = round((C+32)*(5/9), 2)
    return str(f)

if n == 'K' or n == 'k':
    print(Kelvin(), 'Kelvin')
elif n == 'F' or n == 'f':
    print(Farad(), 'Farad')
else:
    print('Not valid check')
