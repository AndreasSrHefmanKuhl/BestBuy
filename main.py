from products import Product


def main():
    """Test function for the Product class."""


    print("--- Testing Initial Products and Buys ---")
    try:
        bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
        mac = Product("MacBook Air M2", price=1450, quantity=100)

        # Test buy
        bose_purchase_price = bose.buy(50)
        print(f"Price of Bose purchase: {bose_purchase_price}")

        mac_purchase_price = mac.buy(100)
        print(f"Price of Mac purchase: {mac_purchase_price}")

        # Check active status after a buy that depletes stock
        print(f"MacBook Air M2 active after purchase: {mac.is_active()}")

        bose.show()
        mac.show()

    except Exception as e:
        print(f"An error occurred during initial setup/buy: {e}")

if __name__ == '__main__':
    main()