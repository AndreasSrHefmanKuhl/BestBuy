from csv import excel


class Product:

    def __init__(self,name=str,price=float,quantity=int):

        if not name:
            raise Exception("Product name cant be empty")
        if price <=0:
            raise Exception("Price can not be negative")
        if quantity <=0:
            raise Exception("If quantity is below zero , we can not sell or buy any")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True