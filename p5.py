# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 11:07:59 2026

@author: Christian Bahamon
"""

# Data Table Program

running = True

while running:

    print("\nData Table")
    print("Addition, Subtraction, Multiplication, or Division")

    operation = input("Which operation is requested: ").strip().lower()

    if operation not in ["addition", "subtraction", "multiplication", "division"]:
        print("Error: Invalid operation selected")

    else:
        value = input("Enter a number: ").strip()

        if value == "":
            print("Error: Number cannot be empty")

        elif not value.replace(".", "", 1).isdigit():
            print("Error: Please enter a valid number")

        else:
            value = float(value)

            print(f"\n{operation.capitalize()} Table for {value}\n")

            for i in range(1, 11):

                if operation == "addition":
                    print(f"{value} + {i} = {value + i}")

                elif operation == "subtraction":
                    print(f"{value} - {i} = {value - i}")

                elif operation == "multiplication":
                    print(f"{value} x {i} = {value * i}")

                elif operation == "division":
                    print(f"{value} / {i} = {value / i}")

    answer = input("\nDo you want to perform another table? (yes/no): ").strip().lower()

    if answer != "yes":
        running = False

print("Thats all folks")
