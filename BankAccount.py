class BankAccount:
    
    def __init__(self, owner, balance):
        
        self.owner = owner
        self.balance = balance
        
    def __str__(self):
        
        return f"{self.owner}'s account's balance is {self.balance} PLN"
        
    def deposit(self,number):
        
        self.balance = self.balance + number
        return f"Deposit accepted. The account's balance is {self.balance} PLN"
        
    def withdraw(self, number):
        
        if self.balance >= number:
        
            self.balance = self.balance - number
            return f" Withdrawal accepted. The account's balance is {self.balance} PLN"
    
        else:
            
            return "Withdrawal not accepted. Not enough funds."