import csv
import sqlite3


def export_to_csv(file_name, cur: sqlite3.Cursor):
    """
    Eksportuje dane z bazy danych do pliku CSV.

    :param file_name: Nazwa pliku CSV.
    :type file_name: str
    :param cur: Kursor do bazy danych.
    :type cur: sqlite3.Cursor
    """
    cur.execute("""SELECT name FROM sqlite_master WHERE type='table';""")
    tables = cur.fetchall()

    with open(file_name + '.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        for table in tables:
            table = table[0]
            cur.execute(f"SELECT * FROM {table}")
            rows = cur.fetchall()

            column_names = [description[0] for description in cur.description]

            # Zapisz nazwę tabeli i nagłówki kolumn
            writer.writerow([table])
            writer.writerow(column_names)

            # Zapisz dane wierszy
            writer.writerows(rows)

            # Oddziel kolejne tabele pustym wierszem
            writer.writerow([])
