class MyAttributeAccessClass:
    def __init__(self, x: int) -> None:
        self.x = x

    def __getattribute__(self, item: str) -> int:
        print(f"Getting attribute {item}")
        return super().__getattribute__(item)

    def __getattr__(self, item: str) -> int:
        print(f"Getting missing attribute {item}")
        return 0

    def __setattr__(self, key: str, value: int) -> None:
        print(f"Setting attribute {key} to {value}")
        super().__setattr__(key, value)


a = MyAttributeAccessClass(10)
print(a.x)
print(a.y)
