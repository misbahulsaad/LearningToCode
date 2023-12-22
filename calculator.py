def calculator():
    """This is a simple calculator in python"""
    print("1.Add\n2.Substract\n3.Multiply\n4.Divide")
    print("Cheose the operation:", end='')
    while True:
        try:
            choice = int(input())
            if 1<= choice <= 4:
                break
            else:
                print('Please enter a number between 1-4')
        except ValueError:
            print('You must input an integer')

    number1 = float(input('Enter first number: '))
    number2 = float(input('Enter second number: '))

    if choice == 1:
        print(number1, "+", number2, "=", add(number1, number2))
    elif choice == 2:
        print(number1, '-', number2, '=', substract(number1, number2))
    elif choice == 3:
        print(number1, 'x', number2, '=', multiply(number1, number2))
    elif choice == 4:
        print(number1, '/', number2, '=', divide(number1, number2))

def add(number1, number2):
    return number1 + number2
def substract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return 'Invalid: Devide by Zero'
calculator()