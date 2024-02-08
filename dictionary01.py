#!/usr/bin/python3
                            ##dictionary01.py
# character values
marvelchars= {
    "Starlord":
      {"real name": "peter quill",
      "powers": "dance moves",
      "archenemy": "Thanos"},

    "Mystique":
      {"real name": "raven darkholme",
      "powers": "shape shifter",
      "archenemy": "Professor X"},

    "Hulk":
      {"real name": "bruce banner",
      "powers": "super strength",
      "archenemy": "adrenaline"}
             }


# Prompt user to enter character name
char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk)")

# Prompt user to enter stat
char_stat = input("What statistic do you want to know about? (real name, powers, archenemy)")

# Are char_name and char_stat valid?
if char_name in marvelchars and char_stat in marvelchars[char_name]:
    # Get value from dictionary
    value = marvelchars[char_name][char_stat]
    # Print result
    print(f"{char_name}'s {char_stat} is : {value}")
else:
    print("Invalid character name or statistic")
