from flask import jsonify, request
from flask_restx import Resource, Namespace
from model.data import my_shop

from model.Coupon import Coupon

CouponApi = Namespace("coupons", description="Coupon management")


@CouponApi.route("/")
class GetCoupons(Resource):
    @CouponApi.doc(description="Get all the currently valid coupons")
    def get(self):
        coupons = my_shop.coupons
        output = []
        for coupon in coupons:
            if coupon.isValid(coupon):
                num = coupon.num
                output.append(num)
        if len(output) == 0:
            return jsonify("There are no currently valid coupons")
        return jsonify(output)

    @CouponApi.doc(description="Add a new coupon",
                   params={"number": "Number",
                           "category": "Category",
                           "start": "Start of the validity",
                           "end": 'End of the validity',
                           "percent": "Percentage of the discount"})
    def post(self):
        args = request.args
        number = args['number']
        category = args['category']
        start = args["start"]
        end = args["end"]
        percent = args["percent"]
        if number.isnumeric():
            if len(number) == 10:
                new_coupon = Coupon(number, category, start, end, percent)
                if my_shop.addCoupon(new_coupon):
                    return jsonify(new_coupon)
                else:
                    return jsonify("Coupon already exists with this number")
            else:
                return jsonify("Length of the number must be 10")
        else:
            return jsonify("Number must consist only numbers")
