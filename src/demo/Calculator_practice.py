def is_number(str):
    try:
        float(str)
    except ValueError:
        return False
    else:
        return True


def is_operation(str):
    if str not in ("+", "-", "*", "/"):
        return False
    else:
        return True


def error_detect_num(str):
    if is_number(str):
        str = float(str)
        return str
    else:
        print("Please enter a valid number.")
        main()


def error_detect_op(str):
    if is_operation(str):
        return str
    else:
        print("Please enter a valid operation.")
        main()


def operate(num1, op, num2):
    if op == "+":
        result = str(num1 + num2)
        return result
    elif op == "-":
        result = str(num1 - num2)
        return result
    elif op == "*":
        result = str(num1 * num2)
        return result
    else:
        try:
            result = str(num1 / num2)
        except ZeroDivisionError as err:
            return str(err)
        else:
            return result


def main():
    num1 = input("Enter the first number: ")
    num1 = error_detect_num(num1)
    op = input("Enter operator (+ - * /): ")
    op = error_detect_op(op)
    num2 = input("Enter the second number: ")
    num2 = error_detect_num(num2)
    print("Result: " + operate(num1, op, num2))


main()