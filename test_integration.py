from projekt import*
import pytest
"""
# Testy integracyjne
def test_budget_with_multiple_transactions():
    store = Mock()
    b = Budget(store)
    t1 = Transaction(100, 'Wypłata', '2022-01-01')
    t2 = Transaction(-50, 'Zakupy', '2022-01-02')
    t3 = Transaction(-20, 'Tankowanie', '2022-01-03')
    b.add_transaction(t1)
    b.add_transaction(t2)
    b.add_transaction(t3)
    assert b.get_balance() == 30
    store.save_transaction.assert_any_call(t1)
    store.save_transaction.assert_any_call(t2)
    store.save_transaction.assert_any_call(t3)
"""

def test_budget_with_multiple_transactions():
    store = Mock()
    b = Budget(store)
    t1 = Transaction(100, 'Wypłata', '2022-01-01')
    t2 = Transaction(-50, 'Zakupy', '2022-01-02')
    t3 = Transaction(-20, 'Tankowanie', '2022-01-03')
    t4 = Transaction(-200, 'Tankowanie', '2022-01-03') # przypadek brzegowy - saldo ujemne
    t5 = Transaction(-20000, 'Tankowanie', '2022-01-03') # przypadek brzegowy - duża kwota wydatku
    t6 = Transaction(10000, 'Wypłata', '2022-01-03') # przypadek brzegowy - duża kwota dochodu
    t7 = Transaction(None, 'Wypłata', '2022-01-03') # przypadek brzegowy - brak kwoty
    t8 = Transaction(100, None, '2022-01-03') # przypadek brzegowy - brak opisu
    t9 = Transaction(100, 'Wypłata', None) # przypadek brzegowy - brak daty
    b.add_transaction(t1)
    b.add_transaction(t2)
    b.add_transaction(t3)
    b.add_transaction(t4)
    b.add_transaction(t5)
    b.add_transaction(t6)
    b.add_transaction(t7)
    b.add_transaction(t8)
    b.add_transaction(t9)
    assert b.get_balance() == 30
    store.save_transaction.assert_any_call(t1)
    store.save_transaction.assert_any_call(t2)
    store.save_transaction.assert_any_call