from flask import jsonify, request
from flask_restx import Resource, Namespace

from model.Customer import Customer
from model.Product import Product
from model.data import my_shop

ProductAPI = Namespace('product',
                       description='Product Management')


@ProductAPI.route('/')
class AddProductA(Resource):
    @ProductAPI.doc(params={'name': 'Product name',
                            'expiry': 'expiry date',
                            'category': 'product category',
                            'serial_num': 'serial_num'})
    def post(self):
        # get the post parameters
        args = request.args
        name = args['name']
        expiry = args['expiry']
        category = args['category']
        serial_num = args['serial_num']

        new_product = Product(name, expiry, category, serial_num)
        # add the product
        my_shop.addProduct(new_product)
        return jsonify(new_product)

    @ProductAPI.doc(description="Get a list of all the products")
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

