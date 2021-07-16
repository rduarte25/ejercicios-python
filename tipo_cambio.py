#-*-coding: UTF-8 -*-

def run ():
    print('Calculadora de Divisas')
    print('Convierte pesos Mexica a Colombianos')
    print('')

    ammount = float( raw_input('Ingresa la cantidad: \n'))

    result = foreign_exchangeCalculator(ammount)

    print('${} pesos mexicanos son ${} pesos colombianos'.format(ammount, result))

def foreign_exchangeCalculator(ammount):
    mexColRate = 145.97
    return mexColRate * ammount


if __name__ == '__main__':
    run()