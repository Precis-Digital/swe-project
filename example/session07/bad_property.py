import time


class MyClass:
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b

    @property
    def ab(self) -> int:
        time.sleep(5)
        return self.a * self.b


my_instance = MyClass(a=10, b=20)

print("accessing ab...")
print(my_instance.ab)
