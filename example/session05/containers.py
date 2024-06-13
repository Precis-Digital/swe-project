from typing import Any, Iterable


class MyContainer:
    def __init__(self, *args) -> None:
        self._items = list(args)

    def __str__(self) -> str:
        return str(self._items).replace("[", "<").replace("]", ">")

    def __iter__(self) -> Iterable[Any]:
        return iter(self._items)

    def __len__(self) -> int:
        return len(self._items)

    def __getitem__(self, index: int) -> Any:
        return self._items[index]

    def __setitem__(self, index: int, value: Any) -> None:
        self._items[index] = value

    def __contains__(self, value: Any) -> bool:
        return value in self._items


my_container = MyContainer(1, 2, 3)
print(my_container)

for item in my_container:
    print(item)

print("length:", len(my_container))
print(my_container[1])

my_container[1] = 10
print(my_container[1])

print(10 in my_container)
