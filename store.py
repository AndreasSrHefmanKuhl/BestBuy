# store.py

from typing import List, Tuple
import products


class Store:
    """Represents a store that manages products and handles orders."""

    def __init__(self, products_list: List[products.Product]):
        self.products = products_list

    def add_product(self, product: products.Product):
        """Adds a new product to the store."""
        self.products.append(product)

    def remove_product(self, product: products.Product):
        """Removes a product from the store if it exists."""
        try:
            self.products.remove(product)
        except ValueError:
            print(f"Warning: Product '{product.name}' not found in store.")

    def get_total_quantity(self) -> int:
        """Returns the total number of product units available in store."""
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> List[products.Product]:
        """Returns a list of all active products."""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[Tuple[products.Product, int]]) -> float:
        """
        Processes a customer's order.

        :param shopping_list: A list of (Product, quantity) tuples.
        :return: Total price of the order.
        :raises Exception: If any product in the order cannot be purchased.
        """
        total_price = 0.0
        print("\n--- Processing Order ---")

        for product, quantity in shopping_list:
            try:
                item_price = product.buy(quantity)
                total_price += item_price
                print(f"Purchased {quantity} x {product.name} for ${item_price:.2f}")
            except Exception as e:
                print(f"Order failed for item {product.name}: {e}")
                raise Exception(f"Order failure. Halting purchase: {e}")

        print("--- Order Complete ---")
        return total_price