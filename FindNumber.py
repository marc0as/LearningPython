# -*- coding: utf-8 -*- 

import random

def FindNumber(Inf, Sup):
    Found = False
    random_number = random.randint(Inf, Sup+1)

    while not Found:
        Number = int(input('Intenta un número: '))

        if Number == random_number:
            print('Felicidades, Encontraste el número')
            Found = True
        elif Number > random_number:
            print('Menos')
        else:
            print('Más')


if __name__ == '__main__':

    print('Encuentra el número')

    LimInf = int(input('Ingresa el límite inferior: '))
    LimSup = int(input('Ingresa el límite superior: '))
    
    FindNumber(LimInf, LimSup)
