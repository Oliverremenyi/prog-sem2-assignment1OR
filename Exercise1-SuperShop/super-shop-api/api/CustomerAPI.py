from flask import jsonify, request
from flask_restx import Resource, Namespace

from model.Customer import Customer
from model.data import my_shop

CustomerAPI = Namespace('customer',
                        description='Customer Management')


@CustomerAPI.route('/')
class GeneralCustomerOps(Resource):

    @CustomerAPI.doc(description="Get a list of all customers")
    def get(self):
        return jsonify(my_shop.customers)

    @CustomerAPI.doc(
        description="Register a new customer",
        params={'address': 'Customers address',
                'name': 'Customers name',
                'email': 'Customer Email',
                'dob': 'Customer birthday'})
    def post(self):
        # get the post parameters
        args = request.args
        name = args['name']
        email = args['email']
        address = args['address']
        dob = args['dob']
        new_customer = Customer(name, email, address, dob)
        # add the customer
        if my_shop.addCustomer(new_customer):
            return jsonify(new_customer)
        else:
            return jsonify("Customer with the email address already exists")


@CustomerAPI.route('/<customer_id>')
class SpecificCustomerOps(Resource):
    @CustomerAPI.doc(description="Get data about a particular customer")
    def get(self, customer_id):
        search_result = my_shop.getCustomer(customer_id)
        return jsonify(search_result)  # this is automatically jsonified by flask-restx

    @CustomerAPI.doc(description="Delete an existing customer")
    def delete(self, customer_id):
        c = my_shop.getCustomer(customer_id)
        if not c:
            return jsonify(f"Customer ID {customer_id} was not found")
        my_shop.removeCustomer(c)
        return jsonify(f"Customer with ID {customer_id} was removed")

    @CustomerAPI.doc(
        description="Update customer data",
        params={'address': 'Customers address',
                'name': 'Customers name',
                'dob': 'Customer birthday'})
    def put(self, customer_id):
        args = request.args
        address = args['address']
        name = args['name']
        dob = args['dob']
        customer = my_shop.getCustomer(customer_id)
        if customer is None:
            return jsonify("Customer not found")
        customer.set_name(name)
        customer.set_address(address)
        customer.set_dob(dob)
        return jsonify("Customer data is updated")


@CustomerAPI.route('/verify')
class CustomerVerficiation(Resource):
    @CustomerAPI.doc(
        description="Verify customer email address",
        params={'token': 'Verification Token sent by email',
                'email': 'Customer Email'})
    def put(self):
        args = request.args
        token = args['token']
        email = args['email']
        customer = my_shop.getCustomerbyEmail(email)
        if customer is None:
            return jsonify("Customer not found.")
        if customer.verify(token):
            return jsonify("Customer is now verified.")
        else:
            return jsonify("Invalid token.")


@CustomerAPI.route('/<customer_id>/pwreset')
class CustomerPWReset(Resource):
    @CustomerAPI.doc(
        description="Generate a temporary password and send via email.", )
    def post(self, customer_id):
        customer = my_shop.getCustomer(customer_id)
        if not customer:
            return jsonify("Customer not found")
        customer.generate_temp_password()
        temp = customer.get_temp_passw()
        return jsonify(f"A temporary password is created: {temp}")

    @CustomerAPI.doc(
        description="Allow password reset based on the temporary password",
        params={'temp_pw': 'Password sent by email',
                'new_pw': 'New password'})
    def put(self, customer_id):
        args = request.args
        temp_pw = args['temp_pw']
        new_pw = args['new_pw']
        customer = my_shop.getCustomer(customer_id)
        if not customer:
            return jsonify("Customer not found")
        if temp_pw == customer.get_temp_passw():
            customer.pwreset(new_pw)
            customer.set_temp_pass()
            return jsonify("Password is updated")


@CustomerAPI.route('/<customer_id>/add2cart')
class CustomerAdd2Cart(Resource):
    @CustomerAPI.doc(
        description="Add products to the cart",
        params={'prod_id': 'Product ID',
                'quantity': 'Quantity'})
    def put(self, customer_id):
        args = request.args
        prod_id = args['prod_id']
        quantity = args['quantity']
        customer = my_shop.getCustomer(customer_id)
        product = my_shop.getProduct(prod_id)
        if not customer:
            return jsonify(f"Customer with ID {customer_id} not found")
        if not product:
            return jsonify("Product not found")
        name = product.getName()
        if quantity == "-1":
            customer.del_from_cart(product)
            return jsonify("Product removed from the cart")
        if quantity.isnumeric() is True:
            quanti = int(quantity)
            if quanti == 0:
                return jsonify(f"Cannot add {quanti} amount of {name} to the cart")
            elif quanti < -1:
                return jsonify(f"Cannot add {quanti} amount of {name} to the cart")
            else:
                customer.add2cart(name, quanti)
                return jsonify('Product added to the cart')
        else:
            return jsonify('Quantity is not a number')


# @CustomerAPI.route('/<customer_id>/order')
# class CustomerOrder(Resource):
    # @CustomerAPI.doc(
    #     description="",
    #     params={'shipping_address': 'Shipping Address',
    #             'card_num': 'Credit Card Number'})
    # def put(self, cust_id):
    #     args = request.args
    #     shipping_address = args['shipping_address']
    #     card_num = args['card_num']
    #     customer = my_shop.getCustomer(cust_id)
    #     if not customer:
    #         return jsonify("Customer not found")
    #     customer.make_order()
    #     return jsonify("Order has been made")

@CustomerAPI.route('/<customer_id>/order')
class CustomerPoints(Resource):
    @CustomerAPI.doc(description="Make an order",
                     params={'shipping_address': 'Shipping Address',
                             'card_num': 'Card number'})
    def post(self, customer_id):
        args = request.args
        shipping_address = args['shipping_address']
        card_num = args['card_num']
        customer = my_shop.getCustomer(customer_id)
        if not customer:
            return jsonify("Customer not found")
        customer.make_order()
        return jsonify("Order has been made")


@CustomerAPI.route('/<customer_id>/points')
class CustomerPoints(Resource):
    @CustomerAPI.doc(description="Earned bonus points")
    def get(self, customer_id):
        customer = my_shop.getCustomer(customer_id)
        if not customer:
            return jsonify("Customer not found")
        points = customer.get_points()
        return jsonify(points)

    @CustomerAPI.doc(description="Add bonus points",
                     params={"points": 'points'})
    def put(self, customer_id):
        args = request.args
        points = args["points"]
        customer = my_shop.getCustomer(customer_id)
        if not customer:
            return jsonify("Customer not found")
        if points.isnumeric():
            customer.addPoints(int(points))
            return jsonify("Points have been added")
        else:
            return jsonify("Points have to be integers")
