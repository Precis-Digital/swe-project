def process_items(items: list[int]) -> int:
    total = 0
    for item in items:
        total += item

    return total


my_items = [1, 2, 3]
result = process_items(items=my_items)
print("Total:", result)
