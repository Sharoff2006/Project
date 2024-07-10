class Customer:

    def __init__(self, account_number, nic, first_name, last_name, birth_date,
                 address, phone):
        self.account_number = account_number
        self.nic = nic
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.address = address
        self.phone = phone
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def update_details(self,
                       nic=None,
                       first_name=None,
                       last_name=None,
                       birth_date=None,
                       address=None,
                       phone=None):
        if nic: self.nic = nic
        if first_name: self.first_name = first_name
        if last_name: self.last_name = last_name
        if birth_date: self.birth_date = birth_date
        if address: self.address = address
        if phone: self.phone = phone
