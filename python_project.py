#!/usr/bin/env python3         ## python_project.py
## Dictionaries set for user input
import crayons
weapon= ["Daniel Defense", "SIG", "BCM", "Knight's Armament"]

A= weapon[0]
B= weapon[1]
C= weapon[2]
D= weapon[3]

optic= ["scope", "lpvo", "red dot", "irons"]

A= optic[0]
B= optic[1]
C= optic[2]
D= optic[3]

muzzle= ["suppressed", "flash hider"]

A= muzzle[0]
A= muzzle[1]

Art_Rifle =((r"""
                           ______
        |\_______________ (_____\\______________
HH======#H###############H#######################
         |__|_|_|_|______|##(_))#H\*****Y########
                          //    \#H\        *Y###
                          //     \H*\
                          """))
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
    print(crayons.red(f"Your rifle is {weapon_choice} with {optic_choice} and {muzzle_choice}"))

    print(Art_Rifle)    

if __name__ == "__main__":
    main()
