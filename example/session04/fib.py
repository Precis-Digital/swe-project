def fib(n: int) -> int:
    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)


def print_fib(n: int) -> None:
    result = fib(n)
    # print(f"Fibonacci of {n} is {result}")
