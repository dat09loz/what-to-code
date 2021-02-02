def input_male():
    choice = input("Are you a male? (Answer T/F only):")
    return choice.upper()

def input_tall():
    choice = input("Are you tall? (Answer T/F only):")
    return choice.upper()

def output(is_male, is_tall):
    if is_male and is_tall:
        print("You are a tall male.")
    elif not is_male and is_tall:
        print("You are tall but not male.")
    elif is_male and not is_tall:
        print("You are male but short. Pretty GAY.")
    elif not is_male and not is_tall:
        print("You are short and GAY!")

def converter(input_data):
    if input_data == "T":
        return True
    else:
        return False

def run():
    gender = input_male()
    gender = converter(gender)
    height = input_tall()
    height = converter(height)
    output(gender, height)

run()