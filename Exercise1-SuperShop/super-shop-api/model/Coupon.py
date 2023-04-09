from datetime import date


class Coupon:
    def __init__(self, num, category, start, end, percentage):
        self.num = num
        self.category = category
        self.start = start
        self.end = end
        self.percentage = percentage

    def isValid(self, coupon):
        today = str(date.today())
        start_date = coupon.start
        end_date = coupon.end
        if start_date <= today <= end_date:
            return True
        else:
            return False
