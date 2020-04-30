# -*- coding: utf-8 -*-
from pip._vendor.distlib.compat import raw_input


def foreign_exchange_calculator(amount):
    bs_to_usd_rate = 9.96
    return amount / bs_to_usd_rate


def run():
    print("Bs to USD calculator")
    print('')

    amount = float(raw_input('What is the Bs amount?'))
    result = foreign_exchange_calculator(amount)

    print('${} Bs = ${} USD'.format(amount, result))


if __name__ == '__main__':
    run()
