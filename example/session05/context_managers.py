import contextlib
from typing import Generator, Self


class MyContext:
    def __enter__(self) -> Self:
        print("Entering context")
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: object | None,
    ) -> bool:
        print(exc_type, exc_value, traceback)
        print("Exiting context")
        return True


@contextlib.contextmanager
def my_context() -> Generator[None, None, bool]:
    try:
        print("Entering context")
        yield
    except BaseException as e:
        exc_type = type(e)
        exc_value = e
        traceback = e.__traceback__
        print(exc_type, exc_value, traceback)
    finally:
        print("Exiting context")
        return True


with MyContext() as context:
    print(context)
    print("Inside context")

    raise ValueError("Something went wrong")

with my_context():
    print("Inside context")
    raise ValueError("Something went wrong")
