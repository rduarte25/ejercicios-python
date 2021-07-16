#-*- coding: UTF-8 -*-
import random
'''
Created on Nov 10, 2019

@author: user
'''
from gtk.keysyms import braceleft
IMAGENES = ['''
        +---+
        |   |
            |
            |
            |
            |
            =========''',
            '''
        +---+
        |   |
        O   |
            |
            |
            |
            =========''',
            '''
        +---+
        |   |
        O   |
        |   |
            |
            |
            =========''',
            '''
        +---+
        |   |
        O   |
       /|   |
            |
            |
            =========''',            
            '''
        +---+
        |   |
        O   |
       /|\  |
            |
            |
            =========''',            
            '''
        +---+
        |   |
        O   |
       /|\  |
        |   |
            |
            =========''',                        
            '''
        +---+
        |   |
        O   |
       /|\  |
        |   |
       /    |
            =========''',                        
            '''
        +---+
        |   |
        O   |
       /|\  |
        |   |
       / \  |
            =========''',
]

WORDS = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'diputado',
    'democracia',
    'computadora',
    'teclado',
    ]

def random_word():
    idx = random.randint(0, len(WORDS) - 1)
    return WORDS[idx]

def display_board(hidden_word, tries):
    print(IMAGENES[tries])
    print('')
    print(hidden_word)
    print('---- * ---- * ---- *')
    

def run():
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0
    
    while True:
        display_board(hidden_word, tries)
        current_letter = str(raw_input('Escoge una lera: \n'))
        letter_indexes = []
        
        for i in range(len(word)):
            if word[i] == current_letter:
                letter_indexes.append(i)
        
        if len(letter_indexes) == 0:
            tries += 1
            if tries == 7:
                display_board(hidden_word, tries)
                print('')
                print('GAME OVER!!!')
                print('La palabra correcta era {}'.format(word))
                break            
        else:
            for i in letter_indexes:
                hidden_word[i] = current_letter
            
            letter_indexes = []
            
        try:
            hidden_word.index('-')
        except ValueError:
            print('')
            print('Wind')
            print('La palabra es: {}'.format(word))
            break
        
if __name__ == '__main__':
    print('Bienvenidos a Ahorcados')
    run()