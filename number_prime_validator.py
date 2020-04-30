from pip._vendor.distlib.compat import raw_input


def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number > 2 and number % 2 == 0:
        return False
    else:
        for i in range(3, number):
            if number % i == 0:
                return False
        return True


def run():
    number = int(raw_input('Enter a number: '))
    result = is_prime(number)

    if result:
        print('The number {} is prime'.format(number))
    else:
        print('The number {} is not prime'.format(number))


if __name__ == "__main__":
    run()
