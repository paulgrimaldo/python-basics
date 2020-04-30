# -*- coding: utf-8 -*-
from pip._vendor.distlib.compat import raw_input


def protected(func):
    def wrapper(password):

        if password == 'hello':
            return func()
        else:
            print('Wrong password')

    return wrapper


@protected
def protected_func():
    print('Password correct')


if __name__ == '__main__':
    password = str(raw_input('Enter your password: '))

    protected_func(password)
