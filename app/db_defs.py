import sqlite3


def add_client(conn: sqlite3.Connection, cur: sqlite3.Cursor):
    while True:
        client_id = input("Podaj ID klienta: ")
        if client_id.isdigit():
            break
        else:
            print("ID klienta powinno być liczbą.")
    while True:
        client_name = input("Podaj imię klienta: ")
        if client_name.isalpha():
            break
        else:
            print("Imię klienta powinno składać się tylko z liter.")
    while True:
        client_surname = input("Podaj nazwisko klienta: ")
        if client_surname.isalpha():
            break
        else:
            print("Nazwisko klienta powinno składać się tylko z liter.")
    while True:
        client_pid = input("Podaj PESEL klienta: ")
        if client_pid.isdigit() and len(client_pid) == 11:
            break
        else:
            print("PESEL powinien składać się z 11 cyfr.")
    cur.execute("INSERT INTO Client VALUES (?, ?, ?, ?)", (client_id,
                                                           client_name,
                                                           client_surname,
                                                           client_pid))
    conn.commit()


def add_car(conn: sqlite3.Connection, cur: sqlite3.Cursor):
    while True:
        car_id = input("Podaj ID samochodu: ")
        if car_id.isdigit():
            break
        else:
            print("ID samochodu powinno być liczbą.")
    while True:
        client_id = input("Podaj ID klienta: ")
        if client_id.isdigit():
            break
        else:
            print("ID klienta powinno być liczbą.")
    brand = input("Podaj markę samochodu: ")
    while True:
        mileage = input("Podaj przebieg samochodu: ")
        if mileage.isdigit():
            break
        else:
            print("Przebieg powinien być liczbą.")
    while True:
        service_date = input("Podaj datę serwisu (DD-MM-YYYY): ")
        try:
            datetime.strptime(service_date, '%d-%m-%Y')
        except value_err:
            print("Niepoprawny format daty. Powinien być DD-MM-YYYY.")
    service_place = input("Podaj miejsce serwisu: ")
    cur.execute("INSERT INTO Car VALUES (?, ?, ?, ?, ?, ?)", (car_id,
                                                              client_id,
                                                              brand,
                                                              mileage,
                                                              service_date,
                                                              service_place))
    conn.commit()
