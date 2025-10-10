"""
🏦 TASK 9 — Bank Accounts Update
Topic: dict state update from a list of transactions

Accounts: {"Alex": 1000, "Bob": 500, "Cara": 200}
Transactions: [("Alex",-200), ("Bob",+300), ("Alex",+100), ("Cara",-50), ("Dan",+40)]
Apply transactions (add deltas). If name not in accounts, create with starting balance 0 before applying.
Finally, print balances sorted by name.

"""
# Starter:
accounts = {"Alex": 1000, "Bob": 500, "Cara": 200}
tx = [("Alex",-200), ("Bob",+300), ("Alex",+100), ("Cara",-50), ("Dan",+40)]
# TODO: apply tx to accounts; then print sorted balances
for account in tx:
    accounts[account[0]] = accounts.get(account[0], 0) + account[1]
print(dict(sorted(accounts.items())))