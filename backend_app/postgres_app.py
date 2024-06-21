import datetime
import psycopg
import csv
import random

import simplejson


def initialize_car_service_db(conn_data):
    conn = psycopg.connect(
        host=conn_data['host'],
        port=conn_data['port'],
        user=conn_data['user'],
        dbname=conn_data['db_name'],
        password=conn_data['password']
    )
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Client (
            clientId SERIAL PRIMARY KEY,
            clientName VARCHAR(50),
            clientSurname VARCHAR(50),
            clientPid VARCHAR(11)
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Car (
            carId SERIAL PRIMARY KEY,
            clientId INT REFERENCES Client(clientId),
            brand VARCHAR(50),
            mileage INT,
            serviceDate DATE,
            servicePlace VARCHAR(50)
        );
    """)

    conn.commit()

    cur.close()
    conn.close()


def generate_random_data_client(conn_data):
    conn = psycopg.connect(
        host=conn_data['host'],
        port=conn_data['port'],
        user=conn_data['user'],
        dbname=conn_data['db_name'],
        password=conn_data['password']
    )
    cur = conn.cursor()

    names = ["Aleksander", "Kacper", "Patryk", "Bartosz", "Maciej"]
    surnames = ["Wiśniewski", "Wójcik", "Kowalczyk", "Kamiński", "Lewandowski"]

    for _ in range(100):
        rand_name = random.choice(names)
        rand_surname = random.choice(surnames)
        rand_pid = '12345678900'

        cur.execute("""
            INSERT INTO Client (clientName, clientSurname, clientPid)
                VALUES (%s, %s, %s);
        """, (rand_name, rand_surname, rand_pid))

    conn.commit()

    cur.close()
    conn.close()


def generate_random_data_car(conn_data):
    conn = psycopg.connect(
        host=conn_data['host'],
        port=conn_data['port'],
        user=conn_data['user'],
        dbname=conn_data['db_name'],
        password=conn_data['password']
    )
    cur = conn.cursor()

    first_index = cur.execute("""SELECT clientId FROM Client""").fetchall()[0][0]
    last_index = cur.execute("""SELECT clientId FROM Client""").fetchall()[-1][0]

    car_brands = ["Audi", "BMW", "Ferrari", "Ford", "McLaren"]
    car_services = ["Wave Motors", "Magnate Automotive", "Phoenix Motors", "Business Streamline", "Apollo Automotive"]
    car_services_place = ["Nowa Ruda", "Waldenburg", "Wrocław", "Kłodzko", "Lisia"]

    for _ in range(last_index * 2):
        rand_client = random.randint(first_index, last_index)
        rand_brand = random.choice(car_brands)
        rand_mileage = random.randint(100, 9999999)
        rand_service_date = datetime.date.today()
        rand_place = random.choice(car_services_place)

        cur.execute("""
            INSERT INTO Car (clientId, brand, mileage, serviceDate, servicePlace)
                VALUES (%s, %s, %s, %s, %s);
        """, (rand_client, rand_brand, rand_mileage, rand_service_date, rand_place))

    conn.commit()

    cur.close()
    conn.close()


def delete_from_database_clients(conn_data):
    conn = psycopg.connect(
        host=conn_data['host'],
        port=conn_data['port'],
        user=conn_data['user'],
        dbname=conn_data['db_name'],
        password=conn_data['password']
    )
    cur = conn.cursor()

    cur.execute("""
        DELETE * FROM Client;
    """)

    conn.commit()

    cur.exit()
    conn.exit()


def delete_from_database_cars(conn_data):
    conn = psycopg.connect(
        host=conn_data['host'],
        port=conn_data['port'],
        user=conn_data['user'],
        dbname=conn_data['db_name'],
        password=conn_data['password']
    )
    cur = conn.cursor()

    cur.execute("""
        DELETE * FROM Car;
    """)

    conn.commit()

    cur.exit()
    conn.exit()


def delete_from_database_all(conn_data):
    conn = psycopg.connect(
        host=conn_data['host'],
        port=conn_data['port'],
        user=conn_data['user'],
        dbname=conn_data['db_name'],
        password=conn_data['password']
    )
    cur = conn.cursor()

    cur.execute("""
        DELETE * FROM Car;
        DELETE * FROM Client;
    """)

    conn.commit()

    cur.exit()
    conn.exit()


def import_from_csv(csv_file_path, conn_data):
    """
    Load data from remote csv file

    :param csv_file_path: Path to csv file.
    :type csv_file_path: basestring
    :param conn_data: Parsed json file with data needed to build connection string.
    :type conn_data: any
    """
    conn = psycopg.connect(
        host=conn_data['host'],
        port=conn_data['port'],
        user=conn_data['user'],
        dbname=conn_data['db_name'],
        password=conn_data['password']
    )
    cur = conn.cursor()

    try:
        with open(csv_file_path, 'r') as file:
            reader = csv.reader(file)
            table = "a"

            for row in reader:
                if len(row) <= 0:
                    continue

                if row[0] == 'Client':
                    table = row[0]
                    next(reader)
                    continue
                elif row[0] == 'Car':
                    table = row[0]
                    next(reader)
                    continue

                print(row, table)
                if table == 'Client':
                    rand_name, rand_surname, rand_pid = row[1:4]
                    cur.execute("""
                        INSERT INTO Client (clientName, clientSurname, clientPid)
                            VALUES (%s, %s, %s);
                        """, (rand_name, rand_surname, rand_pid))
                elif table == 'Car':
                    client_id, brand, mileage, service_date, service_place = row[1:6]
                    cur.execute("""
                        INSERT INTO Car (clientId, brand, mileage, serviceDate, servicePlace)
                            VALUES (%s, %s, %s, %s, %s);
                     """, (client_id, brand, mileage, service_date, service_place))
                    pass

        conn.commit()
        print("Data imported correctly")
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        cur.close()
        conn.close()


with open('./db_creds_home.json') as f:
    db_creds = simplejson.load(f)
    initialize_car_service_db(db_creds)
    import_from_csv('../app/dbAsCsv.csv', db_creds)
