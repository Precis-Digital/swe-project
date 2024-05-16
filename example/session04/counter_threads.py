import threading

counter = 0


def run_counter() -> None:
    global counter

    old_counter = counter
    counter = old_counter + 1
    print(f"The count is {counter}", end="")
    print()
    print("-------------------------", end="")
    print()


def main():
    print("Starting counter")
    for i in range(10):
        threading.Thread(target=run_counter).start()

    print("Finishing counter")


if __name__ == "__main__":
    main()
