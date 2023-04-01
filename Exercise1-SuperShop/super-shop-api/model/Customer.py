import uuid
import random


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

    def set_name(self, newName):
        self.name = newName

    def get_name(self):
        return self.name

    def set_address(self, newAddress):
        self.address = newAddress

    def get_address(self):
        return self.address

    def set_dob(self, newDob):
        self.dob = newDob

    def get_dob(self):
        return self.dob

    def verify(self, token):
        if self.verification_token == token:
            self.status = "verified"
            self.verification_token = None
        return self.status == "verified"

    def generate_temp_password(self):
        upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
        lower_case = []
        nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        special = ['!', '?', '@', '&', '#', '*']
        temp = ""
        for i in upper:
            lower_case.append(i.lower())
        rand_upper = [random.choice(upper) for i in range(3)]
        rand_lower = [random.choice(lower_case) for k in range(3)]
        rand_special = [random.choice(special) for k in range(3)]
        rand_num = [random.choice(nums) for k in range(3)]
        for i in rand_upper:
            temp += i
        for i in rand_lower:
            temp += i
        for i in rand_special:
            temp += i
        for i in rand_num:
            temp += i
        self.temp_pass = temp
        return temp

    def get_temp_passw(self):
        return self.temp_pass

    def pwreset(self, new_password):
        self.password = new_password

    def buy(self, product, quantity):
        self.purchase_history.update({product: quantity})

    def add2cart(self, product, quantity):
        self.shopping_cart.update({product: quantity})
