import csv
import sqlite3


def export_to_csv(file_name, cur: sqlite3.Cursor):
    cur.execute("""SELECT name FROM sqlite_master WHERE type='table';""")
    tables = cur.fetchall()

    with open(file_name + '.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        for table in tables:
            table = table[0]
            cur.execute(f"SELECT * FROM {table}")
            rows = cur.fetchall()

            column_names = [description[0] for description in cur.description]

            writer.writerow([table])
            writer.writerow(column_names)
            writer.writerows(rows)
            writer.writerow([])
