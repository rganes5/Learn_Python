num1 = float(input("Enter a first number: " ))
op = input("Enter a arithmetic operator: ")
num2 = float(input("Enter a second number: "))


def calc(num1, op, num2):
    if op == "+":
        return num1+num2
    elif op == "-":
        return num1-num2
    elif op == "*":
        return num1*num2
    elif op == "/":
        return num1/num2
    else:
        print("Invalid operation")


print(calc(num1, op, num2))