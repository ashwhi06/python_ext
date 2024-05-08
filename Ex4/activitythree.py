class Currency:
    currencies = {'CHF': 0.930023,  # Swiss Franc
                  'CAD': 1.264553,  # Canadian Dollar
                  'GBP': 0.737414,  # British Pound
                  'JPY': 111.019919,  # Japanese Yen
                  'EUR': 0.862361,  # Euro
                  'USD': 1.0}  # US Dollar

    def __init__(self, value, unit="USD"):
        self.value = value
        self.unit = unit

    def changeTo(self, new_unit):
        """Transforms Currency object from self.unit to new_unit."""
        self.value = (self.value / self.currencies[self.unit] * self.currencies[new_unit])
        self.unit = new_unit

    def __repr__(self):
        return f"{round(self.value, 2)} {self.unit}"

    def __str__(self):
        return self.__repr__()

    def __add__(self, other):
        if isinstance(other, Currency):
            # Convert other currency to self currency and add
            other_value_in_self_unit = (other.value / self.currencies[other.unit] * self.currencies[self.unit])
            return Currency(self.value + other_value_in_self_unit, self.unit)
        elif isinstance(other, (int, float)):  # Treat other as USD
            other_in_self_unit = other * self.currencies[self.unit]
            return Currency(self.value + other_in_self_unit, self.unit)
        return NotImplemented

    def __radd__(self, other):
        # This enables int + Currency
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, (int, float)):  # Treat other as USD
            other_in_self_unit = other * self.currencies[self.unit]
            return Currency(self.value - other_in_self_unit, self.unit)
        return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, (int, float)):  # Treat other as USD
            other_in_self_unit = other * self.currencies[self.unit]
            return Currency(other_in_self_unit - self.value, self.unit)
        return NotImplemented

# Example usage
v1 = Currency(23.43, "EUR")
v2 = Currency(19.97, "USD")
print(v1 + v2)  
print(v2 + v1)  
print(v1 + 3)  
print(3 + v1)  
print(v1 - 3)  
print(30 - v2)  