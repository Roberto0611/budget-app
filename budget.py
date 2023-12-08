#Script by: Roberto Ochoa Cuevas

#category budget
class Category:
  name = "Default"
  total = 0
  ledger = []
  
  #Init
  def __init__(self, name):
    self.name = name

  #Method deposit
  def deposit(self, amount, description=""):
    self.total = amount + self.total
    self.ledger.append({"amount": amount, "description": description})

  #Method withdraw
  def withdraw(self, amount , description=""):
    if self.check_funds(amount) is False :
      return False
    else:
      self.total = self.total - amount
      self.ledger.append({"amount": -amount, "description": description})
      return True

  #Method get_balance
  def get_balance(self):
    return self.total

  #Method tranfer
  def transfer(self, amount, destination):
    description = 'Transfer to' + destination.name
    if self.withdraw(amount, description) is True:
      description2 = "Transfer from" + destination.name
      destination.deposit(amount, description2)
    else:
      return False
  
  #Method check_funds
  def check_funds(self, amount):
    if amount > self.total:
      return False
    elif amount < self.total:
      return True

  


#def create_spend_chart(categories):
