from projekt import*
import pytest

# Testy jednostkowe
def test_transaction():
    # Testujemy tworzenie transakcji z kwotą ujemną
    t = Transaction(-100, 'Wypłata', '2022-01-01')
    assert t.amount == -100
    assert t.description == 'Wypłata'
    assert t.date == '2022-01-01'

    # Testujemy tworzenie transakcji z pustym opisem
    t = Transaction(100, '', '2022-01-01')
    assert t.amount == 100
    assert t.description == ''
    assert t.date == '2022-01-01'

    # Testujemy tworzenie transakcji z brakiem daty
    t = Transaction(100, 'Wypłata', '')
    assert t.amount == 100
    assert t.description == 'Wypłata'
    assert t.date == ''

def test_transaction_with_missing_amount():
    with pytest.raises(ValueError):
        t = Transaction(None, 'Wypłata', '2022-01-03')

def test_transaction_with_missing_description():
    with pytest.raises(ValueError):
        t = Transaction(100, None, '2022-01-03')

def test_transaction_with_missing_date():
    with pytest.raises(ValueError):
        t = Transaction(100, 'Wypłata', None)


def test_budget():
    b = Budget(Mock())

    # Testujemy dodawanie transakcji z kwotą ujemną
    t1 = Transaction(-100, 'Wypłata', '2022-01-01')
    t2 = Transaction(50, 'Zakupy', '2022-01-02')
    b.add_transaction(t1)
    b.add_transaction(t2)
    assert b.get_balance() == -50

    # Testujemy dodawanie transakcji z pustym opisem
    t1 = Transaction(100, '', '2022-01-01')
    t2 = Transaction(50, 'Zakupy', '2022-01-02')
    b = Budget(Mock())
    b.add_transaction(t1)
    b.add_transaction(t2)
    assert b.get_balance() == 150

def test_budget_with_empty_date():
    #Testujemy dodawanie transakcji bez daty
    t1 = Transaction(100, 'Wypłata', '')
    t2 = Transaction(50, 'Zakupy', '2022-01-02')
    b = Budget(Mock())
    b.add_transaction(t1)
    b.add_transaction(t2)
    assert b.get_balance() == 150

def test_budget_with_future_date():
    #Testujemy dodawanie transakcji z datą w przyszłości
    t1 = Transaction(100, 'Wypłata', '2022-01-01')
    t2 = Transaction(50, 'Zakupy', '2023-01-01')
    b = Budget(Mock())
    b.add_transaction(t1)
    b.add_transaction(t2)
    assert b.get_balance() == 150

def test_budget_with_past_date():
    #Testujemy dodawanie transakcji z datą w przeszłości
    t1 = Transaction(100, 'Wypłata', '2020-01-01')
    t2 = Transaction(50, 'Zakupy', '2019-01-01')
    b = Budget(Mock())
    b.add_transaction(t1)
    b.add_transaction(t2)
    assert b.get_balance() == 150



