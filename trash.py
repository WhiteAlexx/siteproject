# import time

# print(time.time() - time.mktime(time.strptime(str('2024-7-30 15:36:00+00:00'.split('+')[0]), "%Y-%m-%d %H:%M:%S")))

import decimal


class Product():
    price_low = decimal.Decimal(100)
    discount_low = decimal.Decimal(0)
    residual = str

    def residual_cost_low(self):
        if self.residual:
            list = self.residual_list()
            return [float(self.sell_price_low()) * i for i in list]

    def sell_price_low(self):
        if self.discount_low:
            return round(self.price_low - self.price_low * self.discount_low / 100, 2)
        return self.price_low

    def residual_list(self):
        if ',' in  self.residual:
            self.residual =  self.residual.replace(',', '.')
            return [float(i) for i in self.residual.split()]



# def residual_list(residual):
#     if ',' in residual:
#         residual = residual.replace(',', '.')
#         return [float(i) for i in residual.split()]
# def residual_cost_low(residual, price):
#     return [price * i for i in residual_list(residual)]


# price = 100

# while True:
#     print("Остатки: ", residual)
#     buy = input("Какие остатки хотите забрать (порядковые номера, через пробел): ")
#     price = 100

#     for ind in buy.split():
#         print('Купили: ', residual_list(residual)[int(ind) - 1], 'штук, заплатив:')
#         print(residual_list(residual)[int(ind) - 1] * price, 'руб')

#     lst = residual.split()
#     for ind in buy.split():
#         x = residual.split()[int(ind) - 1]
#         print(x, type(x))
#         lst.remove(x)
#         print(lst)

#     residual = " ".join(lst)

# price_low = 100
# discount_low = 0
# residual = '3 2,5 5 8 5'

x = Product
x.price_low = 1000
x.discount_low = 10
x.residual = '3 2,2 5 4.5 8 5'

print(Product.sell_price_low(x))

print(Product.residual_list(x))

print(Product.residual_cost_low(x))
