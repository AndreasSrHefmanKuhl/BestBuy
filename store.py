from typing import List, Tuple
import products



class Store:

    def __init__(self,products_list:list[products.Product]):

        self.products = products_list

    def add_product(self,product:products.Product):

        self.products.append(product)
        return f"{product} has been added to the store"#

    def remove_product(self,product:list[products.Product]):

        try:
            self.products.remove(product)

        except ValueError:
            print(f"Warning: Product '{product.name}' not found in store and could not be removed.")

    def get_total_quantity(self) -> int:

        total = 0
        for product in self.products:
            total += product.get_quantity()
        return total

    def get_all_products(self) -> List[products.Product]:

        return [product for product in self.products if product.is_active()]


    def order(self, shopping_list: List[Tuple[products.Product, int]]) -> float:

        total_price = 0.0
        print("\n--- Processing Order ---")

        for product, quantity in shopping_list:
            try:
                item_price = product.buy(quantity)
                total_price += item_price
                print(f"Purchased{quantity} x {product.name} for ${item_price:.2f}")
            except Exception as e:
                print(f"Order failed for item {product.name}: {e}")
                raise Exception(f"Order failure. Halting purchase: {e}")

        print("--- Order Complete ---")
        return total_price







