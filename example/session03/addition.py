class SpecialString(str):
    def __add__(self, other: str | int) -> str | int:
        if isinstance(other, int):
            return int(self) + other

        return super().__add__(other)

    def __radd__(self, other: int) -> int:
        return other + int(self)


s = SpecialString("hello")
print(s + " world")  # hello world

s = SpecialString("10")
print(s + 5)  # 15
print(5 + s)
