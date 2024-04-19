from typing import Never


def do_something() -> None: ...


def loop_forever() -> Never:
    while True:
        do_something()


def raise_error() -> Never:
    raise ValueError("This function never returns")
