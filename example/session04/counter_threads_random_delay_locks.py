import random
import threading
import time

counter = 0

counter_lock = threading.Lock()


def random_delay() -> None:
    time.sleep(random.random() / 3)


def run_counter() -> None:
    global counter
    with counter_lock:
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


def main() -> None:
    print("Starting counter")
    threads = []
    for i in range(10):
        thread = threading.Thread(target=run_counter)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Finishing counter")


if __name__ == "__main__":
    main()
