class Balance:
    ...


balance = Balance()

balance.add_left(10)
balance.add_right(5)

print(balance.balance())  # -1

balance.add_right(5)
print(balance.balance())  # 0

balance.clear()
balance.add_right(5)
print(balance.balance())  # 1
