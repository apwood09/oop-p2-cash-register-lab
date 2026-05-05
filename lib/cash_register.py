#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=None):
        
        if discount is None:
            try:
                user_input = input("Enter discount percentage: ")
                discount = int(user_input) if user_input != "" else 0
            except (OSError, EOFError, ValueError):
                discount = 0

        if isinstance(discount, int) and 0 <= discount <= 100:
            self.discount = discount
        else:
            print("Not valid discount")
            self.discount = 0
            
        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, item, price, quantity=1):
        self.total += (price * quantity)
        for _ in range(quantity):
            self.items.append(item)
        
        self.previous_transactions.append({
            "item": item, 
            "price": price, 
            "quantity": quantity, 
            "line_total": price * quantity
        })

    def apply_discount(self):
        if not self.previous_transactions or self.discount == 0:
            print("There is no discount to apply.")
            return

        discount_amount = (self.discount / 100) * self.total
        self.total -= discount_amount

        if isinstance(self.total, float) and self.total.is_integer():
            self.total = int(self.total)

        print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        last_tx = self.previous_transactions.pop()
        self.total -= last_tx["line_total"]
        for _ in range(last_tx.get("quantity", 1)):
            if last_tx["item"] in self.items:
                self.items.remove(last_tx["item"])