# -*- coding: utf-8 -*-

import turtle

def main():
    window = turtle.Screen()
    dave = turtle.Turtle()

    MakeSquare(dave)

    turtle.mainloop()

def MakeSquare(dave):
    lenght = int(input('Ingresa el lado del cuadrado: '))

    for i in range(4):
        MakeLineAndTurn(dave, lenght)

def MakeLineAndTurn(dave, lenght):
    dave.forward(lenght)
    dave.left(90)

if __name__ == '__main__':
    main()
