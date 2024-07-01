import user_app

# Otwórz plik z danymi połączenia do bazy danych
with open('./db_creds_home.json') as f:
    db_creds = simplejson.load(f)

    # Nawiąż połączenie z bazą danych
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
        # Pobierz wszystkich klientów
        for row in get_client_all(conn):
            print(row)
    elif choice == '2':
        # Pobierz wszystkie samochody
        for row in get_cars_all(conn):
            print(row)
    elif choice == '3':
        print("1. Wybierz po imieniu")
        print("2. Wybierz po nazwisku")
        print("3. Wybierz po numerze pesel")

        user_choice = input("Wybierz opcję: ")

        if user_choice == '1':
            # Pobierz klientów o określonym imieniu
            for row in get_client_by_name(input("Podaj imie klienta: "), conn):
                print(row)
        elif user_choice == '2':
            # Pobierz klientów o określonym nazwisku
            for row in get_client_by_surname(input("Podaj nazwisko klienta: "), conn):
                print(row)
        elif user_choice == '3':
            # Pobierz klientów o określonym numerze PESEL
            for row in get_client_by_pid(input("Podaj pesel klienta: "), conn):
                print(row)
        pass
    elif choice == '4':
        # Pobierz samochody przypisane do klienta o określonym numerze PESEL
        car_brand = input("Wprowadź pesel klienta: ")
        for row in get_cars_of_client(car_brand, conn):
            print(row)
    elif choice == '5':
        break
