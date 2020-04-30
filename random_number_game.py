# -*- coding: utf-8 -*-
import random

from pip._vendor.distlib.compat import raw_input


def run():
    number_found = False
    random_number = random.randint(0, 20)

    while not number_found:
        number = int(raw_input('Try a number：'))

        if number == random_number:
            print('Congratulations. You found the number')
            number_found = True
        elif number > random_number:
            print('The number is smaller')
        else:
            print('The number is bigger')


if __name__ == '__main__':
    run()
