# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 10:14:11 2026

@author: Christian Bahamon
"""

def sum_recursive(n):
    if n == 1:
        return "1", 1

    expr, subtotal = sum_recursive(n - 1)
    return f"{n}+{expr}", n + subtotal


def main():
    again = "y"

    while again == "y":
        numb = input('Enter a positive whole number: ')

        if numb == '':
            print('Error: Input cannot be blank')
            continue

        elif not numb.isdigit():
            print("Error: Input is not valid")
            continue
        else:
            numb = int(numb)

        if numb <= 0:
            print("Error: Number must be greater than 0")
            continue

        expression, total = sum_recursive(numb)
        print(f"{expression} = {total}")

        again = input("Another number? y/n: ").lower()

    print('Program ended')


main()
