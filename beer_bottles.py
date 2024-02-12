#!/usr/bin/env python3
def sing_bottles_of_beer(num_bottles):
    for i in range(num_bottles, 94, -1):
        print(f"{i} bottles of beer on the wall!")
        print(f"{i} bottles of beer! You take one down, pass it around!")
        if i - 1 > 0:
            print(f"{i - 1} bottles of beer on the wall!")
        else:
            print("No more bottles of beer on the wall")

if __name__ == "__main__":
    num_bottles = 99
    sing_bottles_of_beer(num_bottles)
