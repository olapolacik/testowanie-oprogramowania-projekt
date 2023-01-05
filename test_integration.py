from projekt import*
import pytest

#Testy integracyjne 
def test_budget_with_multiple_transactions():
    store = Mock()
    b = Budget(store)
    t1 = Transaction(100, 'Wypłata', '2022-01-01')
    t2 = Transaction(-50, 'Zakupy', '2022-01-02')
    t3 = Transaction(-20, 'Tankowanie', '2022-01-03')
    t4 = Transaction(-200, 'Tankowanie', '2022-01-03') # przypadek brzegowy - saldo ujemne
    t5 = Transaction(-20000, 'Tankowanie', '2022-01-03') # przypadek brzegowy - duża kwota wydatku
    t6 = Transaction(10000, 'Wypłata', '2022-01-03') # przypadek brzegowy - duża kwota dochodu
    b.add_transaction(t1)
    b.add_transaction(t2)
    b.add_transaction(t3)
    b.add_transaction(t4)
    b.add_transaction(t5)
    b.add_transaction(t6)
    assert b.get_balance() == -10170
    store.save_transaction.assert_any_call(t2)
    store.save_transaction.assert_any_call

