import uuid
import datetime
from datetime import date


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
        self.orders = []

    def get_purchase_history(self):
        return self.purchase_history

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
        in_history = False
        for key in self.purchase_history.keys():
            if key == product:
                self.purchase_history[key] += quantity
                in_history = True
        if not in_history:
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
        new_dict = {}
        for prod, quantity in self.shopping_cart.items():
            if prod == product:
                continue
            else:
                new_dict.update({prod: quantity})
        self.shopping_cart = new_dict

    def get_shopping_cart(self):
        return self.shopping_cart

    def setShoppingCart(self, cart):
        self.shopping_cart = cart

    def order(self, product, quantity, order_date, delivery_date):
        lst = [product, quantity, order_date, delivery_date]
        self.orders.append(lst)

    def get_order(self):
        return self.orders

    def current_date(self):
        return date.today()

    def delivery_date(self, order_date):
        delivery_time = datetime.timedelta(days=5)
        delivery_date = order_date + delivery_time
        return delivery_date

    def ifReturnable(self):
        lst = []
        for i in self.orders:
            order_date = i[1]
            two_week = datetime.timedelta(days=14)
            returnable = order_date + two_week
            today = date.today()
            if order_date <= today <= returnable:
                lst.append(i[0])
        return lst
