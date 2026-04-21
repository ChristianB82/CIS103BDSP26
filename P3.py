# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 09:34:39 2026

@author: Christian Bahamon
"""

print("All sales are final")

lbs = float(input("Number of pounds: "))

price_per_lb = 0.99
gross = lbs * price_per_lb


def discount_rate(lbs):
    # discount rates depend on lbs purchased
    if lbs < 0:
        print("Error: Lbs cannot be negative")
        return None
    elif lbs < 10:
        return 0.0
    elif lbs < 100:
        return 0.10
    elif lbs < 1000:
        return 0.20
    elif lbs < 10000:
        return 0.30
    else:
        return 0.40


rate = discount_rate(lbs)

if rate is not None:
    discount = gross * rate
    total = gross - discount

    print("Gross Sales:", gross)
    print("Discount:", discount)
    print("Total Due:", total)