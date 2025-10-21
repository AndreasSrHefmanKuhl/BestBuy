import products
import store

def list_products(store_instance:store.Store):
    """prints the listed products in store"""
    print("\n--- Available Products ---")
    active_products = store_instance.get_all_products()

    if not active_products:
        print("No products currently in stock")
        return

    for i, product in enumerate(active_products):
        # need i for indexing for user selection later
        print(f"{i+1}. ", end="")
        product.show()
    print("--------------------------------")

def make_order(store_instance: store.Store):
    """guides user through creating and placing an order"""
    global selected_product
    active_products = store_instance.get_all_products()

    if not active_products:
        print("Can't place an order, Product is not active")
        return

    shopping_list= []

    print("\n--- Place an Order ---")

    while True:
        list_products(store_instance)

        try:
            choice = input("Enter product number to add (or 0 to finalize order)")
            product_index = int(choice)-1

            if product_index < -1:
                print("Invalid choice. Please enter a valid number")
                continue
            if product_index == -1: # User entered zero order is done then
                break
            if 0 <= product_index < len(active_products):
                selected_product = active_products[product_index]

            # get quantity
            quantity_str = input(f"Enter quantity for {selected_product.name}: ")
            quantity = int(quantity_str)

            if quantity <=0:
                print("Quantity must be a postiv number.")
                continue





def main():
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250)]

    best_buy = store.Store(product_list)

if __name__ == "__main__":
    main()