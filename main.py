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


def main():
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = store.Store(product_list)

if __name__ == "__main__":
    main()