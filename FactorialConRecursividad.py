# -*- coding utf-8 -*-

def Fact(Number):
    if Number == 0:
        return 1
    else:
        return Number * Fact(Number-1)


if __name__ == '__main__' :
    Number = int(input('Ingresa un número: '))

    Res = Fact(Number)

    print(Res)
