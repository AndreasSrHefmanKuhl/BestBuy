from products import Product
from store import Store


def main():
    """Test function for the Store class."""

    # 1. Setup Products
    print("--- Initializing Products and Store ---")
    mac = Product("MacBook Air M2", price=1450, quantity=100)
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    pixel = Product("Google Pixel 7", price=500, quantity=250)

    product_list = [mac, bose, pixel]

    # 2. Setup Store
    best_buy = Store(product_list)

    # 3. Test get_total_quantity
    initial_total_quantity = best_buy.get_total_quantity()
    print(f"Total quantity of all items in store: {initial_total_quantity}")  # Expected: 100 + 500 + 250 = 850

    # 4. Test add_product
    new_item = Product("Air Fryer", price=150, quantity=50)
    best_buy.add_product(new_item)
    print(f"Total quantity after adding 'Air Fryer': {best_buy.get_total_quantity()}")  # Expected: 850 + 50 = 900

    # 5. Test get_all_products
    active_products = best_buy.get_all_products()
    print(f"Number of active products: {len(active_products)}")  # Expected: 4
    for prod in active_products:
        print(f"- Active Product: {prod.name}")

    # 6. Test order method
    print("\n--- Testing Order Purchase ---")
    try:
        # Order 1 Mac, 2 Bose
        shopping_list = [(mac, 1), (bose, 2)]
        price = best_buy.order(shopping_list)
        print(f"Order cost: ${price:.2f}")  # Expected: (1*1450) + (2*250) = 1950.00

        # Check remaining quantities
        print(f"MacBook remaining: {mac.get_quantity()}")  # Expected: 99
        print(f"Bose remaining: {bose.get_quantity()}")  # Expected: 498

    except Exception as e:
        print(f"An error occurred during order processing: {e}")

    # 7. Test order failure (Insufficient Stock)
    print("\n--- Testing Order Failure (Insufficient Stock) ---")
    # This item will cause the order to fail and halt
    shopping_list_fail = [(mac, 1), (pixel, 1000), (bose, 1)]
    try:
        best_buy.order(shopping_list_fail)
    except Exception as e:
        print(f"Order failed successfully (as expected): {e}")

    # Note: If the order fails, Mac's quantity (99) would still be updated
    # for the first item bought before the failure.
    print(f"MacBook quantity after failed order attempt: {mac.get_quantity()}")

    # 8. Test remove_product
    print("\n--- Testing Remove Product ---")
    best_buy.remove_product(new_item)
    print(
        f"Total quantity after removing 'Air Fryer': {best_buy.get_total_quantity()}")  # Expected: 900 - 50 = 850 (adjusting for previous buys)


# ---

if __name__ == "__main__":
    # The Product class is needed, so ensure products.py is in the same directory
    main()