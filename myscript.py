from bankaccount import BankAccount

konto = BankAccount(500)

amountToWithdraw = 600

result = konto.try_withdraw(amountToWithdraw)

if (result.isSuccess):
    print(result.message, result.value)
elif (result.isSuccess is False):
    print(result.message, konto.balance)
