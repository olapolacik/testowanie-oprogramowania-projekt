from projekt import*
import pytest

# Fixture do tworzenia budżetu z mockowanym sklepem
@pytest.fixture
def budget():
    store = Mock()
    b = Budget(store)
    t1 = Transaction(100, 'Wypłata', '2022-01-01')
    t2 = Transaction(-50, 'Zakupy', '2022-01-02')
    t3 = Transaction(-20, 'Tankowanie', '2022-01-03')
    b.add_transaction(t1)
    b.add_transaction(t2)
    b.add_transaction(t3)
    return b

# Testy E2E/akceptacyjne z użyciem fixture'a

def test_end_to_end(budget):
    # Sprawdzamy, czy saldo jest poprawne
    assert budget.get_balance() == 30

    # Generujemy raport
    report = budget.generate_report()

    # Sprawdzamy, czy raport zawiera odpowiednie informacje o transakcjach
    assert '2022-01-01: Wypłata (100)' in report
    assert '2022-01-02: Zakupy (-50)' in report
    assert '2022-01-03: Tankowanie (-20)' in report
