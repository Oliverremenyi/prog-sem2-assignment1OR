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

    def verify(self, token):
        if self.verification_token == token:
            self.status = "verified"
            self.verification_token = None
        return self.status == "verified"

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

    def buy(self, product, quantity):
        self.purchase_history.update({product: quantity})
