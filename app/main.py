import sqlite3
import db_defs
import export_to_csv

conn = sqlite3.connect('CarMileage.db')
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS Client(
        clientId INTEGER,
        clientName TEXT,
        clientSurname TEXT,
        clientPid TEXT
    );
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS Car(
        carId INTEGER,
        clientId INTEGER,
        brand TEXT,
        mileage INTEGER,
        serviceDate TEXT,
        servicePlace TEXT
    );
""")

while True:
    print("1. Dodaj klienta")
    print("2. Dodaj samochód")
    print("3. Wyeksportuj do CSV")
    print("4. Wyjdź")

    choice = input("Wybierz opcję: ")

    if choice == '1':
        db_defs.add_client(conn, cur)
    elif choice == '2':
        db_defs.add_car(conn, cur)
    elif choice == '3':
        export_to_csv.export_to_csv('dbAsCsv', cur)
    elif choice == '4':
        break
    elif choice == '5':
        print("Debug window")
        print("1. Usuń wszystko")

        choice = input("Wybierz opcje: ")

        if choice == '1':
            cur.execute("""DELETE FROM Client""")
            cur.execute("""DELETE FROM Car""")
            conn.commit()
        else:
            print("Nieznana opcja")
    else:
        print("Nieznana opcja")
