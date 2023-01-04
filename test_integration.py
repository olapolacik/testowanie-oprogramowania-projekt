from projekt import*
import pytest

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