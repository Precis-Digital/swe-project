import functools


@functools.total_ordering
class A:
    def __init__(self, x: int) -> None:
        self.x = x

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, type(self)):
            return NotImplemented

        return self.x < other.x


a = A(10)
b = A(20)

print(a < b)
print(a > b)
print(a == b)
print(a <= b)
