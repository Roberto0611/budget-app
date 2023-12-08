#Script by: Roberto Ochoa Cuevas

#category budget
class Category:
  name = "Default"
  total = 0

  #Init
  def __init__(self, name):
    self.name = name
    self.ledger = []

  #Method deposit
  def deposit(self, amount, description=""):
    self.total = amount + self.total
    self.ledger.append({"amount": amount, "description": description})

  #Method withdraw
  def withdraw(self, amount, description=""):
    if self.check_funds(amount) is False:
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
    description = 'Transfer to ' + destination.name
    if self.withdraw(amount, description) is True:
      description2 = "Transfer from " + self.name
      destination.deposit(amount, description2)
      return True
    else:
      return False

  #Method check_funds
  def check_funds(self, amount):
    return amount <= self.total

  # Method to format ledger entries
  def format_ledger_entry(self, entry):
    return f"{entry['description'][:23]:<23} {entry['amount']:.2f}"

  # Method __str__
  def __str__(self):
    # Create the title line
    title_line = f"{'*' * ((30 - len(self.name)) // 2)}{self.name}{'*' * ((30 - len(self.name)) // 2)}"

    # Create the ledger entries
    ledger_entries = "\n".join(
        self.format_ledger_entry(entry) for entry in self.ledger)

    # Create the total line
    total_line = f"\nTotal: {self.total:.2f}"

    # Combine all parts into the final string
    result = f"{title_line}\n{ledger_entries}{total_line}"

    return result
