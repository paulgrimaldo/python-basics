# -*- coding: utf-8 -*-

import turtle

from pip._vendor.distlib.compat import raw_input


def main():
    window = turtle.Screen()
    dave = turtle.Turtle()

    make_square(dave)

    turtle.mainloop()


def make_square(dave):
    length = int(raw_input('Square length: '))

    for i in range(4):
        make_line_and_turn(dave, length)


def make_line_and_turn(dave, length):
    dave.forward(length)
    dave.left(90)


if __name__ == '__main__':
    main()
