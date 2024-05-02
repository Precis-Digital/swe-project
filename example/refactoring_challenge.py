import collections
import dataclasses
import datetime
import enum
from typing import Callable, Generator


class InsufficientInventoryError(Exception):
    pass


class EnumeratedEnum(enum.Enum):
    @classmethod
    def get_enumerated(cls) -> Generator[str, None, None]:
        return (f"[{action.value}] {action.name}" for action in cls)

    @classmethod
    def list_choices(cls) -> str:
        return "\n".join(cls.get_enumerated())


class Product(EnumeratedEnum):
    APPLE = "1"
    BANANA = "2"
    COOKIE = "3"


class Action(EnumeratedEnum):
    ADD = "1"
    CHECKOUT = "2"
    EXIT = "3"


@dataclasses.dataclass
class ProductInfo:
    price: int
    quantity: int

    def __post_init__(self) -> None:
        if not isinstance(self.quantity, int) or self.quantity < 0:
            raise ValueError(f"Invalid inventory: {self.quantity}")


class CashRegistry:
    inventory: dict[Product, ProductInfo]
    discount_codes: dict[str, float]
    cart: collections.defaultdict[Product, int]
    action_map: dict[Action, Callable[[], None]]

    def __init__(
        self,
        inventory: dict[Product, ProductInfo],
        discount_codes: dict[str, float],
    ) -> None:
        self.inventory = inventory
        self.discount_codes = discount_codes
        self.cart = collections.defaultdict(int)
        self.action_map = {
            Action.ADD: self.add_to_cart,
            Action.CHECKOUT: self.checkout,
            Action.EXIT: self.exit,
        }

    def add_to_cart(self) -> None:
        product = take_enum_input(input_type=Product)
        quantity = int(input("Enter quantity: "))

        if quantity < 0:
            raise ValueError(f"Invalid quantity: {quantity}")

        if quantity > self.inventory[product].quantity:
            raise InsufficientInventoryError(
                f"Insufficient inventory: {self.inventory[product].quantity}"
            )

        self.cart[product] += quantity
        self.inventory[product].quantity -= quantity

    def _print_receipt(self, discount: float) -> None:
        total = 0
        print("Receipt:")
        for item, quantity in self.cart.items():
            item_price = self.inventory[item].price
            item_total = item_price * quantity
            total += item_total
            print(
                f"{item.name}: {item_price / 100:.2f} x{quantity} = {item_total / 100:.2f}"
            )
        print(f"Your total is: {total / 100:.2f}")

        if discount:
            total = int(total * (1 - discount))
            print(f"Discounted total: {total / 100:.2f}")

        print(f"Checkout time: {datetime.datetime.now()}")

    def checkout(self) -> None:
        self._print_receipt(discount=self._get_discount())
        raise SystemExit(0)

    @staticmethod
    def exit() -> None:
        print("Exiting")
        raise SystemExit(0)

    def _get_discount(self) -> float:
        if (discount_code := input("Enter discount code (optional): ")) == "":
            return 0.0

        if discount := self.discount_codes.get(discount_code, 0.0):
            print(f"{discount * 100:.0f}% Discount applied")
        else:
            print("Invalid discount code, proceeding without discount")

        return discount


def get_action() -> Action:
    return take_enum_input(input_type=Action)


def take_enum_input[T: EnumeratedEnum](input_type: type[T]) -> T:
    return input_type(
        input(f"Choose {input_type.__name__.title()}:\n{input_type.list_choices()}\n: ")
    )


def main() -> None:
    cash_registry = CashRegistry(
        inventory={
            Product.APPLE: ProductInfo(price=120, quantity=10),
            Product.BANANA: ProductInfo(price=50, quantity=20),
            Product.COOKIE: ProductInfo(price=250, quantity=30),
        },
        discount_codes={"10OFF": 0.1, "20OFF": 0.2},
    )

    while True:
        try:
            action = take_enum_input(input_type=Action)
            cash_registry.action_map[action]()
        except ValueError as e:
            print(f"Invalid input. Please try again. Error: {e}")
        except InsufficientInventoryError as e:
            print(e)


if __name__ == "__main__":
    main()
