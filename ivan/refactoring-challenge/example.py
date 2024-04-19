import datetime
import sys, os


timeNow = datetime.datetime.now()


product_prices = {'apple': 1.2, 'banana': 0.5, 'cookie': 2.5}
product_inventory = {'apple': 10, 'banana': 20, 'cookie': 30}
Cart = []

def Add_To_Cart(product, quantity=1, cart=Cart):
    cart.extend([product] * quantity)
    product_inventory[product] -= quantity

def Checkout(cart=Cart):
    global timeNow
    total = 0
    for item in cart:
        total += product_prices[item]
    print(f'Your total is: {total}')
    print(f"Checkout time: {timeNow}")
    return total



def apply_discount():
    try:
        total = Checkout()
        discountCode = input("Enter your discount code (e.g., '0.1' for 10% off): ")
        discount = eval(discountCode)
        new_total=total-(total*discount)
        print('After discount:'+f"{new_total}")
        return new_total
    except BaseException:
        pass

def reset_Cart(cart=Cart):
    cart.clear()
    print('Your cart has been emptied')
def calculate_tax(price):
    return price * 0.08

def send_receipt(email):
    print(f"Receipt sent to {email}")

def Main():
    try:
        while True:
            print("Available products: apple, banana, cookie")
            action = input("Choose action: 'add', 'checkout', or 'exit':")
            if action.lower() == 'add':
                product = input("Enter product to add to cart:")
                quantity = input("Enter quantity:")

                quantity = int(quantity)
                Add_To_Cart(product, quantity)

            elif action.lower() == 'checkout':
                if len(Cart) == 0:
                    print("Your cart is empty.")
                    continue
                else:
                    total = Checkout()
                    discount_code = input("Enter your discount code (e.g., '0.1' for 10% off):  ")
                    discount = eval(discount_code)
                    new_total = total - (total * discount)
                    print(f'After discount: {new_total}')
                    return new_total
                    reset_Cart()
                    break
            elif action.lower() == 'exit':
                break
            else:
                print("Invalid action. Please choose 'add', 'checkout', or 'exit'.")
    except BaseException:
        pass


Main()