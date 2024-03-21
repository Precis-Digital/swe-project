"""This is a linting example"""


def print_result(first_number: int, second_number: int, operator: str) -> None:
    """Prints the result of the operation."""
    print("Result: ", end="")
    if operator == "+":
        print(first_number + second_number)
    elif operator == "-":
        print(first_number - second_number)
    elif operator == "*":
        print(first_number * second_number)
    elif operator == "/":
        print(first_number / second_number)


def main():
    first_number = int(input("Input first number: "))
    second_number = int(input("Input second number: "))
    operator = input("Operator: ")

    print_result(
        first_number=first_number,
        second_number=second_number,
        operator=operator,
    )


if __name__ == "__main__":
    main()
