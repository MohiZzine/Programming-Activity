# Program Name: Transaction
# Author(s): Mohieddine Farid
# Date of Creation: Nov 4, 2022

import calendar
from datetime import datetime


class Money:
  """The class represents a Money object
  attributes:
    amount (float): represents the money value of the object
  methods:
    getAmount: returns the amount attribute of an instance
    setAmount: changes the amount attribute of an instance to a desired value
    __str__: special method to display the money object
  """
  def __init__(self, amount: float=0.0, currency:str = "USD"):
    self._amount = amount
    self._currency = currency
  
  def getAmount(self):
    return self._amount
  
  def setAmount(self, amount):
    self._amount = amount

  def __str__(self):
    return f"This is {self._amount} DH "

# Class Name: Account
# Author(s): Mohieddine Farid
# Date of Creation: Nov 4, 2022
class Account:
  """The class represents a Bank Account
  Attributes:
    number (str): denotes the account number of the Account
    balance (Money): denotes the balance of the Account 
    minimum (Money): denotes the minimum balance required in the Account
  Methods:
    getNumber: returns the number attribute of the Account instance 
    getBalance: returns the balance attribute of the Account instance
    getMinimum: returns the mininum attribute of the Account instance
    setNumber: sets the number attribute of the Account instance to a desired value
    setBalance: sets the balance attribute of the Account instance to a desired value
    setMinimum: sets the balance attribute of the Account instance to a desired value
    withdraw: withdraws a desired amount from an Account instance
    deposit: deposits a desired amount from an Account instance
    displayBalance: display the net available balance of an Account instance
  """
  def __init__(self, number:str = "", balance:Money = Money(0.0), minimum:Money = Money(0.0)):
    if not isinstance(number, str):
      raise TypeError('Account Number must be of type str')
    else:
      self._number = number
    if not isinstance(balance, Money):
      raise TypeError('Balance must be of type Money')
    else:
      self._balance = balance
    if not isinstance(minimum, Money):
      raise TypeError('Minimum balance must be of type Money')
    elif (balance._amount < minimum._amount):  # balance less than the minimum
      raise Exception('The balance number must be greater than the minimum balance required')
    else:
      self._minimum = minimum

  def getNumber(self) -> str:
    return self._number 
  def getBalance(self) -> Money:
    return self._balance
  def getMinimum(self) -> Money:
    return self._minimum

  def setNumber(self, number: str):
    if not isinstance(number, str):
      raise TypeError('Account Number must be of type str')
    else:
      self._number = number
  def setBalance(self, balance: Money):
    if not isinstance(balance, Money):
      raise TypeError('Balance must be of type int')
    else:
      self._balance = balance
  def setMinimum(self, minimum: Money):
    if not isinstance(minimum, Money):
      raise TypeError('Minimum balance must be of type Money')
    else:
      self._minimum = minimum
  
  def withdraw(self, money):
    if not isinstance(money, Money): # check if of type Money
      raise TypeError('Money to withdraw must be of type Money')
    else:
      if (self._balance._amount - money._amount >= self._minimum._amount):  # if the eventual balance will be over the minimum
        self._balance._amount -= money._amount
        print(f"The withdrawal of {money._amount} from account {self._number} DH was successful")
        return True
      else: # The balance after operation is less than minimum
        print("Your balance is not sufficient for the withdrawal")
        return False

  def deposit(self, money):
    if not isinstance(money, Money):
      raise TypeError('The deposit money must be of type Money')
    else:
      self._balance._amount += money._amount
      print(f"You successfully deposit {money._amount} in account {self._number} ")  # Deposit the amount to the balance
    return True

  def displayBalance(self):
    print(f"The Net Available Balance of account number {self._number} is : {self._balance} ")
  
# Program/Class Name: Customer
# Author(s): Mohieddine Farid
# Date of Creation: Nov 4, 2022

