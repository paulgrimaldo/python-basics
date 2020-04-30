from pip._vendor.distlib.compat import raw_input


def sum_recursive(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return number + sum_recursive(number - 1)


def run():
    number = int(raw_input("Enter a number: "))
    result = sum_recursive(number)
    print('Sum = {}'.format(result))


if __name__ == "__main__":
    run()
