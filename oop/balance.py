class Balance:
    left = 0
    right = 0

    def add_left(self, v):
        self.left += v

    def add_right(self, v):
        self.right += v

    def clear(self):
        self.left = 0
        self.right = 0

    def balance(self):
        if self.left > self.right:
            return -1
        elif self.right > self.left:
            return 1
        return 0

balance = Balance()

balance.add_left(10)
balance.add_right(5)

print(balance.balance())  # -1

balance.add_right(5)
print(balance.balance())  # 0

balance.clear()
balance.add_right(5)
print(balance.balance())  # 1
