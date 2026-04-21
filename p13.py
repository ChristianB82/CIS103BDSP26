# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 10:14:11 2026

@author: Christian Bahamon
"""

def main():

    # dictionary for Roman Numerals
    roman_dict = {
        1:"I", 2:"II", 3:"III", 4:"IV", 5:"V",
        6:"VI", 7:"VII", 8:"VIII", 9:"IX", 10:"X",
        11:"XI", 12:"XII", 13:"XIII", 14:"XIV", 15:"XV",
        16:"XVI", 17:"XVII", 18:"XVIII", 19:"XIX", 20:"XX",
        21:"XXI", 22:"XXII", 23:"XXIII", 24:"XXIV"}

    again = "y"

    while again.lower() == "y":

        try:
            num = int(input("Enter a number (0 or negative to quit): "))

            while num > 0:

                if num in roman_dict:
                    print("Roman numeral:", roman_dict[num])

                else:
                    print("Number not found in dictionary.")
                    add = input("Do you want to add it? (y/n): ")

                    if add.lower() == "y":
                        roman = input("Enter the Roman numeral: ")

                        if roman.isalpha():
                            roman_dict[num] = roman
                            print("Added to dictionary.")
                        else:
                            print("Input must be numerical & whole numbers.")

                num = int(input("Enter a number (0 or negative number to quit): "))

        except ValueError:
            print("Invalid input. Please enter a number.")

        print("\nCurrent Dictionary:")
        print(roman_dict)

        again = input("\nRun program again? (y/n): ")

        if again.lower() == 'n':
            print('Program ended')

main()