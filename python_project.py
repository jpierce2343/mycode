#!/usr/bin/env python3         ## python_project.py
## Dictionaries set for user input
import pyfiglet
weapon= ["daniel defense", "sig", "bcm", "knight's armament"]

a= weapon[0]
b= weapon[1]
c= weapon[2]
d= weapon[3]

optic= ["scope", "lpvo", "red dot", "iron"]

a= optic[0]
b= optic[1]
c= optic[2]
d= optic[3]

muzzle= ["suppressed", "flash hider"]

a= muzzle[0]
b= muzzle[1]

def main():
# Choose first item
    print("choose a weapon (a, b, c, or d)")
    choice = input()
    weapon_choice = weapon[ord(choice) - ord('a')]

#choose second item
    print("choose sights (a, b, c, or d)")
    choice = input()
    optic_choice = optic[ord(choice) - ord('a')]

# Choose third item
    print("choose barrel end (a or b)")
    choice = input()
    muzzle_choice = muzzle[ord(choice) - ord('a')]

# Print out rifle combination
    print(f"Your rifle is {weapon_choice} with {optic_choice} and {muzzle_choice}")

    print(ascii.file)
main()
