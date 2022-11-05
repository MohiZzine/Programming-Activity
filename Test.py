# Test file for testing some of A3 methods
from A3 import *

# First Money instance
amount1 = Money(5000.0)
print(amount1)
# Second Money instance
amount2 = Money(3500.0)
print(amount2)

# First account object
acc1 = Account("001", amount1, Money(0.0))
# Customer intance having the first account
custom1 = Customer("Iman", "Route Mehdia", "AE31", [acc1])
# display first Customer info
print(custom1)
# Second account object
acc2 = Account("002", amount2, Money(0.0))
# Customer instance having the second account
custom2 = Customer("Ilyas", "Route Casa", "IF67", [acc2])
# display second Customer info
print(custom2)

# Transaction instance (between the two accounts)
trans = Transaction(Money(2500.0), acc1, acc2, status = "medium transaction")
# transaction begins
trans.begin()

# display balance of both accounts after the transaction 
acc1.displayBalance()
acc2.displayBalance()

# reverse transaction
trans.rollback()

# same as before (we should notice the same balance as beginning)
acc1.displayBalance()
acc2.displayBalance()
