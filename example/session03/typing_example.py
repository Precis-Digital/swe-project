import enum


class Operation(enum.Enum):
    SUM = enum.auto()
    AVG = enum.auto()


def calculate(values: list[int], operation: Operation) -> int:
    if operation is Operation.SUM:
        return sum(values)
    elif operation is Operation.AVG:
        return int(sum(values) / len(values))


result = calculate(values=[10, 20, 30], operation=Operation.AVG)
print(result)
