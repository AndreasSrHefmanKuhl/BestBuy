import products
import store
from typing import List, Tuple


def list_products(store_instance: store.Store):
    """Prints a numbered list of all active products in the store."""
    print("\n--- Available Products ---")
    active_products = store_instance.get_all_products()

    if not active_products:
        print("No active products currently in stock.")
        return

    for i, product in enumerate(active_products):

        print(f"{i + 1}. ", end="")
        product.show()
    print("--------------------------------")


def make_order(store_instance: store.Store):
    """Guides user through creating and placing an order."""


    active_products = store_instance.get_all_products()

    if not active_products:
        print("Can't place an order, no active products available.")
        return

    shopping_list: List[Tuple[products.Product, int]] = []

    print("\n--- Place an Order ---")

    while True:
        # Display current active products with their index
        list_products(store_instance)

        try:
            choice = input("Enter product number to add (or 0 to finalize order): ")

            # This is the product index
            product_index = int(choice) - 1

            if product_index < -1:
                print("Invalid choice. Please enter a valid number.")
                continue

            if product_index == -1:  # User entered 0
                break

            if 0 <= product_index < len(active_products):

                selected_product = active_products[product_index]

                # get quantity
                quantity_str = input(f"Enter quantity for {selected_product.name}: ")
                quantity = int(quantity_str)

                if quantity <= 0:
                    print("Quantity must be a positive number.")
                    continue

                shopping_list.append((selected_product, quantity))
                print(f"Added {quantity} x {selected_product.name} to cart.")


            else:
                print("Invalid product number selected.")

        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            # Catching generic exceptions just in case
            print(f"An unexpected error occurred during selection: {e}")

    if not shopping_list:
        print("Order cancelled or empty cart.")
        return

    # Process final order
    try:
        total_price = store_instance.order(shopping_list)
        print(f"\n✅ SUCCESS! Total Order Price: ${total_price:.2f}")
    except Exception as e:
        print(f"\n❌ ORDER FAILED: {e}")


def start(store_instance: store.Store):
    """The main function to display the menu and handle user input."""
    while True:
        print("\n===============================")
        print("         Store Menu 🛍️         ")
        print("===============================")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        print("-------------------------------")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            list_products(store_instance)

        elif choice == '2':
            total_items = store_instance.get_total_quantity()
            print(f"\n🛒 Total items in stock: {total_items}")

        elif choice == '3':
            make_order(store_instance)

        elif choice == '4':
            print("\n👋 Thank you for visiting! Goodbye.")
            break

        else:
            print("\n❌ Invalid choice. Please enter a number from 1 to 4.")