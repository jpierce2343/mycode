#!/usr/bin/env python3

from subprocess import call

call(["ip", "link", "show", "up"])
print("This program will check you interfaces.")
interface = input("Enter an interface, like, ens3: ")
call(["ip", "show", "dev", interface])
call(["ip", "route", "show", "dev", interface])
