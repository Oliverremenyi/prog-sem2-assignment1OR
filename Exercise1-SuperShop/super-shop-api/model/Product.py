import uuid


class Product:
    def __init__(self, name, expiry, category, serial_num):
        self.product_id = str(uuid.uuid4())
        self.name = name
        self.expiry = expiry
        self.category = category
        self.serial_num = serial_num
