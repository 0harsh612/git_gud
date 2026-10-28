from functools import singledispatch
import time

class Currency:
    def __init__(self, amount: float, symbol: str):
        self.amount = amount
        self.symbol = symbol

@singledispatch
def format_value(value):
    raise TypeError(f"Unsupported type: {type(value)}")

@format_value.register
def _(value: int | float):
    return f"${value:,.2f}"

@format_value.register
def _(value: Currency):
    return f"{value.symbol}{value.amount:,.2f}"

# Hint: Check type of each input given
try:
    print(format_value("1500"))
except:
    raise TypeError("Unsupported type")
time.sleep(0.5)

try:
    print(format_value(Currency({120}, "€")))
except:
    raise TypeError("Unsupported type")