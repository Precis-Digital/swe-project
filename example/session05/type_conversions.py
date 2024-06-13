class MyInt:
    def __init__(self, value: int) -> None:
        self.value = value

    def __int__(self) -> int:
        return self.value

    def __float__(self) -> float:
        return float(self.value)

    def __str__(self) -> str:
        return str(self.value)


my_int = MyInt(10)

print(int(my_int), type(int(my_int)))
print(float(my_int), type(float(my_int)))
print(str(my_int), type(str(my_int)))
