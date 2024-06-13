from typing import Any, Self


class MyMathClass:
    def __init__(self, value: int) -> None:
        self.value = value

    def __str__(self) -> str:
        return f"MyMathClass({self.value})"

    def __repr__(self) -> str:
        return str(self)

    def __add__(self, other: object) -> Self:
        if not isinstance(other, type(self)):
            return NotImplemented

        return type(self)(self.value + other.value)

    def __sub__(self, other: object) -> Self:
        if not isinstance(other, type(self)):
            return NotImplemented

        return type(self)(self.value - other.value)

    def __mul__(self, other: object) -> Self:
        if not isinstance(other, type(self)):
            return NotImplemented

        return type(self)(self.value * other.value)

    def __matmul__(self, other: object) -> None:
        print(f"{self} is spying on {other}")

    def __rmatmul__(self, other: object) -> None:
        print(f"{other} is spying on {self}")

    def __and__(self, other: object) -> list[Self | Any]:
        return [self, other]

    def __iadd__(self, other: object) -> Self:
        if not isinstance(other, type(self)):
            return NotImplemented

        self.value += other.value
        return self


a = MyMathClass(10)
b = MyMathClass(20)

print(a + b)
print(a - b)
print(a * b)
a @ b
a @ 5
5 @ a
print(a & 5)
a += b
print(a)
