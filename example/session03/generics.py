from typing import Protocol


class SupportsComparison(Protocol):
    def __lt__(self, other) -> bool: ...


def get_max[T: SupportsComparison](items: list[T]) -> T:
    return max(items)
