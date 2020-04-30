from pip._vendor.distlib.compat import raw_input


def calculate_factorial(number):
    if number == 0:
        return 1
    else:
        return number * calculate_factorial(number - 1)


def run():
    number = int(raw_input("Enter a number: "))
    result = calculate_factorial(number)
    print('Factorial of {} = {}'.format(number, result))


if __name__ == "__main__":
    run()
