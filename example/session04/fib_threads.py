import threading

from example.session04.fib import print_fib

numbers = [30, 31, 32, 33, 34, 35, 36, 37]


def main() -> None:
    threads = []

    for number in numbers:
        thread = threading.Thread(target=print_fib, args=(number,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
