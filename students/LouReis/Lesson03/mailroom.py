#!/usr/bin/env python3
# mailroom.py
# Coded by LouReis

"""
Write a small command-line script called mailroom.py.
It should have a data structure that holds a list of your donors and a history
of the amounts they have donated. This structure should be populated at first
with at least five donors, with between 1 and 3 donations each.
The script should prompt the user (you) to choose from a menu of 3 actions:
“Send a Thank You”, “Create a Report” or “quit”)

Report should look like the following:
Donor Name                | Total Given | Num Gifts | Average Gift
------------------------------------------------------------------
Joe Donor                  $  653784.49           2  $   326892.24
John Rich                  $   16396.10           3  $     5465.37
Sally Neighbor             $     877.33           1  $      877.33
Mack Jack                  $     708.42           3  $      236.14

"""

# donations = ['Robin Hood', 1500000, 3, 500000, 'Tycoon Reis', 75000000, 3, 25000000, 'Howie Long', 100000, 1, 100000, 'Joe Neighbor', 50, 2, 25, 'Rick Retiree', 1.00, 2, 0.50]
# Data structure in global namespace to store all donations & donors.
donations = ['Robin Hood', 50000, 'Tycoon Reis', 25000000, 'Howie Long', 100000, 'Joe Neighbor', 25, 'Rick Retiree', 0.50, 'Robin Hood', 50000, 'Tycoon Reis', 25000000, 'Joe Neighbor', 25, 'Rick Retiree', 0.50, 'Robin Hood', 50000, 'Tycoon Reis', 25000000]
donor_list = ['Robin Hood', 'Tycoon Reis', 'Howie Long', 'Joe Neighbor', 'Rick Retiree']

print("Mailroom Donation Tracking System - MDTS")
print("Please choose from the following Menu Options:")
print("1 - Create a Donation Report")
print("2 - Generate a Thank You Note")
print("3 - Quit Program")
enter = input("Enter Menu Option: ")
if enter == '1':
    print("DONOR SUMMARY REPORT")
elif enter == '2':
    donor=input("Enter the full name of the Donor (Type 'L' for a donor list):")
    if donor == 'L':
        print(donor_list)
else:
    print("Thanks for using MDTS, Goodbye!")






















Donor Name                | Total Given | Num Gifts | Average Gift
------------------------------------------------------------------
William Gates, III         $  653784.49           2  $   326892.24
Mark Zuckerberg            $   16396.10           3  $     5465.37
Jeff Bezos                 $     877.33           1  $      877.33
Paul Allen                 $     708.42           3  $      236.14
