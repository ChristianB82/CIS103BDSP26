# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 10:14:11 2026

@author: Christian Bahamon
"""

def main():
    print('Chicago Rainfall 2017\n\n')

    inputfile = 'c:/temp/chicagorainfall2017.txt'

    rainfall_list = []   
    months = []          

    with open(inputfile, 'r') as infile:
        for line in infile:
            line = line.strip()
            if line:
                parts = line.split()
                month = parts[0]
                amount = float(parts[1])

                months.append(month)
                rainfall_list.append(amount)

    print("Highest:", max(rainfall_list))
    print("Lowest:", min(rainfall_list))
    print("Total:", sum(rainfall_list))
    average = sum(rainfall_list) / len(rainfall_list)
    print("Average:", round(average,2))

main()
