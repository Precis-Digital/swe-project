"""This is a linting example"""

first_number = int(input("Input first number: "))
second_number = int(input("Input second number: "))


operator = input("Operator: ")


def print_result():
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
    print_result()


if __name__ == "__main__":
    main()
