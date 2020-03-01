#!/usr/bin/python

import argparse


def find_max_profit(price_list):
    return max(price_list)-min(price_list)


def find_max_profit2(price_list):
    init = price_list[0]
    for item in range(1, len(price_list)+1):
        for price in price_list:
            if price > init:
                price, init = init, price
            else:
                continue

    # for price in price_list:
    #     if price > init:
    #         # set init to price

    #         return False
    # return True


def fmp(price_list):
    return max(price_list)-min(price_list)



def check(price_list, value):
    # traverse in the list
    for price in price_list:
        # compare with all the prices with highest or lowest number
        if value >= price:
            return False
    return True


# trial  pass two
#  compare first index with the second second and so on.
# store
# for each number compared to the next number
# if greater then set as the highest number
#Answer is 6
print(find_max_profit([10, 7, 5, 8, 11, 9]))


if __name__ == '__main__':
        # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
