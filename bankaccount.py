class Result:
    def __init__(self, message, value=None):
        self.isSuccess = None
        self.message = message
        self.value = value


class Ok(Result):
    def __init__(self, message, value=None):
        super().__init__(message, value)
        self.isSuccess = True


class Error(Result):
    def __init__(self, message, value=None):
        super().__init__(message, value)
        self.isSuccess = False


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def try_withdraw(self, amount):
        if (self.balance >= amount):
            self.balance -= amount
            return Ok("Wypłacono kasę:", amount)

        return Error("Nie wypłacono kasy,"
                     "Obecny stan konta:", self.balance)

    def __str__(self):
        return str(self.balance)


class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance=0, minimumBalance=1000):
        super().__init__(balance)
        self.minimumBalance = minimumBalance

    def try_withdraw(self, amount):
        if (self.balance - amount > self.minimumBalance):
            return super().try_withdraw(amount)
        else:
            withdrawToMin = self.balance - self.minimumBalance
            self.balance -= withdrawToMin
            return Error("Przekroczono minimalny balans konta, "
                         "wypłacamy pieniądze do minimalnej wartości. "
                         "Stan konta:", self.balance)
