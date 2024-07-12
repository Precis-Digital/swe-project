from typing import Protocol


class PaymentStrategy(Protocol):
    def pay(self, amount: float) -> None: ...


class CreditCardPayment:
    def __init__(self, card_number: str, card_expiry: str, card_cvv: str) -> None:
        self.card_number = card_number
        self.card_expiry = card_expiry
        self.card_cvv = card_cvv

    def pay(self, amount: float) -> None:
        print(f"Paid {amount} using Credit Card ending in {self.card_number[-4:]}.")


class PayPalPayment:
    def __init__(self, email: str) -> None:
        self.email = email

    def pay(self, amount: float) -> None:
        print(f"Paid {amount} using PayPal account {self.email}.")


class BitcoinPayment:
    def __init__(self, wallet_address: str) -> None:
        self.wallet_address = wallet_address

    def pay(self, amount: float) -> None:
        print(f"Paid {amount} using Bitcoin wallet {self.wallet_address}.")


class ShoppingCart:
    def __init__(self) -> None:
        self.items = []
        self.total = 0.0
        self.payment_strategy = None

    def add_item(self, item_name: str, price: float) -> None:
        self.items.append((item_name, price))
        self.total += price

    def set_payment_strategy(self, strategy: PaymentStrategy) -> None:
        self.payment_strategy = strategy

    def checkout(self) -> None:
        if not self.payment_strategy:
            raise Exception("Payment strategy not set!")

        self.payment_strategy.pay(self.total)


if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("Laptop", 1200.00)
    cart.add_item("Headphones", 150.00)

    # Pay with Credit Card
    credit_card_payment = CreditCardPayment("1234567812345678", "12/25", "123")
    cart.set_payment_strategy(credit_card_payment)
    cart.checkout()

    # Pay with PayPal
    paypal_payment = PayPalPayment("user@example.com")
    cart.set_payment_strategy(paypal_payment)
    cart.checkout()

    # Pay with Bitcoin
    bitcoin_payment = BitcoinPayment("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")
    cart.set_payment_strategy(bitcoin_payment)
    cart.checkout()
