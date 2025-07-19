import json
import os
from datetime import datetime
from budget_utils import group_by_category, calculate_totals

DATA_FILE = "expenses.json"


class Transaction:
    def __init__(self, date, category, amount):
        self.date = date
        self.category = category
        self.amount = amount

    def to_dict(self):
        return {"date": self.date, "category": self.category, "amount": self.amount}

    @staticmethod
    def from_dict(data):
        return Transaction(data["date"], data["category"], data["amount"])


def save_transactions(transactions):
    with open(DATA_FILE, "w") as f:
        json.dump([t.to_dict() for t in transactions], f)


def load_transactions():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            return [Transaction.from_dict(d) for d in data]
    return []


def add_transaction(transactions):
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Category: ")
    try:
        amount = float(input("Amount: "))
    except:
        print("Invalid amount.")
        return
    transactions.append(Transaction(date, category, amount))
    print("Transaction added.")


def view_transactions(transactions):
    if not transactions:
        print("No transactions yet.")
    for t in transactions:
        print(f"{t.date} | {t.category}: ₦{t.amount:.2f}")


def report(transactions):
    grouped = group_by_category(transactions)
    totals = calculate_totals(transactions)
    print("\n--- Report by Category ---")
    for cat, ts in grouped.items():
        print(f"{cat}: {len(ts)} transaction(s), Total: ₦{totals[cat]:.2f}")


def main():
    transactions = load_transactions()
    while True:
        print(
            "\n1. Add transaction\n2. View transactions\n3. Category report\n4. Save & Exit")
        op = input("Choose: ")
        if op == "1":
            add_transaction(transactions)
        elif op == "2":
            view_transactions(transactions)
        elif op == "3":
            report(transactions)
        elif op == "4":
            save_transactions(transactions)
            print("Saved. Bye!")
            break
        else:
            print("Invalid.")


if __name__ == "__main__":
    main()
