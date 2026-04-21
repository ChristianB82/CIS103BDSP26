# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 10:27:49 2026

@author: Christian Bahamon
"""

from datetime import datetime

def main():

    inputfile = 'c:/temp/points.txt'
    gradefile = 'c:/temp/grades.txt'
    errorfile = 'c:/temp/errors.txt'

    infile = open(inputfile, 'r')
    gfile = open(gradefile, 'w')
    efile = open(errorfile, 'w')

    total_records = 0
    graded_records = 0
    error_records = 0

    countA = 0
    countB = 0
    countC = 0
    countD = 0
    countF = 0

    timestamp_start = datetime.now()

    line = infile.readline()

    while line != '':
        total_records += 1
        line = line.strip()
        parts = line.split(',')

        try:
            if len(parts) != 3:
                raise ValueError("Missing fields")

            idnum = parts[0].strip()
            name = parts[1].strip()

            try:
                points = int(parts[2].strip())
            except:
                raise ValueError('(' + idnum + ')' + ',' + "Points not numeric")

            if points < 0 or points > 1000:
                raise ValueError('(' + idnum + ')' + ',' + "Points out of range")

            if points >= 900:
                grade = 'A'
                countA += 1
            elif points >= 800:
                grade = 'B'
                countB += 1
            elif points >= 700:
                grade = 'C'
                countC += 1
            elif points >= 600:
                grade = 'D'
                countD += 1
            else:
                grade = 'F'
                countF += 1

            gfile.write(name + ',' + ' ' + '(' + idnum + ')' + ',' + ' ' + grade + '\n')
            graded_records += 1

        except ValueError as e:
            try:
                name = parts[1].strip()
            except:
                name = "Unknown"

            efile.write(name + " - " + str(e) + '\n')
            error_records += 1

        line = infile.readline()

    timestamp_end = datetime.now()

    infile.close()
    gfile.close()
    efile.close()

    print("\n===== SUMMARY REPORT =====")
    print("Start time:", timestamp_start)
    print("Total records read:", total_records)
    print("A grades:", countA)
    print("B grades:", countB)
    print("C grades:", countC)
    print("D grades:", countD)
    print("F grades:", countF)
    print("Graded records:", graded_records)
    print("Error records:", error_records)
    print("End time:", timestamp_end)

main()