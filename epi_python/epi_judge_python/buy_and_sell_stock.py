from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    max_profit, min_price = 0, float('inf')
    for price in prices:
        profit = price - min_price
        max_profit = max(profit, max_profit)
        min_price = min(price, min_price)
    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
