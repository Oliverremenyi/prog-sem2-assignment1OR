class Shop:
    def __init__(self):
        self.customers = []
        self.products = []
        self.coupons = []

    def addProduct(self, p):
        self.products.append(p)

    def getProducts(self):
        return self.products

    def addCustomer(self, c):
        c1 = self.getCustomerbyEmail(c.email)
        if c1 is None:  # customer does not exist with the given email address
            self.customers.append(c)
            return True
        else:
            return False

    def removeCustomer(self, c):
        self.customers.remove(c)

    def getCustomer(self, cust_id):
        for c in self.customers:
            if c.customer_id == cust_id:
                return c

    def getCustomerbyEmail(self, email):
        for c in self.customers:
            if c.email == email:
                return c

    def getProduct(self, prod_id):
        for product in self.products:
            if product.product_id == prod_id:
                return product

    def removeProduct(self, product):
        self.products.remove(product)

    def addCoupon(self, coupon):
        c1 = self.getCouponByNumber(coupon.num)
        if c1 is None:  # customer does not exist with the given email address
            self.coupons.append(coupon)
            return True
        else:
            return False

    def getCouponByNumber(self, number):
        for c in self.coupons:
            if c.num == number:
                return c
