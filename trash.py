# import time

# print(time.time() - time.mktime(time.strptime(str('2024-7-30 15:36:00+00:00'.split('+')[0]), "%Y-%m-%d %H:%M:%S")))


def residual_list(residual):
    if ',' in residual:
        residual = residual.replace(',', '.')
        return [float(i) for i in residual.split()]
def residual_cost_low(residual, price):
    return [price * i for i in residual_list(residual)]

residual = '3 2,25 5 8 4.5 5'
price = 100

while True:
    print("Остатки: ", residual, type(residual))
    buy = input("Какие остатки хотите забрать (порядковые номера, через пробел): ")
    price = 100

    for ind in buy.split():
        print('Купили: ', residual_list(residual)[int(ind) - 1], 'штук, заплатив:')
        print(residual_list(residual)[int(ind) - 1] * price, 'руб')

    lst = residual.split()
    for ind in buy.split():
        x = residual.split()[int(ind) - 1]
        print(x, type(x))
        lst.remove(x)
        print(lst)

    residual = " ".join(lst)

# price_low = 100
# discount_low = 0
# residual = '3 2,5 5 8 5'

