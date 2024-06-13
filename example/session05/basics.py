import datetime


class MyClass:
    def __init__(self, x: int = 5, y: int = 10) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"MyClass(x={self.x}, y={self.y})"

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, type(self)):
            return NotImplemented

        return self.x == other.x and self.y == other.y


a = MyClass(x=10, y=20)
b = MyClass(x=10, y=1)

print([a, b])
print(a)

now = datetime.datetime.now()
print(now)
print(repr(now))

print(a == b)
