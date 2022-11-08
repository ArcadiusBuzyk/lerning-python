class Result:
    def __init__(self, isSuccess, message, value):
        self.isSuccess = isSuccess
        self.message = message
        self.value = value


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def try_withdraw(self, amount):
        if (self.balance >= amount):
            self.balance -= amount
            return Result(True, "Wypłacono kasę:", amount)

        return Result(False, "Nie wypłacono kasy,"
                      "Obecny stan konta:", self.balance)

    def __str__(self):
        return str(self.balance)
