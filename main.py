import products
import store
import ui_functions


def main():

    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250)]

    best_buy = store.Store(product_list)


    ui_functions.start(best_buy)


if __name__ == "__main__":
    main()