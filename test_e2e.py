from projekt import*
import pytest
import csv


def test_e2e(budget):
    # Sprawdzamy, czy saldo jest poprawne
    assert budget.get_balance() == 30

    # Generujemy raport
    report = budget.generate_report()

    # Sprawdzamy, czy raport zawiera odpowiednie informacje o transakcjach
    assert '2022-01-01: Wypłata (100)' in report
    assert '2022-01-02: Zakupy (-50)' in report
    assert '2022-01-03: Tankowanie (-20)' in report

    # Dodajemy wynik testu do pliku CSV
    with open('report_csv_e2e.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['test_end_to_end', budget.get_balance()])



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


def test_empty_budget_report(budget):
    #Testowanie generowania raportu z pustym budżetem (bez transakcji) 
    budget.transactions = []
    report = budget.generate_report()
    assert report == ''


def test_single_transaction_report(budget):
    #Testowanie generowania raportu z jedną transakcją
    budget.transactions = [Transaction(100, 'Wypłata', '2022-01-01')]
    report = budget.generate_report()
    assert report == '2022-01-01: Wypłata (100)\n'


def test_two_transactions_same_date_report(budget):
    #Testowanie generowania raportu z dwoma transakcjami o tej samej dacie
    budget.transactions = [
    Transaction(100, 'Wypłata', '2022-01-01'),
    Transaction(-50, 'Zakupy', '2022-01-01')
    ]
    report = budget.generate_report()
    assert '2022-01-01: Wypłata (100)\n' in report
    assert '2022-01-01: Zakupy (-50)\n' in report


def test_two_transactions_same_amount_description_report(budget):
    #dokończ Testowanie generowania raportu z dwoma transakcjami o tej samej kwocie i opisie 
    budget.transactions = [
    Transaction(100, 'Wypłata', '2022-01-01'),
    Transaction(100, 'Wypłata', '2022-01-02')
    ]
    report = budget.generate_report()
    assert '2022-01-01: Wypłata (100)' in report
    assert '2022-01-02: Wypłata (100)' in report


def test_two_transactions_different_amount_description_same_date_report(budget):
    #Testowanie generowania raportu z dwoma transakcjami o różnych kwotach i opisach, ale tej samej dacie
    budget.transactions = [
    Transaction(100, 'Wypłata', '2022-01-01'),
    Transaction(200, 'Zakupy', '2022-01-01')
    ]
    report = budget.generate_report()
    assert '2022-01-01: Wypłata (100)' in report
    assert '2022-01-01: Zakupy (200)' in report


# Testy E2E/akceptacyjne 
def test_end_to_end(budget):
    # Sprawdzamy, czy saldo jest poprawne
    assert budget.get_balance() == 30

    # Generujemy raport
    report = budget.generate_report()

    # Sprawdzamy, czy raport zawiera odpowiednie informacje o transakcjach
    assert '2022-01-01: Wypłata (100)' in report
    assert '2022-01-02: Zakupy (-50)' in report
    assert '2022-01-03: Tankowanie (-20)' in report
