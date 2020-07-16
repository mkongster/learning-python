from functools import lru_cache, wraps
import time


def timer(func):
    def wrapper_timer(*args, **kwargs):
        tic = time.perf_counter()
        value = func(*args, **kwargs)
        toc = time.perf_counter()
        elapsed = toc - tic
        print('Elapsed time: {elapsed}'.format(elapsed=elapsed))
        return value
    return wrapper_timer


def fibonacci(n):
    if n == 1:
        return 0
    if n <= 2:
        return 1
    last = 0
    current = 1
    for _ in range(1, n):
        last, current = current, last + current
    return current


def fib2(n):
    if n < 2:
        return n
    return fib2(n - 2) + fib2(n - 1)


memo = {0: 0, 1: 1}
def fib3(n):
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2)
    return memo[n]


@lru_cache(maxsize=None)
def fib4(n):
    if n < 2:
        return n
    return fib4(n - 2) + fib4(n - 1)


@timer
def test_fibs(fib_func):
    return fib_func


def main():
    func_list = [fibonacci, fib2, fib3, fib4]
    for i in func_list:
        print(test_fibs(i))

if __name__ == "__main__":
    main()