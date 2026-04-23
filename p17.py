# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 12:25:36 2026

@author: Christian Bahamon
"""

#Illinois lottery
import random 


def displaymenu():
    print(' '*10,' select action ')
    print(' '*2,'---------------------------')
    print (' '*10,'1  Powerball')
    print (' '*10,'2  Mega Millions')
    print (' '*10,'3  Lucky Day Lotto')
    print (' '*10,'4  Lotto')    
    print(' ')
    print (' '*10,'9   Quit\n')
    return


def powerball():
    random_list = []
    while len(random_list) < 5:
        num = random.randint(1,69)
        if num not in random_list:
            random_list.append(num)

    print('Powerball', '\n' * 2, random_list)
    input('Hit Enter Key to return to menu...')
    print('\n' * 2)
    menu()

def megamillions():
    random_list = []
    while len(random_list) < 5:
        num = random.randint(1,70)
        if num not in random_list:
            random_list.append(num)

    print('Mega Millions', '\n' * 2, random_list)
    input('Hit Enter Key to return to menu...')
    print('\n' * 2)
    menu()
        
    
def luckydaylotto():
    random_list = []
    while len(random_list) < 5:
        num = random.randint(1,45)
        if num not in random_list:
            random_list.append(num)

    print('Lucky Day Lotto', '\n' * 2, random_list)
    input('Hit Enter Key to return to menu...')
    print('\n' * 2)
    menu()
    
def lotto():
    random_list = []
    while len(random_list) < 6:
        num = random.randint(1,52)
        if num not in random_list:
            random_list.append(num)

    print('Lotto', '\n' * 2, random_list)
    input('Hit Enter Key to return to menu...')
    print('\n' * 2)
    menu()

def menu():
    displaymenu()
    selection = input(' Select 1,2,3,4 or 9 [to quit]: ')

    if selection == '1':
        powerball()
    elif selection == '2':
        megamillions()
    elif selection == '3':
        luckydaylotto()
    elif selection == '4':
        lotto()
    else:
        if selection == '9':
            print('Better Luck Next Time')
        else:
            print('Invalid selection, try again')

        again = input('Do you want to try again? (y/n): ').lower()

        if again in ['y', 'yes']:
            print('\n' + '-' * 40 + '\n')
            menu()
        else:
            print('Goodbye!')
            return
menu()