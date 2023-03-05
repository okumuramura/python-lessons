price = 3.49
discount = 0.6

def invoice(n):
    print('ordinary price:', price)
    print('with discount:', price * discount)
    print('total:', round(price * discount * n, 5))

invoice(10)
