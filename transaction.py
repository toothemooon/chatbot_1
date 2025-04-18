class Transaction:
    def __init__(self, number, funds, status="active"):
        self.number = number
        self.funds = funds
        self.status = status
    
    def __repr__(self):
        return f"Transaction({self.number}, {self.funds}, {self.status})"
    
    def __str__(self):
        return f"Transaction({self.number}, {self.funds}, {self.status})"


payment = Transaction(1, 3, "Hey")
print(repr(payment))
print(str(payment))
print(payment)
