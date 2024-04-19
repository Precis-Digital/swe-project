from typing import overload


class SpecialString(str):

    @overload
    def __add__(self, other: str) -> str: ...
    @overload
    def __add__(self, other: int) -> int: ...

    def __add__(self, other: str | int) -> str | int:
        if isinstance(other, int):
            return int(self) + other

        return super().__add__(other)

    def __radd__(self, other: int) -> int:
        return other + int(self)


s = SpecialString("hello")
reveal_type(s + " world")  # hello world

s = SpecialString("10")
reveal_type(s + 5)  # 15
reveal_type(5 + s)
