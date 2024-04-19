from typing import Protocol, TypeVar

T = TypeVar("T", bound="SupportsComparison")


class SupportsComparison(Protocol):
    def __lt__(self, other) -> bool: ...


def get_max(items: list[T]) -> T:
    return max(items)
