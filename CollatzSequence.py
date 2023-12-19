try:
    def collatz(number):
        return calculation(number)

    def calculation(number):
        if number % 2 == 0 :
            return number // 2
        else:
            return 3 * number + 1

    number = int(input('Enter a number: '))
    while number != 1:
        print(collatz(number))
        number = collatz(number)
except ValueError:
    print('You must enter an integer')
