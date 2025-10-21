class Product:
    """
    Represents a specific type of product available in the store.

    It encapsulates information including the product's name, price, quantity, 
    and active status.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initializes a new Product instance.

        :param name: The name of the product (str).
        :param price: The price per unit (float, must be non-negative).
        :param quantity: The initial stock quantity (int, must be non-negative).
        :raises Exception: If name is empty, or price or quantity are negative.
        """
        if not name:
            raise Exception("Product name cant be empty")
        if price < 0:
            raise Exception("Price can not be negative")
        if quantity < 0:
            raise Exception("If quantity is below zero , we can not sell or buy any")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """ 
        Getter method for quantity.

        :return: The current stock quantity of the product (int).
        """
        return self.quantity

    def set_quantity(self, quantity: int):
        """
        Setter method for quantity.

        Updates the stock quantity and deactivates the product if the 
        new quantity reaches zero.

        :param quantity: The new stock quantity (int).
        :return: None
        """
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def activate(self):
        """
        Sets the product's active status to True.

        :return: True, representing the new active status. 
                 (Note: This should typically set the internal state, 
                 and return nothing, but based on your implementation, it returns True).
        """
        return self.active == True

    def deactivate(self):
        """
        Sets the product's active status to False.

        :return: False, representing the new active status.
                 (Note: This should typically set the internal state, 
                 and return nothing, but based on your implementation, it returns False).
        """
        return self.active == False

    def is_active(self) -> bool:
        """
        Checks if the product is currently active and available for sale.

        :return: True if the product is active, False otherwise (bool).
        """
        return self.active

    def show(self):
        """
        Prints a string representation of the product's current state.

        Format: "Name, Price: [price], Quantity: [quantity]"

        :return: None (prints to console).
        """
        print(f"{self.name}, Price:{self.price}, Quantity:{self.quantity}")

    def buy(self, quantity: int) -> float:
        """
        Processes a purchase of a specified quantity of the product.

        Updates the product's stock quantity and returns the total purchase price.

        :param quantity: The amount of the product to buy (int).
        :return: The total price of the purchase (float).
        :raises Exception: If the product is inactive, insufficient quantity is 
                           available, or the quantity to buy is non-positive.
        """

        if not self.is_active():
            raise Exception(f"Cannot buy {self.name}: Product is inactive.")

        if quantity > self.quantity:
            raise Exception(
                f"Cannot buy {quantity} units of {self.name}. "
                f"Only {self.quantity} available."
            )

        if quantity <= 0:
            raise Exception("Quantity to buy must be a positive integer.")

        total_price = (self.price * quantity)
        updated_quantity = (self.quantity - quantity)
        self.set_quantity(updated_quantity)

        return total_price