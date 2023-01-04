from projekt import*
import pytest

# Testy jednostkowe
def test_transaction():
    t = Transaction(100, 'Wypłata', '2022-01-01')
    assert t.amount == 100
    assert t.description == 'Wypłata'
    assert t.date == '2022-01-01'

def test_budget():
    b = Budget(Mock())
    t1 = Transaction(100, 'Wypłata', '2022-01-01')
    t2 = Transaction(-50, 'Zakupy', '2022-01-02')
    b.add_transaction(t1)
    b.add_transaction(t2)
    assert b.get_balance() == 50
