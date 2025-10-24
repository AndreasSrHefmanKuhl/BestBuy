# products.py

class Product:
    """
    Represents a specific type of product available in the store.
    Encapsulates information including the product's name, price,
    quantity, and active status.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initializes a new Product instance.

        :param name: Product name (non-empty string).
        :param price: Price per unit (float, non-negative).
        :param quantity: Initial stock (int, non-negative).
        :raises Exception: If validation fails.
        """
        if not name:
            raise Exception("Product name can't be empty.")
        if price < 0:
            raise Exception("Price cannot be negative.")
        if quantity < 0:
            raise Exception("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """Returns the current stock quantity."""
        return self.quantity

    def set_quantity(self, quantity: int):
        """
        Updates the stock quantity and deactivates product if it reaches zero.
        """
        if quantity < 0:
            raise Exception("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def activate(self):
        """Sets the product as active."""
        self.active = True

    def deactivate(self):
        """Sets the product as inactive."""
        self.active = False

    def is_active(self) -> bool:
        """Checks if the product is active."""
        return self.active

    def show(self) -> str:
        """Returns a string describing the product."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        """
        Processes a purchase for a given quantity.

        :param quantity: Number of units to buy.
        :return: Total price for the purchase.
        :raises Exception: For invalid or unavailable purchases.
        """
        if not self.is_active():
            raise Exception(f"Cannot buy {self.name}: Product is inactive.")

        if quantity <= 0:
            raise Exception("Quantity to buy must be positive.")

        if quantity > self.quantity:
            raise Exception(
                f"Cannot buy {quantity} units of {self.name}. "
                f"Only {self.quantity} available."
            )

        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)
        return total_price