class Customer:
  """The class represents a Customer Object
    Attributes:
      name (str): represents the name of the Customer
      address (str): represents the address of the Customer
      id (str): represents the id of the Customer
      accounts (list): represents a list of accounts the Customer has
    Methods:
      getName: returns the name of the Customer
      getAddress: returns the address of the Customer
      getId: returns the attribute of the Customer
      getAccount: returns a list of the account numbers of the Customer's accounts
      setName: sets the name attribute of the Customer to a desired name
      setAddress: sets the address attribute of the Customer to a desired address
      setId: sets the id attribute of the Customer to a desired id
      setAccounts: sets the accounts attribute of the Customer to a list of desired accounts
  """
  def __init__(self, name: str = "", address: str = "", ID: str = "", accounts: list = []):
    self._name = name
    self._address = address
    self._id = ID
    self._accounts = accounts
  def getName(self):
    return self._name
  def getAddress(self):
    return self._address
  def getId(self):
    return self._id
  def getAccounts(self):
    return [account._number for account in self._accounts]
  
  def setName(self, name):
    if not isinstance(name, str):
      raise TypeError('name must be of type int')
    else:
      self._name = name
  def setAddress(self, address):
    if not isinstance(address, str):
      raise TypeError('address must be of type str')
    self._address = address
  def setId(self, id):
    if not isinstance(id, str):
      raise TypeError('id must be of type str')
    else:
      self._id = id
  def setAccounts(self, accounts):
    if not isinstance(accounts, list):
      raise TypeError('accounts must be of type list')
    else:
      self.accounts = accounts
  
  def __str__(self):
    return f"""Customer : {self._name} 
    Address: {self._address}
    Id: {self._id}
    Accounts: {self.getAccounts()} """


# Program/Class Name: CheckingAccount
# Author(s): Mohieddine Farid
# Date of Creation: Nov 4, 2022

class CheckingAccount(Account):
  """The class represents a Checking Account
  Parent: Account
  Attributes:
    number (str): denotes the account number of the Checking Account
    balance (Money): denotes the balance of the Checking Account 
    minimum (Money): denotes the minimum balance required in the Checking Account
  Methods:
    getNumber: returns the number attribute of the Checking Account instance 
    getBalance: returns the balance attribute of the Checking Account instance
    getMinimum: returns the mininum attribute of the Checking Account instance
    setNumber: sets the number attribute of the Checking Account instance to a desired value
    setBalance: sets the balance attribute of the Checking Account instance to a desired value
    setMinimum: sets the balance attribute of the Checking Account instance to a desired value
    withdraw: withdraws a desired amount from an Checking Account instance
    deposit: deposits a desired amount from an Checking Account instance
    displayBalance: display the net available balance of an Checking Account instance
  """
  def __init__(self, number: str = "", balance: Money = Money(0.0), minimum: Money = Money(0.0)):
    super().__init__(number, balance, minimum)
  

# Program/Class Name: SavingsAccount
# Author(s): Mohieddine Farid
# Date of Creation: Nov 4, 2022
class SavingsAccount(Account):
  """The class represents a Savings Account
  Parent: Account
  Variables:
    year (int): represents the amount of years the Savings Account was oppened
  Attributes:
    number (str): denotes the account number of the Savings Account
    balance (Money): denotes the balance of the Savings Account 
    minimum (Money): denotes the minimum balance required in the Savings Account
    interestRate (float): denotes the interest rate of the Savings Account
  Methods:
    getNumber: returns the number attribute of the Savings Account instance 
    getBalance: returns the balance attribute of the Savings Account instance
    getMinimum: returns the mininum attribute of the Savings Account instance
    setNumber: sets the number attribute of the Savings Account instance to a desired value
    setBalance: sets the balance attribute of the Savings Account instance to a desired value
    setMinimum: sets the balance attribute of the Savings Account instance to a desired value
    withdraw: withdraws a desired amount from an Savings Account instance
    deposit: deposits a desired amount from an Savings Account instance
    displayBalance: display the net available balance of an Savings Account instance
    updateBalance: updates the balance attribute with interestRate after a year
  """
  year = 0
  def __init__(self, number: str = "", balance: Money = Money(0.0), minimum: Money = Money(0.0), interestRate = 0.02):
    super().__init__(number, balance, minimum)
    self._interestRate = interestRate

  def getInterestRate(self):
    return self._interestRate

  def setInterestRate(self, interest):
    self._interestRate = interest

  def updateBalance(self):
    SavingsAccount.year += 1
    self._balance *= (1 + self._interestRate)

# Class Name: Transaction
# Author(s): Mohieddine Farid
# Date of Creation: Nov 4, 2022

