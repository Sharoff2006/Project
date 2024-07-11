class Customer:
    def __init__(self, account_number, nic, first_name, last_name, birth_date, address, phone):
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

    def update_details(self, nic=None, first_name=None, last_name=None, birth_date=None, address=None, phone=None):
        if nic: self.nic = nic
        if first_name: self.first_name = first_name
        if last_name: self.last_name = last_name
        if birth_date: self.birth_date = birth_date
        if address: self.address = address
        if phone: self.phone = phone


customers = []

def validate_account_number(account_number):
    return account_number.isdigit() and len(account_number) == 10

def validate_nic(nic):
    return len(nic) == 10

def validate_name(name, max_length):
    return len(name) <= max_length

def validate_address(address):
    return len(address) <= 15

def validate_phone(phone):
    return phone.isdigit() and len(phone) == 10

def add_customer():
    if len(customers) >= 5:
        print("Cannot add more customers. Maximum limit reached.")
        return

    account_number = input("Enter Account Number (10 digits): ")
    if not validate_account_number(account_number):
        print("Invalid Account Number. Must be 10 digits.")
        return

    nic = input("Enter NIC (10 characters): ")
    if not validate_nic(nic):
        print("Invalid NIC. Must be 10 characters.")
        return

    first_name = input("Enter First Name (max 10 characters): ")
    if not validate_name(first_name, 10):
        print("Invalid First Name. Must be 10 characters or less.")
        return

    last_name = input("Enter Last Name (max 15 characters): ")
    if not validate_name(last_name, 15):
        print("Invalid Last Name. Must be 15 characters or less.")
        return

    birth_date = input("Enter Birth Date: ")

    address = input("Enter Address (max 15 characters): ")
    if not validate_address(address):
        print("Invalid Address. Must be 15 characters or less.")
        return

    phone = input("Enter Phone Number (10 digits): ")
    if not validate_phone(phone):
        print("Invalid Phone Number. Must be 10 digits.")
        return

    new_customer = Customer(account_number, nic, first_name, last_name, birth_date, address, phone)
    customers.append(new_customer)
    print("Customer added successfully.")

def view_customer(account_number):
    for cust in customers:
        if cust.account_number == account_number:
            print(f"Account Number: {cust.account_number}")
            print(f"NIC: {cust.nic}")
            print(f"First Name: {cust.first_name}")
            print(f"Last Name: {cust.last_name}")
            print(f"Birth Date: {cust.birth_date}")
            print(f"Address: {cust.address}")
            print(f"Phone: {cust.phone}")
            print(f"Balance: {cust.balance}")
            return
    print("Customer not found.")

def view_all_customers():
    for cust in customers:
        print(f"Account Number: {cust.account_number}, Name: {cust.first_name} {cust.last_name}, Balance: {cust.balance}")

def deposit_money(account_number, amount):
    for cust in customers:
        if cust.account_number == account_number:
            cust.deposit(amount)
            print("Deposit successful.")
            return
    print("Customer not found.")

def withdraw_money(account_number, amount):
    for cust in customers:
        if cust.account_number == account_number:
            if cust.withdraw(amount):
                print("Withdrawal successful.")
            else:
                print("Insufficient balance.")
            return
    print("Customer not found.")

def update_customer_details(account_number):
    for cust in customers:
        if cust.account_number == account_number:
            nic = input("Enter new NIC (10 characters): ")
            if validate_nic(nic):
                cust.update_details(nic=nic)

            first_name = input("Enter new First Name (max 10 characters): ")
            if validate_name(first_name, 10):
                cust.update_details(first_name=first_name)

            last_name = input("Enter new Last Name (max 15 characters): ")
            if validate_name(last_name, 15):
                cust.update_details(last_name=last_name)

            birth_date = input("Enter new Birth Date: ")
            cust.update_details(birth_date=birth_date)

            address = input("Enter new Address (max 15 characters): ")
            if validate_address(address):
                cust.update_details(address=address)

            phone = input("Enter new Phone Number (10 digits): ")
            if validate_phone(phone):
                cust.update_details(phone=phone)

            print("Customer details updated successfully.")
            return
    print("Customer not found.")

def main_menu():
    while True:
        print("\nABC Bank Main Menu")
        print("1. Add a new customer")
        print("2. View details of a customer")
        print("3. View details of all customers")
        print("4. Deposit money")
        print("5. Withdraw money")
        print("6. Update customer details")
        print("7. Exit")

        choice = input("Your choice: ")

        if choice == '1':
            add_customer()
        elif choice == '2':
            account_number = input("Enter Account Number: ")
            view_customer(account_number)
        elif choice == '3':
            view_all_customers()
        elif choice == '4':
            account_number = input("Enter Account Number: ")
            amount = float(input("Enter amount to deposit: "))
            deposit_money(account_number, amount)
        elif choice == '5':
            account_number = input("Enter Account Number: ")
            amount = float(input("Enter amount to withdraw: "))
            withdraw_money(account_number, amount)
        elif choice == '6':
            account_number = input("Enter Account Number: ")
            update_customer_details(account_number)
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
