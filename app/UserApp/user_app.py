import string
import psycopg
import simplejson


def get_client_all(connection: psycopg.Connection) -> list:
    """
    Pobiera wszystkich klientów z tabeli 'Client' w bazie danych.

    :param connection: Połączenie z bazą danych.
    :type connection: psycopg.Connection
    :return: Lista klientów.
    :rtype: list
    """
    cur = connection.cursor()

    # Pobierz wszystkich klientów
    clients = cur.execute("""SELECT * FROM Client""").fetchall()
    cur.close()
    return clients


def get_cars_all(connection: psycopg.Connection) -> list:
    """
    Pobiera wszystkie samochody z tabeli 'Car' w bazie danych.

    :param connection: Połączenie z bazą danych.
    :type connection: psycopg.Connection
    :return: Lista samochodów.
    :rtype: list
    """
    cur = connection.cursor()

    # Pobierz wszystkie samochody
    cars = cur.execute("""SELECT * FROM Car""").fetchall()
    cur.close()
    return cars


def get_client_by_name(client_name: string, connection: psycopg.Connection) -> list:
    """
    Pobiera klientów o określonym imieniu z tabeli 'Client' w bazie danych.

    :param client_name: Imię klienta.
    :type client_name: str
    :param connection: Połączenie z bazą danych.
    :type connection: psycopg.Connection
    :return: Lista klientów o podanym imieniu.
    :rtype: list
    """
    cur = connection.cursor()

    # Pobierz klientów o określonym imieniu
    clients = cur.execute("""SELECT * FROM Client WHERE clientName = %s""", (client_name,)).fetchall()
    cur.close()
    return clients


def get_client_by_surname(client_surname: string, connection: psycopg.Connection) -> list:
    """
    Pobiera klientów o określonym nazwisku z tabeli 'Client' w bazie danych.

    :param client_surname: Nazwisko klienta.
    :type client_surname: str
    :param connection: Połączenie z bazą danych.
    :type connection: psycopg.Connection
    :return: Lista klientów o podanym nazwisku.
    :rtype: list
    """
    cur = connection.cursor()

    # Pobierz klientów o określonym nazwisku
    clients = cur.execute("""SELECT * FROM Client WHERE clientSurname = %s""", (client_surname,)).fetchall()
    cur.close()
    return clients


def get_client_by_pid(client_pid: string, connection: psycopg.Connection) -> list:
    """
    Pobiera klientów o określonym numerze PESEL z tabeli 'Client' w bazie danych.

    :param client_pid: Numer PESEL klienta.
    :type client_pid: str
    :param connection: Połączenie z bazą danych.
    :type connection: psycopg.Connection
    :return: Lista klientów o podanym numerze PESEL.
    :rtype: list
    """
    cur = connection.cursor()

    # Pobierz klientów o określonym numerze PESEL
    clients = cur.execute("""SELECT * FROM Client WHERE clientPid = %s""", (client_pid,)).fetchall()
    cur.close()
    return clients


def get_cars_of_client(client_pid: string, connection: psycopg.Connection) -> (list, list):
    """
   Pobiera samochody klienta o określonym numerze PESEL z tabeli 'Car' w bazie danych.

   :param client_pid: Numer PESEL klienta.
   :type client_pid: str
   :param connection: Połączenie z bazą danych.
   :type connection: psycopg.Connection
   :return: Krotka zawierająca listę klientów i listę samochodów.
   :rtype: tuple
   """
    cur = connection.cursor()

    # Pobierz klienta o określonym numerze PESEL
    (client_id,) = cur.execute("""SELECT clientId FROM Client WHERE clientPid = %s""", (client_pid,)).fetchone()
    cars = cur.execute("""SELECT * FROM Car WHERE clientId = %s""", (client_id,)).fetchall()
    clients = cur.execute("""SELECT * FROM Client WHERE clientId = %s""", (client_id,)).fetchall()
    cur.close()
    return clients, cars

