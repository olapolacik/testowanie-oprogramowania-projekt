import pytest
import csv

def pytest_sessionfinish(session, exitstatus):
    with open('report_csv_unit.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['name', 'result'])
        writer.writeheader()
        for item in session.items:
            if 'unit' in item.keywords:
                writer.writerow({'name': item.name, 'result': item.outcome})


