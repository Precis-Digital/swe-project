import random
import threading
import time

counter = 0


def random_delay() -> None:
    time.sleep(random.random() / 3)


def run_counter() -> None:
    global counter

    random_delay()
    old_counter = counter
    random_delay()
    counter = old_counter + 1
    random_delay()
    print(f"The count is {counter}", end="")
    random_delay()
    print()
    random_delay()
    print("-------------------------", end="")
    random_delay()
    print()
    random_delay()


def main():
    print("Starting counter")
    for i in range(10):
        threading.Thread(target=run_counter).start()
        random_delay()

    print("Finishing counter")


if __name__ == "__main__":
    main()
