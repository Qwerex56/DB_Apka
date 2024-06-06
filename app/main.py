import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

#cur.execute("CREATE DATABSE CarMileageService IF NOT EXISTS")
cur.execute(""""CREATE TABLE IF NOT EXISTS Client(
                    clientId INTEGER,
                    clientName TEXT,
                    clientSurname TEXT,
                    clientPid TEXT
            );""")

cur.execute("""CREATE TABLE IF NOT EXISTS Car(
                    carId INTEGER,
                    clientId INTEGER,
                    
                    brand TEXT,
                    mileage INTEGER,
                    serviceDate TEXT,
                    servicePlace TEXT
            );""")


while (true):
    uInput = input("Select an operation: ")

