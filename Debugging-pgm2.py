# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 10:18:47 2026

@author: CHRISTIAN BAHAMON
"""

# property tax program calculator 2

def getinput(msg):
    xin = float(input(msg))
    return xin

def main():
    print('\n'*1)

    AssesmentLevel = 0.10
    HomeOwnerEx = 500.43
    SeniorCEX = 357.45

    PropertyValue = getinput('Enter value of property: ')
    StateEqualizer = getinput('Enter state equalizer rate: ')
    LocalTaxRate = getinput('Enter local tax rate: ')

    print('\n'*1)

    # convert percentage to decimal
    LocalTaxRate = LocalTaxRate / 100

    AssessedValue = PropertyValue * AssesmentLevel
    EqualizeValue = AssessedValue * StateEqualizer
    PropertyTaxBefore = EqualizeValue * LocalTaxRate
    TotalPropertyTax = PropertyTaxBefore - HomeOwnerEx - SeniorCEX

    print('\n'*1)
    print('Property tax due:', format(TotalPropertyTax, '.2f'))
    print('\n'*1)

    return TotalPropertyTax

main()
