# It's just like a panic and recover in golang

try:
    print("Gonna do some dumb thing now!")
    number = int(input("Enter a number soldier: "))
    value = 10 / 0
    print("This won't be printed since it will exit and except will catch it")
except ZeroDivisionError as err1:
    print(err1)
    print("Division by zero ain't good bruh!")
except ValueError:
    print("Invalid input")

