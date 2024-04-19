import time


def fib(n: int) -> int:
    if n <= 1:
        return n

    return fib(n - 2) + fib(n - 1)


t0 = time.monotonic()
fib(32)
print(time.monotonic() - t0)
