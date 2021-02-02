def say_hi(user, age):
    print("Hello " + user + ". You're " + age)


def write_name():
    name1 = input("Your name:")
    age1 = input("Your age:")
    name2 = input("Your friend's name:")
    age2 = input("Your friend's age:")
    say_hi(name1, age1)
    say_hi(name2, age2)


def cube(num):
    return num*num*num  # return statement


def calculate_cube():
    num = input("Enter cube's size:")
    result = cube(int(num))
    print(result)











