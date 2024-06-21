import string
import psycopg
import simplejson


def get_client_all(connection: psycopg.Connection) -> list:
    cur = connection.cursor()
    clients = cur.execute("""SELECT * FROM Client""").fetchall()
    cur.close()
    return clients


def get_cars_all(connection: psycopg.Connection) -> list:
    cur = connection.cursor()
    cars = cur.execute("""SELECT * FROM Car""").fetchall()
    cur.close()
    return cars


def get_client_by_name(client_name: string, connection: psycopg.Connection) -> list:
    cur = connection.cursor()
    clients = cur.execute("""SELECT * FROM Client WHERE clientName = %s""", (client_name,)).fetchall()
    cur.close()
    return clients


def get_client_by_surname(client_surname: string, connection: psycopg.Connection) -> list:
    cur = connection.cursor()
    clients = cur.execute("""SELECT * FROM Client WHERE clientSurname = %s""", (client_surname,)).fetchall()
    cur.close()
    return clients


def get_client_by_pid(client_pid: string, connection: psycopg.Connection) -> list:
    cur = connection.cursor()
    clients = cur.execute("""SELECT * FROM Client WHERE clientPid = %s""", (client_pid,)).fetchall()
    cur.close()
    return clients


def get_cars_of_client(client_pid: string, connection: psycopg.Connection) -> (list, list):
    cur = connection.cursor()
    (client_id,) = cur.execute("""SELECT clientId FROM Client WHERE clientPid = %s""", (client_pid,)).fetchone()
    cars = cur.execute("""SELECT * FROM Car WHERE clientId = %s""", (client_id,)).fetchall()
    clients = cur.execute("""SELECT * FROM Client WHERE clientId = %s""", (client_id,)).fetchall()
    cur.close()
    return clients, cars


with open('./db_creds_home.json') as f:
    db_creds = simplejson.load(f)
    conn = psycopg.connect(
        host=db_creds['host'],
        port=db_creds['port'],
        user=db_creds['user'],
        dbname=db_creds['db_name'],
        password=db_creds['password']
    )

while True:
    print("1. Pobierz wszystkich klientów")
    print("2. Pobierz wszystkie samochody")
    print("3. Pobierz klienta")
    print("4. Pobierz samochódy klienta")
    print("5. Wyjdź")

    choice = input("Wybierz opcję: ")

    if choice == '1':
        for row in get_client_all(conn):
            print(row)
    elif choice == '2':
        for row in get_cars_all(conn):
            print(row)
    elif choice == '3':
        print("1. Wybierz po imieniu")
        print("2. Wybierz po nazwisku")
        print("3. Wybierz po numerze pesel")

        user_choice = input("Wybierz opcję: ")

        if user_choice == '1':
            for row in get_client_by_name(input("Podaj imie klienta: "), conn):
                print(row)
        elif user_choice == '2':
            for row in get_client_by_surname(input("Podaj nazwisko klienta: "), conn):
                print(row)
        elif user_choice == '3':
            for row in get_client_by_pid(input("Podaj pesel klienta: "), conn):
                print(row)
        pass
    elif choice == '4':
        car_brand = input("Wprowadź pesel klienta: ")
        for row in get_cars_of_client(car_brand, conn):
            print(row)
    elif choice == '5':
        break
