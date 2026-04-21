# -*- coding: utf-8 -*-
"""
Created on Sun Feb 15 21:15:26 2026

@author: Christian Bahamon
"""
# Conversion Table

# Miles to Kilometers

def main1():
    print('Miles to Kilometers conversion')
    miles = float(input('Enter miles here:'))
    kilometers = miles * 1.609344
    print('Kilometers: ', kilometers)
    return
main1()
print('\n' * 2)

# Pounds to Kilograms
 
def main3():
    print('Pounds to Kilograms')
    lbs = float(input('Enter the amount of lbs here:'))
    kgms = lbs * 0.45359237
    print('Kilograms: ', kgms)
    return
main3()
print('\n' *2)

# Fahrenheit to Celsius

def main2():
    print('Fahrenheit to Celsius conversion')
    fahr = float(input('Enter Fahrenheit temperature here:'))
    celc = (fahr - 32) * 5/9
    print('Celsius: ', celc)
    return
main2()
print('\n' *2)