class Transaction:
  """The class represents the Transaction class
    Variables:
      commit (bool): represents the actual commit (can be changed by the "commit" method)
    Attributes:
      amount: denotes the amount of the Transaction
      sender: denotes the sender Account of the Transaction
      recipient: denotes the recipient Account of the Transaction
      dateTime: denotes the time of the Transaction
      status: denotes the status of the Transaction
    Methods:
      getAmount: returns the amount attribute of the Transaction instance
      getSender: returns the sender account number attribute of the Transaction instance
      getRecipient: returns the recipient account number attribute of the Transaction instance
      getDateTime: returns the dateTime attribute of the Transaction instance
      getStatus: returns the status attribute of the Transaction instance
      setAmount: sets the amount attribute of the Transaction instance to a desired value
      setSender: sets the sender attribute of the Transaction instance to a desired value
      setRecipient: sets the recipient attribute of the Transaction instance to a desired value
      setDateTime: sets the dateTime attribute of the Transaction instance to a desired value
      setStatus: sets the status attribute of the Transaction instance to a desired value
      begin: begins the Transaction between "sender" and "recipient"
      rollback: reverses the Transaction between "sender" and "recipient"
      commit: inverses the static variable "commit"
  """
  commit = False
  def __init__(self, amount: Money = Money(0.0), sender:Account = Account("", Money(0.0), Money(0.0)), recipient:Account = Account("", Money(0.0), Money(0.0)), dateTime: calendar.Calendar = calendar.Calendar(), status: str ="" ):
    if not isinstance(amount, Money):
      raise TypeError('Amount must be of type Money')
    else:
      self._amount = amount
    if not isinstance(sender, Account):
      raise TypeError('Sender must be of type Account')
    else:
      self._sender = sender
    if not isinstance(recipient, Account):
      raise TypeError('Recipient must be of type Account')
    else:
      self._recipient = recipient
    if not isinstance(dateTime, calendar.Calendar):
      raise TypeError('DateTime must be of type Calendar')
    else:
      self._dateTime = dateTime
    if not isinstance(status, str):
      raise TypeError('Status must be of type Str')
    else:
      self._status = status
  
  def getAmount(self) -> Money:
    return self._amount
  def getSender(self) -> str:
    return self._sender._number
  def getRecipient(self) -> str:
    return self._recipient._number
  def getDateTime(self) -> calendar.Calendar:
    return self._dateTime
  def getStatus(self) -> str:
    return self._status

  def setAmount(self, amount: Money):
    if not isinstance(amount, Money):
      raise TypeError('Amount must be of type Money')
    else:
      self._amount = amount
  def setSender(self, sender: Account):
    if not isinstance(sender, Account):
      raise TypeError('Sender must be of type Account')
    else:
      self._sender = sender
  def setRecipient(self, recipient):
    if not isinstance(recipient, Account):
      raise TypeError('Recipient must be of type Account')
    else:
      self._recipient = recipient
  def setDateTime(self, datetime):
    if not isinstance(datetime, calendar.Calendar):
      raise TypeError('DateTime must be of type Calendar')
    else:
      self._dateTime = datetime
  def setStatus(self, status):
    if not isinstance(status, str):
      raise TypeError('Status must be of type str')
    else:
      self._status = status
  

  def begin(self):
    if Transaction.commit:
      self._sender.withdraw(self._amount)
      self._recipient.deposit(self._amount)
    else:
      print("Transaction was blocked !")

  def rollback(self):
    if Transaction.commit:
      self._recipient.withdraw(self._amount)
      self._sender.deposit(self._amount)
    else:
      print("The Transaction was blocked !")

  def commit(self):
   commit = not commit


# Program/Class Name: Transfer
# Author(s): Mohieddine Farid
# Date of Creation: Nov 4, 2022

class Transfer(Transaction):
  """The class represents a Transfer
  Parent: Transaction
  Attributes:
    Inherits all attributes from the Transaction class
  Methods:
    Inherits all methods from the Transaction class
    """
  def __init__(self, amount:  Money = Money(0.0), sender: Account = Account("", Money(0.0), Money(0.0)), recipient:Account = Account("", Money(0.0), Money(0.0)), dateTime= calendar.Calendar(), status: str = ""):
    super().__init__(amount, sender, recipient, dateTime, status)


  
# Program/Class Name: Withdraw
# Author(s): Mohieddine Farid
# Date of Creation: Nov 4, 2022

class Widthdraw(Transaction):
  """The class represents a Withdraw
  Parent: Transaction
  Attributes: 
    Inherits all attributes from the Transaction class
  Methods: 
    Inherits all methods from the Transaction class
  """
  def __init__(self, amount: Money = (0.0), sender: Account = Account("", Money(0.0), Money(0.0)), recipient: Account = Account("", Money(0.0), Money(0.0)), dateTime: calendar.Calendar= calendar.Calendar(), status: str = ""):
    super().__init__(amount, sender, recipient, dateTime, status)

  
# Program/Class Name: Deposit
# Author(s): Mohieddine Farid
# Date of Creation: Nov 4, 2022

class Deposit(Transaction):
  """The class represents a Deposit
  Parent: Transaction
  Attributes:
    Inherits all attributes from the Transaction class
  Methods:
    Inherits all methods from the Transaction class
  """
  def __init__(self, amount: Money = Money(0.0), sender:Account = Account("", Money(0.0), Money(0.0)), recipient:Account = Account("", Money(0.0), Money(0.0)), dateTime= calendar.Calendar(), status: str = ""):
    super().__init__(amount, sender, recipient, dateTime, status)