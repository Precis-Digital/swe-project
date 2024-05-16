import multiprocessing


def run_counter(counter: multiprocessing.Value) -> None:
    with counter.get_lock():
        old_counter = counter.value
        counter.value = old_counter + 1
        print(f"The count is {counter.value}", end="")
        print()
        print("-------------------------", end="")
        print()


def main() -> None:
    print("Starting counter")

    counter = multiprocessing.Value("i", 0)

    processes = []
    for _ in range(10):
        process = multiprocessing.Process(target=run_counter, args=(counter,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print("Finishing counter")


if __name__ == "__main__":
    main()
