def show_balance(balance):
    print(f"Your Balance is {balance}")

def deposit(balance):
    amount = float(input("Enter your deposit: "))
    if amount >= 0:
        balance += amount
    else:
        print("Your deposit is invalid")
    return balance

def withdraw(balance):
    amount = float(input("Enter your withdraw: "))
    if amount > balance:
        print("Insufficient funds ")
    elif amount < 0:
        print("Invalid amount ")
    else:
        balance -= amount
    return balance


balance = 0
is_running = True

while is_running:

    print("\nWelcome to Bank Account")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        show_balance(balance)

    elif choice == "2":
        balance = deposit(balance)

    elif choice == "3":
        balance = withdraw(balance)

    elif choice == "4":
        is_running = False

    else:
        print("Enter a valid choice")