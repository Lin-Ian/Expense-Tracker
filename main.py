import sqlite3


def connect_to_db():
    """
    Set up connection to sqlite database
    :return: None
    """

    connection = sqlite3.connect("identifier.sqlite")
    cursor = connection.cursor()
    print("Connected to sqlite")
    cursor.execute('CREATE TABLE IF NOT EXISTS expenses(date TEXT, vendor TEXT, category TEXT, amount INT, notes TEXT)')


def main():
    connect_to_db()


if __name__ == "__main__":
    main()
