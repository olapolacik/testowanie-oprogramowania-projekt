import pytest
from unittest.mock import Mock

# Aleksandra Połacik
# Aplikacja do zarządzania budżetem domowym

# Klasa reprezentująca pojedynczą transakcję
class Transaction:
      def __init__(self, amount, description, date):
        if amount is None:
            raise ValueError("Brak kwoty w transakcji")
        if description is None:
            raise ValueError("Brak opisu w transakcji")
        if date is None:
            raise ValueError("Brak daty w transakcji")
        self.amount = amount
        self.description = description
        self.date = date

# Klasa reprezentująca budżet domowy
class Budget:
    def __init__(self, store):
        self.store = store
        self.transactions = []

    # Metoda do generowania raportu
    def generate_report(self):
        report = ''
        for t in self.transactions:
            report += f'{t.date}: {t.description} ({t.amount})\n'
        return report

    def add_transaction(self, transaction):
        if transaction.amount > 0:
            self.transactions.append(transaction)
            self.store.save_transaction(transaction)

    # Metoda do obliczania salda budżetu
    def get_balance(self):
        balance = 0
        for t in self.transactions:
            if t.amount is not None:
                balance += t.amount
        return balance

