# ABC Bank Customer Management System

This project is a simple customer management system for ABC Bank. It allows for adding new customers, viewing customer details, depositing and withdrawing money, and updating customer details.

## Features

- Add a new customer with the following details:
  - Bank Account Number (10-digit number)
  - NIC (National Identity Card Number, 10 characters)
  - Account Holder’s First Name (maximum of 10 characters)
  - Account Holder’s Last Name (maximum of 15 characters)
  - Birth Date
  - Permanent Address (maximum of 15 characters)
  - Telephone Number (10 digits)
- View details of a specific customer
- View details of all customers
- Deposit money into a customer's account
- Withdraw money from a customer's account
- Update customer details

## Installation and Setup

### Running Locally

1. **Ensure Python is Installed**: Make sure Python 3.x is installed on your computer. You can download it from [python.org](https://www.python.org/downloads/).

2. **Set Up the Project Directory**: 
    - Create a directory for your project and place the provided Python files (`main.py` and `customer.py`) inside it.

3. **Run the Project**: 
    - Use a terminal or command prompt to navigate to your project directory and execute the `main.py` file:
    ```sh
    python main.py
    ```

## Usage

After running the program, you will see the main menu for the ABC Bank system in the console. You can follow the menu prompts to interact with the system.

### Main Menu Options

1. **Add a new customer**: Enter customer details as prompted, ensuring they meet the specified constraints.
2. **View details of a customer**: Enter the customer's account number to view their details.
3. **View details of all customers**: Displays a list of all customers with their account numbers, names, and balances.
4. **Deposit money**: Enter the customer's account number and the amount to deposit.
5. **Withdraw money**: Enter the customer's account number and the amount to withdraw.
6. **Update customer details**: Enter the customer's account number and update their details as prompted.
7. **Exit**: Exit the program.

