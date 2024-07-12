from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R", bound=str)


def shout(func: Callable[P, R]) -> Callable[P, R]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        return func(*args, **kwargs).upper() + "!!!"

    return wrapper


@shout
def say_hello(name: str) -> str:
    return f"Hello {name}!"


@shout
def say_goodbye(name: str) -> str:
    return f"Goodbye {name}!"


# say_hello = shout(say_hello)
# say_goodbye = shout(say_goodbye)

print(say_hello("Alice"))
print(say_goodbye("Alice"))
