# -*- coding utf-8 -*-

def IsPrime(Number):
    if Number < 2:
        return False
    elif Number == 2:
        return True
    elif Number > 2 and Number % 2 ==0:
        return False
    else:
        for i in range(3, Number):
            if Number % i ==0:
                return False
        return True

def run():
    Number = int(input('Ingresa un número: '))

    result = IsPrime(Number)

    if result == True:
        print('El {} es primo'.format(Number))
    else:
        print('El {} NO es primo'.format(Number))
    

if __name__ == '__main__':
    run()
