import dataclasses

import pydantic


class MyClass:
    def __init__(self, a: int, b: str) -> None:
        self.a = a
        self.b = b

    def __str__(self) -> str:
        return f"MyClass(a={self.a}, b={self.b})"


my_class = MyClass(a=42, b="Hello, World!")
print(my_class)


print("-" * 25)


@dataclasses.dataclass
class MyDataclass:
    a: int
    b: str


my_dataclass = MyDataclass(a=42, b="Hello, World!")
print(my_dataclass)

print("-" * 25)


class MyPydanticModel(pydantic.BaseModel):
    a: int
    b: str


my_pydantic_model = MyPydanticModel(a=42, b="Hello, World!")
print(my_pydantic_model)
