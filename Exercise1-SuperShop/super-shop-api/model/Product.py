import uuid


class Product:
    def __init__(self, name, expiry, category, serial_num, price):
        self.product_id = str(uuid.uuid4())
        self.name = name
        self.expiry = expiry
        self.category = category
        self.serial_num = serial_num
        self.quantity = 1
        self.price = price

    def get_category(self):
        return self.category

    def __repr__(self):
        return self.name

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def sell(self, quantity):
        self.quantity -= quantity

    def changeStock(self, quantity):
        self.quantity += quantity

    def setQuantity(self, quantity):
        self.quantity = quantity

    def getQuantity(self):
        return self.quantity

    def remove(self):
        pass

    def reorder(self):
        pass
