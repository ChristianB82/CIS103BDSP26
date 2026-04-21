# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 09:42:38 2026

@author: Christian Bahamon
"""

def main():
    running = True

    while running:
        duration = input('How long should the loop run: ').strip()

        # Validate input
        if duration == "":
            print('Error: Input cannot be blank')
            continue

        if not duration.isdigit():
            print("Error: Please enter a valid whole number.")
            continue

        duration = int(duration)

        if duration <= 5:
            print('Error: Input must be greater than 5')
            continue

        # Run calorie table
        count = 5
        while count <= duration:
            calories = count * 4.33
            print(f"{count} minutes = {calories:.2f} calories")
            count += 5

        while running:
            again = input("Do you want to run it again? (y/n): ").strip().lower()

            if again == "n":
                running = False
                print("That's all folks.")
                break
            elif again == "y":
                print("\nRunning again...\n")
                break
            else:
                print("Follow directions! Please enter 'y' or 'n'.")

main()