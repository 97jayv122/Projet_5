## Écrivez votre code ici !
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Le montant {amount} a été déposé avec succès !")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Le montant {amount} a été retiré avec succès !")
        else:
            print("Solde insuffisant !")

    def display_balance(self):
        print(f"Solde actuel: {self.balance}")
