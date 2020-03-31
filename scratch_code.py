# daily work
import math


weight = int(input("weight: "))
unit = input("(L)bs or (K)g: ")

if unit.upper() == "L":
    converted = weight * .45
    print(f"you r {converted} kgs.")
else:
    converted = weight / .45
    print(f"you r {converted} pounds.")

