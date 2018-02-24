# -*- coding: utf-8 -*-

def ForeignExchangeCalc(ammount):
    MexTColRate = 147.97

    return MexTColRate * ammount

def run():
    print('Calculadora de Divisas')
    print('Convierte de pseos mexicanos a pesos colombianos.')
    print('')

    ammount = float(input('Ingresa la cantidad de pesos mexicanos que vas a convertir: '))

    result = ForeignExchangeCalc(ammount)

    print('${} pesos mexicanos son ${} pesos colombianos'.format(ammount, result))

if __name__ == '__main__':
    run()