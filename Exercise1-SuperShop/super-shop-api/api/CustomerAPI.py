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
                # 'email': 'Customer Email',
                'dob': 'Customer birthday'})
    def put(self, customer_id):
        args = request.args
        address = args['address']
        name = args['name']
        # email = args['email']
        dob = args['dob']
        custumer = my_shop.getCustomer(customer_id)
        if custumer is None:
            return jsonify("Customer not found")
        custumer.set_name(name)
        custumer.set_address(address)
        custumer.set_dob(dob)
        return jsonify("Custumer data is updated")


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
        temp = customer.generate_temp_password()
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
            return jsonify("Password is updated")


@CustomerAPI.route('/<customer_id>/add2cart ')
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
        customer.add2cart(name, quantity)
        return jsonify('Product added to the cart')