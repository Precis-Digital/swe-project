from __future__ import annotations


class A:
    def __init__(self, a: int, b: int, c: int) -> None:
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def from_list(cls, abc: list[int]) -> A:
        return cls(a=abc[0], b=abc[1], c=abc[2])


a1 = A(a=1, b=2, c=3)
a2 = A.from_list([1, 2, 3])
