# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 11:44:12 2026

@author: Christian Bahamon
"""

print("Payment Receipt")
print()

name = input("Enter customer name: ")
account_number = input("Enter account number: ")
payment_input = input("Enter payment amount: ")

name = name.strip()
if name == "":
    print("Error: Name cannot be empty")
elif len(name) < 3:
    print("Error: Name must be at least 3 characters long")
elif not name.replace(" ", "").isalpha():
    print("Error: Name must contain only letters")

account_number = account_number.strip()
if account_number == "":
    print("Error: Account number cannot be empty")
elif not account_number.isdigit():
    print("Error: Account number must contain only numbers")
elif len(account_number) != 9:
    print("Error: Account number must be exactly 9 digits long")


payment_input = payment_input.strip()
try:
    payment_amount = float(payment_input)

    if payment_amount <= 0:
        print("Error: Payment amount must be greater than zero")

except ValueError:
    print("Error: Payment amount must be a valid number")
