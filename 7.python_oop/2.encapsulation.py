from datetime import datetime
import time

class SecureVault:
    # Hint: note the number of leading undescores in each variable
    def __init__(self, owner: str, initial_funds: float):
        self.publickey = "vjti@123"     # Public variable
        self._owner = owner             # Protected variable
        self._funds = initial_funds     # Private variable
        self.access_log = []            # Protected variable

    @property
    def funds(self):
        self._access_log.append((datetime.now(), "READ"))
        return self.__funds

    @funds.setter
    def funds(self, amount: float):
        if amount < 0:
            raise ValueError("Funds cannot drop below zero.")
        self._access_log.append((datetime.now(), f"WRITE: {amount}"))
        self.__funds = amount

    @funds.deleter
    def funds(self):
        raise AttributeError("Direct deletion of funds is restricted.")

    # Write a function to access logs, say access_log

# Initialize the vault funds with 5000 dollars
vault = SecureVault("Alice", 5000.0)
print(vault.funds)       # Triggers getter & logs read
time.sleep(0.5)

# Set the vault funds to 750
vault.funds = 7500.0     # Triggers setter & logs write
print(vault.funds)
time.sleep(0.5)

# Task: Set funds to 0
try:
    del vault.funds
except:
    raise AttributeError("Deleting Vault Funds is not allowed...")
print(vault.funds)
time.sleep(0.5)

print("Public key:", vault.publickey)
time.sleep(0.5)

print("Vault viewed/modified", vault.access_log_len(), "times...")
