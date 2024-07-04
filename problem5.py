import os

def get_balance(account_number: str) -> float:
    if not os.path.exists('accounts.txt'):
        raise FileNotFoundError("The accounts.txt file does not exist.")
    with open('accounts.txt', 'r') as file:
        for line in file:
            acc_num, balance = line.strip().split(',')
            if acc_num == account_number:
                return float(balance)
    raise ValueError(f"Account {account_number} not found")

def update_account(account_number: str, balance: float):
    accounts = []
    found = False
    if not os.path.exists('accounts.txt'):
        with open('accounts.txt', 'w') as file:
            pass  
    with open('accounts.txt', 'r') as file:
        for line in file:
            acc_num, bal = line.strip().split(',')
            if acc_num == account_number:
                accounts.append(f"{acc_num},{balance}\n")
                found = True
            else:
                accounts.append(line)
    if not found:
        accounts.append(f"{account_number},{balance}\n")
    with open('accounts.txt', 'w') as file:
        file.writelines(accounts)

def deposit(account_number: str, amount: float):
    if amount < 0:
        raise ValueError("Deposit amount must be positive")
    try:
        balance = get_balance(account_number)
    except ValueError:
        balance = 0.0
    balance += amount
    update_account(account_number, balance)

def withdraw(account_number: str, amount: float):
    if amount < 0:
        raise ValueError("Withdrawal amount must be positive")
    balance = get_balance(account_number)
    if balance < amount:
        raise ValueError("Insufficient funds")
    balance -= amount
    update_account(account_number, balance)


try:
    print("Initial balance for account 12345:", get_balance("12345"))
    deposit("12345", 200.0)
    print("Balance after deposit for account 12345:", get_balance("12345"))
    withdraw("12345", 100.0)
    print("Balance after withdrawal for account 12345:", get_balance("12345"))
except ValueError as e:
    print(e)
except FileNotFoundError as e:
    print(e)
