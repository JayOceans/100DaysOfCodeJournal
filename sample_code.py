
import math

# Day 5



numbers = [5, 2, 5, 2, 2]

for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)


prices = [10, 20, 30]
total = 0

for cost in prices:
    total += cost
print(f"the total is {total})


user_says = ""
now_started = False

while True:
    user_says = input(">").lower()

    if user_says == "start":
        if now_started:
            print("your already started!!!")
        else:
            now_started = True
            print("your car is starting...")

    elif user_says == "stop":
        if not now_started:
            print("your already stopped!!!")
        else:
            now_started = False
            print("your car is stoping...")

    elif user_says == "help":
        print("""
        start - starts car
        stops - stops car
        quit - quits game
        """)
    elif user_says == "quit":
        break

    else:
        print("sorry, i don't understand")


magic_number = 7
guess_limit = 3

num_of_trys = 0


while num_of_trys < guess_limit:
    user_guess = int(input("please guess 1-10: "))
    num_of_trys += 1

    if user_guess == magic_number:
        print("your right!")
        break
else:
    print("you lose")

print("game over")


# Day 4

weight = int(input("weight: "))
unit = input("(L)bs or (K)g: ")

if unit.upper() == "L":
    converted = weight * .45
    print(f"you r {converted} kgs.")
else:
    converted = weight / .45
    print(f"you r {converted} pounds.")


name = "jay"

if len(name) < 3:
    print("your names too short")
elif len(name) >= 50:
    print("yo names too long, dude")
else:
    print(f"thnaks {name}!")


house_price = 1000000
has_good_credit = True

if has_good_credit:
    deposit = house_price * .1

else:
    deposit = house_price * .2

print(f"the despoit is ${deposit}.")


lbs = input("how many pound u weigh? ")
kilos = int(lbs) / 2
KGs = kilos * .1
KG = kilos - KGs

print("you weigh " + str(KG) + " kg...wow!")


name = input("what's your name? ")
age = input("what's your age? ")
print(name + " is " + age + " years old.")
print("ok")
print("good")


def fizz_buzz(input):

    if (input % 5 == 0) and (input % 3 == 0):
        return("FizzBuzz")
    if input % 3 == 0:
        return("Fizz")
    if input % 5 == 0:
        return("Buzz")
    return(input)


print(fizz_buzz(34))


def multing_unknown_numbers(*abc):

    total = 1
    for x in abc:
        total *= x   # total = total * x
    return total


print(multing_unknown_numbers(3, 9,))


def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("welcome aboard")


greet("Jay", "Oceans")


# Day 3

# add change
# did the file name change ?...
# test if git is needed ... NO

count = 0
for number in range(1, 30):
    if number % 2 == 0:
        print(number)
        count += 1
print(f"we have {count} numbers...")


# Day 2 code disappeared (sad)

# LOST CODE...


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
