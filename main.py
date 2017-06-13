import datetime
import random


def sum_double(a, b):
    sum = a+b
    if a == b:
        return sum+sum
    return sum


def not_string(str):
    if str[0:3] == "not":
        return str
    return "not "+str


def missing_char(str, n):
    return str[0:n]+str[n+1:len(str)]


def front_back(str):
    if len(str)==1:
        return str
    return str[len(str)-1:len(str)]+str[1:len(str)-1]+str[0:1]


def get_details():
    name = input("please enter your first name")
    last_name = input("please enter your last name")
    year = input("please enter your year of birth")
    age = (datetime.datetime.now().year - int(year))
    print("Your initial are", name[0].upper()+last_name[0].upper(), "and you are", age, "years old")


def guess_num():
    return random.randint(0, 100)


def let_guss(num):
    print("The guess number is:", num)
    x=input("Please enter number")
    if int(x) == int(num):
        print("You Won")
        return 1
    else:
        print("You Lost")
        if int(x) < int(num):
            print("you to lwo")
        else:
            print("You too high")
        return 0


def game_guess():
    result = let_guss(guess_num())
    while result == 0:
        result = let_guss(guess_num())
game_guess()
get_details()
print(sum_double(5, 5))
print(sum_double(2, 4))
print(not_string('not bad'))
print("yifat"[0:3])
