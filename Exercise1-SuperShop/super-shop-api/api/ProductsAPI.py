from flask import jsonify, request
from flask_restx import Resource, Namespace

from model.Customer import Customer
from model.Product import Product
from model.data import my_shop

ProductAPI = Namespace('product',
                       description='Product Management')

ProductsAPI = Namespace('products',
                        description='All the products')


@ProductAPI.route('/')
class AddProductA(Resource):
    @ProductAPI.doc(description='Add a new product',
                    params={'name': 'Product name',
                            'expiry': 'Expiry date',
                            'category': 'Product category',
                            'serial_num': 'Serial_num',
                            'price': 'Price'})
    def post(self):
        # get the post parameters
        args = request.args
        name = args['name']
        expiry = args['expiry']
        category = args['category']
        serial_num = args['serial_num']
        price = args['price']
        is_float = False
        try:
            float(price)
            is_float = True
        except ValueError:
            is_float = False
        if is_float is True:
            price = float(price)
            new_product = Product(name, expiry, category, serial_num, price)
            # add the product
            my_shop.addProduct(new_product)
            return jsonify(new_product)
        else:
            return jsonify('Invalid price')


@ProductsAPI.route('/')
class GetProducts(Resource):
    @ProductsAPI.doc(description="Get a list of all the products")
    def get(self):
        return jsonify(my_shop.products)


@ProductAPI.route('/<product_id>')
class SpecificProductOps(Resource):
    @ProductAPI.doc(description="Delete an existing product")
    def delete(self, product_id):
        product = my_shop.getProduct(product_id)
        if not product:
            return jsonify("Product was not found")
        my_shop.removeProduct(product)
        return jsonify("Product was removed")

    @ProductAPI.doc(description="Get an existing product")
    def get(self, product_id):
        product = my_shop.getProduct(product_id)
        if not product:
            return jsonify("Product was not found")
        return jsonify(product)

    @ProductAPI.doc(description="Change the stock of an existing product",
                    params={'quantity': 'quantity'})
    def put(self, product_id):
        args = request.args
        quantity = args['quantity']
        product = my_shop.getProduct(product_id)
        if not product:
            return jsonify("Product not found")
        if quantity.isnumeric() is True:
            product.changeStock(int(quantity))
            return jsonify("Stock is updated")
        else:
            return jsonify("Quantity should be a number")


@ProductAPI.route('/sell')
class ProductSell(Resource):
    @ProductAPI.doc(
        decription="Sell a product",
        params={'cust_id': 'ID of the buyer',
                'quantity': 'Quantity',
                'prod_id': 'Product ID'})
    def put(self):
        args = request.args
        cust_id = args['cust_id']
        quant = args['quantity']
        prod_id = args['prod_id']
        customer = my_shop.getCustomer(cust_id)
        product = my_shop.getProduct(prod_id)
        if not customer:
            return jsonify("Customer not found")
        if not product:
            return jsonify("Product not found")
        if quant.isnumeric() is True:
            quantity = int(quant)
            if int(quantity) > product.getQuantity():
                return jsonify("There is not enough products in the store")
            product.sell(int(quantity))
            name = product.getName()
            customer.buy(name, quantity)
            return jsonify("The purchase has been made")
        else:
            return jsonify("Quantity is not a number")


@ProductAPI.route('/remove')
class ProductRemove(Resource):
    @ProductAPI.doc(
        decription="Remove a product",
        params={'reason': 'Reason for removal',
                'prod_id': 'Product ID'})
    def put(self):
        args = request.args
        reason = args['reason']
        prod_id = args['prod_id']
        product = my_shop.getProduct(prod_id)
        if not product:
            return jsonify("Product not found")
        product.setQuantity(0)
        return jsonify(f"Product was removed, because {reason}")
