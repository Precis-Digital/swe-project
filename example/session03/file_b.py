from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from file_a import A


class B:
    @staticmethod
    def print_a(a: A) -> None:
        print(a)
