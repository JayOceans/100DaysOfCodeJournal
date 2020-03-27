import math

print("Hello World !")
print("*" * 10)
print("hello")

x = "Hello \n Sally"
big = 5

print(big)

print """
hi,
this is Bob
how r u...
"""

print(len(x))
print(x[0])
print(x[1:4])
print(x[-4])

first = "Jay"
last = " Oceans"
full = first + last
print(full)

bold_first_name = first.upper()

print(bold_first_name)

print(full.find("O"))

print(full.find("o"))

print(full.replace("O", "F"))

print("Jay" in full)            # True

print("Joe" not in full)        # True

print(math.ceil(2))


x = input("x: ")
y = int(x) + 3
print(y)

