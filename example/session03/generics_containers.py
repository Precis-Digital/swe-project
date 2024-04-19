def func(x: list[int] | tuple[int, int]) -> dict[str, int] | None:
    if (sum_x := sum(x)) > 100:
        return {"value": sum_x}

    return None
