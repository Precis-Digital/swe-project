from dataclasses import dataclass
from typing import Protocol
import datetime
from enum import Enum


@dataclass
class Item:
    name: str
    quantity: int
    price: float | None


class Actions(Enum):
    ADD = "add"
    CHECKOUT = "checkout"
    EXIT = "exit"


class Inventory:
    def __init__(self):
        self.content: dict[Item.name, Item] = {}

    def add(self, items: list[Item]):
        for item in items:
            self.content[item.name] = item

    def get(self, item: Item) -> Item | None:
        try:
            assert item.quantity <= self.content[item.name].quantity, f"Not enough {item.name} in the inventory."
            self.content[item.name].quantity -= item.quantity
            item.price = self.content[item.name].price
            return item
        except KeyError:
            print(f"Product {item.name=} not found in the inventory.")


class Cart:
    def __init__(self):
        self.content: list[Item] = []
        self.total_cost = 0

    def add(self, item: Item):
        self.content.append(item)
        self.total_cost += item.price * item.quantity
        print(f"{item.quantity} {item.name} added to cart.")

    def reset(self):
        self.content.clear()
        self.total_cost = 0


class PaymentSystem(Protocol):
    inventory: Inventory
    cart: Cart

    def show_catalog(self): ...

    def apply_discount(self, discount: float): ...

    def checkout(self): ...

    def _print_receipt(self): ...


class TerminalPaymentSystem:
    def __init__(self, inventory: Inventory, cart: Cart):
        self.inventory = inventory
        self.cart = cart

    def _show_welcome_message(self):
        print("=== Welcome to the FoodStore ===")

    def show_catalog(self):
        print("\nAvailable products:")
        items = (f"{item.name} | {item.quantity} | ${item.price}" for _, item in self.inventory.content.items())
        print("\n".join(items))
        print("\n")

    def apply_discount(self, discount: float):
        self.cart.total_cost *= 1 - discount
        print(f"{discount * 100}% discount applied.")

    def checkout(self):
        if not self.cart.content:
            print("Your cart is empty.")
            return
        print(f"To pay: {self.cart.total_cost}")
        discount_code = float(input("Enter your discount code (e.g., '0.1' for 10% off): "))
        assert 0 <= discount_code <= 1, "Discount should be between 0 and 1. Please try again."
        if discount_code:
            self.apply_discount(discount_code)
        self._print_receipt()
        self.cart.reset()

    def _print_receipt(self):
        print("\n\n=== Receipt ===")
        print(f"Your total is: {self.cart.total_cost:2f}")
        print(f"Checkout time: {datetime.datetime.now()}")
        print("=== End Receipt ===")


def start_program(payment_system: PaymentSystem):
    payment_system._show_welcome_message()  # TODO: How to fix typing?
    while True:
        payment_system.show_catalog()
        try:
            action = input(f"Choose action: {", ".join([action.value for action in Actions])}: ")
            match action:
                case Actions.ADD.value:
                    item_name = input("Enter product to add to cart: ")
                    assert item_name in [
                        name for name in payment_system.inventory.content
                    ], "Item not found in the inventory. Please try again."

                    item_quantity = int(input("Enter quantity: "))
                    assert item_quantity > 0, "Quantity should be more than zero. Please try again."

                    payment_system.cart.add(
                        payment_system.inventory.get(
                            Item(name=item_name, quantity=item_quantity, price=None)
                        )  # TODO: How to fix the ugly "price=None"?
                    )
                case Actions.CHECKOUT.value:
                    payment_system.checkout()
                case Actions.EXIT.value:
                    break
                case _:
                    print(f"Invalid action. Please choose {", ".join([action.value for action in Actions])}.")
        except AssertionError as ae:
            print(ae)


if __name__ == "__main__":
    inventory = Inventory()
    inventory.add([Item("apple", 10, 1.2), Item("banana", 20, 0.5), Item("cookie", 30, 2.5)])

    cart = Cart()

    start_program(TerminalPaymentSystem(inventory, cart))
