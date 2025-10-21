from products import Product

"""Step 2 - Store Class
Now we have a bunch of instances of Product, but we might need something to connect them all together. Let’s create a class called Store that will hold all of these products, and will allow the user to make a purchase of multiple products at once.
Did you know?
This design concept is called composition - where a class holds reference to one or more objects of other classes. This is also called a “has-a” relation.
Specification
The Store class will contain one variable - a list of products that exist in the store. It will expose the following methods:
add_product(self, product)
Example:
bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = products.Product("MacBook Air M2", price=1450, quantity=100)

# instance of a store
best_buy = Store([bose, mac])

pixel = products.Product("Google Pixel 7", price=500, quantity=250)
best_buy.add_product(pixel)

remove_product(self, product)
Removes a product from store.

get_total_quantity(self) -> int
Returns how many items are in the store in total.

get_all_products(self) -> List[Product]
Returns all products in the store that are active.

order(self, shopping_list) -> float
Gets a list of tuples, where each tuple has 2 items:

Product (Product class) and quantity (int).
Buys the products and returns the total price of the order.

Example:
bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = products.Product("MacBook Air M2", price=1450, quantity=100)

best_buy = Store([bose, mac])
price = best_buy.order([(bose, 5), (mac, 30), (bose, 10)])
print(f"Order cost: {price} dollars.")
Task
In the file store.py, create the new class Store according to the specification above.
When you’re done, you can check that everything works using this code:
product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
               ]

best_buy = Store(product_list)
products = best_buy.get_all_products()
print(best_buy.get_total_quantity())
print(best_buy.order([(products[0], 1), (products[1], 2)]))
Put it in your main function in the same file, and make sure you are handling the importing in the right manner.
"""


class Store:

    def __init__(self,products:list[Product]):

        self.products = products

    def add_product(self,product:Product):

        self.products.append(product)
        return f"{product} has been added to the store"#

    def remove_product(self,product:list[Product]):
        try:
            self.products.remove(product)
        except ValueError:
            print(f"Warning: Product '{product.name}' not found in store and could not be removed.")







