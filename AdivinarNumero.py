#-*- coding: UTF-8 -*-
import random

'''
Created on Nov 10, 2019

@author: user
'''

def run():
    numberFound = False
    randomNumber = random.randint(0,20)
    while not numberFound:
        number = int( raw_input('Intenta un número\n') )
        if number == randomNumber:
            print('Felicidades encontraste el número')
            numberFound = True
        elif number > randomNumber:
            print('El número es menor')
        else:
            print('El número es mayor')
                        

if __name__ == '__main__':
    run()