#-*- coding: UTF-8 -*-

def factorial(number):
    if number == 0:
        return 1
        
    return number * factorial(number -1)
        
    
    
if __name__ == '__main__':
    number = int(raw_input('Ingresa el número'))
    
    result = factorial(number)
    print(result)