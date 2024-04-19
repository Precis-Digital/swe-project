from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from file_b import B


class A:
    @staticmethod
    def print_b(b: B) -> None:
        print(b)
