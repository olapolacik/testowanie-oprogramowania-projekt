# pytest cache directory #

This directory contains data from the pytest's cache plugin,
which provides the `--lf` and `--ff` options, as well as the `cache` fixture.

**Do not** commit this to version control.

See [the docs](https://docs.pytest.org/en/stable/how-to/cache.html) for more information.


Oto przykładowa instrukcja, jak odpalić testy dla aplikacji budżetu domowego:

![alt text](img.png)

1. Uruchom terminal w katalogu z projektem.

2. Upewnij się, że masz zainstalowane wszystkie wymagane zależności, takie jak pytest i ewentualne wtyczki (np. pytest-html lub pytest-csv). Możesz to zrobić, używając polecenia:
$ **pip install -r requirements.txt**

3. Uruchom testy, używając polecenia pytest. To uruchomi wszystkie pliki z testami w bieżącym katalogu i podkatalogach.
Jeśli chcesz uruchomić testy tylko dla określonego pliku lub katalogu, możesz to zrobić, podając nazwę pliku lub ścieżkę do katalogu jako argument dla polecenia pytest. Na przykład, aby uruchomić testy dla pliku test_unit.py, użyj polecenia 
$ **pytest test_unit.py**

4. Jeśli chcesz wygenerować raport HTML lub CSV z wynikami testów, możesz to zrobić, używając odpowiedniej opcji. Aby wygenerować raport HTML, użyj opcji --html i podaj nazwę pliku, do którego chcesz zapisać raport. Na przykład, aby wygenerować raport HTML i zapisać go do pliku report.html, użyj polecenia 
$ **pytest --html=report.html**

Aby wygenerować raport CSV, użyj opcji --csv i podaj nazwę pliku, do którego chcesz zapisać raport. Na przykład, aby wygenerować raport CSV i zapisać go do pliku report.csv, użyj polecenia 
$ **pytest --csv=report.csv**

6. Możesz także użyć opcji **-v** lub **--verbose**, aby uzyskać bardziej szczegółowe informacje o przebiegu testów.