from datetime import datetime
import time

class SecureVault:
    def __init__(self, owner: str, initial_funds: float):
        self.publickey = "vjti@123"
        self._owner = owner
        self.__funds = initial_funds
        self._access_log = []

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

    # Write a function to return length of access logs, say access_log_len
    def access_log_len(self) -> int:
        return len(self._access_log)

# Initialize the vault funds with 5000 dollars
vault = SecureVault("Alice", 5000.0)
print(vault.funds)       # Triggers getter & logs read
time.sleep(0.5)

# Set the vault funds to 750
vault.funds = 7500.0     # Triggers setter & logs write
print(vault.funds)
time.sleep(0.5)

# Task: Set funds to 0
vault.funds = 0
print(vault.funds)
time.sleep(0.5)

print("Public key:", vault.publickey)
time.sleep(0.5)

print("Vault viewed/modified", vault.access_log_len(), "times...")

# Can you tell us why vault was modified 5 times?
