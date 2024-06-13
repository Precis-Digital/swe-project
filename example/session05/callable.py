from typing import Any


class MyCallable:
    def __call__(self, arg: Any) -> None:
        print(f"Called with {arg}")


my_callable = MyCallable()
my_callable("hello world")
