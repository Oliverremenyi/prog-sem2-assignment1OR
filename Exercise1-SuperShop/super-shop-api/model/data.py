# the instance of shop, where all data is stored.
from model.Customer import Customer
from model.Product import Product
from model.Shop import Shop
from model.Coupon import Coupon

my_shop = Shop()

# Test data
c1 = Customer("Markus Muelle", "markus.mueller@email.test", "1101 Vienna", "10.09.2001")
my_shop.addCustomer(c1)

c2 = Customer("Sam Wright", "sam.wright@email.test", "1102 Vienna", "10.09.2002")
my_shop.addCustomer(c2)

c3 = Customer("Callum Hart", "callum.hart@email.test", "1103 Vienna", "10.10.2001")
my_shop.addCustomer(c3)

c4 = Customer("Adam Smith", "adam.smith@email.test", "1104 Vienna", "11.09.2001")
my_shop.addCustomer(c4)

c5 = Customer("John Doe", "john.doe@email.test", "1105 Vienna", "03.09.2001")
my_shop.addCustomer(c5)

product1 = Product("banana", "23.04.2023", "fruit", "012345", 3.50)
my_shop.addProduct(product1)

product2 = Product("apple", "20.04.2023", "fruit", "1234564", 2.50)
my_shop.addProduct(product2)

product3 = Product("butter", "30.04.2023", "food", "512352", 1.50)
my_shop.addProduct(product3)

product4 = Product("bread", "26.04.2023", "food", "927439", 2.30)
my_shop.addProduct(product4)

product5 = Product("chocolate", "23.06.2023", "sweets", "823487", 1.60)
my_shop.addProduct(product5)

product6 = Product("snack", "23.06.2023", "sweets", "823487", 1.60)
my_shop.addProduct(product6)

product7 = Product("mars", "23.06.2023", "sweets", "823487", 1.60)
my_shop.addProduct(product7)

product8 = Product("asd", "23.06.2023", "asd", "823487", 1.60)
my_shop.addProduct(product8)

coupon1 = Coupon('1234567890', "food", "2023-04-08", "2023-04-15", 10)
my_shop.addCoupon(coupon1)

coupon2 = Coupon('1254589788', "food", "2023-04-08", "2023-04-15", 10)
my_shop.addCoupon(coupon2)

coupon3 = Coupon('7845165878', "food", "2023-04-05", "2023-04-15", 10)
my_shop.addCoupon(coupon3)

coupon4 = Coupon('7854964245', "sweets", "2023-03-08", "2023-04-07", 10)
my_shop.addCoupon(coupon4)
