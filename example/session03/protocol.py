from typing import Protocol


class Item:
    name: str
    price: int

    def __init__(self, name: str, price: int) -> None:
        self.name = name
        self.price = price


class PaymentSystem(Protocol):
    def pay(self, amount: int) -> None: ...

    def refund(self, amount: int) -> None: ...

    def get_balance(self) -> int: ...


class MyPaymentSystem:
    balance: int

    def __init__(self, balance: int) -> None:
        self.balance = balance

    def pay(self, amount: int) -> None:
        self.balance -= amount

    def refund(self, amount: int) -> None:
        self.balance += amount

    def get_balance(self) -> int:
        return self.balance


def buy_item(item: Item, payment_system: PaymentSystem) -> None:
    payment_system.pay(item.price)
    print(f"Bought {item.name} for {item.price} dollars")
    print(f"Balance: {payment_system.get_balance()}")


def main() -> None:
    item = Item(name="apple", price=10)
    payment_system = MyPaymentSystem(balance=100)
    buy_item(item=item, payment_system=payment_system)


if __name__ == "__main__":
    main()
