import uuid


class Customer:
    def __init__(self, name, email, address, dob):
        self.customer_id = str(uuid.uuid4())
        self.name = name
        self.address = address
        self.email = email
        self.bonus_points = 0
        self.status = "unverified"
        self.verification_token = str(uuid.uuid4())[:5]
        self.dob = dob
        self.purchase_history = {}
        self.password = None
        self.temp_pass = None
        self.shopping_cart = {}
    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name

    def get_points(self):
        return self.bonus_points

    def addPoints(self, points):
        self.bonus_points += points

    def set_address(self, new_address):
        self.address = new_address

    def get_address(self):
        return self.address

    def set_dob(self, new_dob):
        self.dob = new_dob

    def get_dob(self):
        return self.dob

    def verify(self, token):
        if self.verification_token == token:
            self.status = "verified"
            self.verification_token = None
        return self.status == "verified"

    def generate_temp_password(self):
        temp = str(uuid.uuid4())[:5]
        self.temp_pass = temp
        return temp

    def set_temp_pass(self):
        self.temp_pass = None

    def get_temp_passw(self):
        return self.temp_pass

    def pwreset(self, new_password):
        self.password = new_password

    def buy(self, product, quantity):
        self.purchase_history.update({product: quantity})

    def add2cart(self, product, quantity):
        # quantity = int(quan)
        in_cart = False
        for i in self.shopping_cart.keys():
            if i == product:
                product_quantity = self.shopping_cart[i]
                self.shopping_cart.update({product: product_quantity + quantity})
                in_cart = True
        if not in_cart:
            self.shopping_cart.update({product: quantity})

    def del_from_cart(self, product):
        in_cart = False
        for i in self.shopping_cart.keys():
            if i == product:
                in_cart = True
        if in_cart is True:
            del self.shopping_cart[product]

    def make_order(self):
        sum = 0
        for product, quantity in self.shopping_cart.items():
            for prod in my_shop.products:
                if prod.getName() == product:
                    sum += prod.getPrice() * quantity
        bonus_points = round(sum / 10, 2)
        self.bonus_points += bonus_points
