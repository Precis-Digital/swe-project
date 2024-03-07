# pylint: disable=missing-function-docstring, missing-module-docstring
def concatenate_strings(a: str, b: str) -> str:
    return a + b


def sum_list_elements(elements: list[int]) -> int:
    return sum(elements)


def find_element(elements: list[str], target: str) -> bool:
    return target in elements


def main() -> None:
    result_1 = concatenate_strings(a="Hello, ", b="123")
    result_2 = sum_list_elements(elements=[1, 2, 3, 4])
    result_3 = find_element(elements=["1", "2", "5"], target="5")

    print(result_1, result_2, result_3)


if __name__ == "__main__":
    main()
