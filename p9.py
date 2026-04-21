# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 10:56:20 2026

@author: Christian Bahamon
"""

def part1():
    print('Data Conversion')
    print('\n' * 2)
    print('Acres to Hectares')
    try:
        acres = float(input('Enter amount of Acres: '))
        if acres < 0:
            print('Error: Value cannot be negative')
        else:
            hect = acres * 0.4047
            print('Hectares:', format(hect, '.2f'))
    except ValueError:
        print('Error: Please enter a valid number')
    

def part2():
    print('\n' * 2)
    print('Quarts to Liters')
    try:
        qrtz = float(input('Enter amount of Quarts: '))
        if qrtz < 0:
            print('Error: Value cannot be negative')
        else:
            liters = qrtz * 0.946353
            print('Liters:', format(liters, '.2f'))
    except ValueError:
        print('Error: Please enter a valid number')



def part3():
    print('\n' * 2)
    print('Fahrenheit to Kelvin')
    try:
        fah = float(input('Enter the temperature Fahrenheit: '))
        K = (fah - 32) * (5/9) + 273.15
        print('Kelvin:', format(K, '.2f'))
    except ValueError:
        print('Error: Please enter a valid number')
        


def main():
    again = 'y'

    while again.lower() == 'y':
        part1()
        part2()
        part3()

        print('\n')
        again = input('Run all conversions again? (Y/N): ')

    print('Program ended.')
    return
main()