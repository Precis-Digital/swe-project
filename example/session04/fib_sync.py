from example.session04.fib import print_fib

numbers = [30, 31, 32, 33, 34, 35, 36, 37]


def main() -> None:
    for number in numbers:
        print_fib(number)


if __name__ == "__main__":
    main()
