from multiprocessing import Pool

from example.session04.fib import print_fib

numbers = [30, 31, 32, 33, 34, 35, 36, 37]


def main() -> None:
    with Pool() as pool:
        pool.map(print_fib, numbers)


if __name__ == "__main__":
    main()
