<<<<<<< HEAD
=======
# add change
# did the file name change ?...

>>>>>>> 64340e991dadb6f7c622ea82271b69d8505cecd9
import math


# Day 1

# x = input("x: ")
y = int(x) + 3
print(y)

temp = 25
if temp < 20:
    print("it's cold!")
elif temp > 30:
    print("it's crazy hot!!")
else:
    print("it's fine")
print("ok")

age = 24
if age < 18:
    print("too young!")
else:
    print("ok!")

# OR
age = 12

message = ("ok") if age > 18 else "too young"

print(message)

# and  not  or

stack_sats = True
strong_hands = True
big_ego = False

if (stack_sats or strong_hands) and not big_ego:
    print("to the moon!")
else:
    print("sad face...")


# coding bitcoin

shit_coin = False
strong_hands = False
big_heart = False

if (strong_hands or big_heart) and not shit_coin:
    print("to the moon!")
else:
    print("game over")

    # chaining comparison operators

temp = 76

if 50 < temp <= 75:
    print("it's a nice day")
else:
    print("it's too hot or too cold")

# for  in a range

for number in range(1, 100, 2):
    print("Try", number, number * "*")

# maybe trying to get user info OR send something

successful_sent = True

for number in range(1, 4):
    print("Try", number)
    if successful_sent:
        print("thanks")
        break
else:
    print("sorry, no go")

# Day 0

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
