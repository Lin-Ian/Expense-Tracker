import sqlite3


def connect_to_db():
    """
    Set up connection to sqlite database
    :return: connection object that represents the database
    """

    # Connect to sqlite database
    connection = sqlite3.connect("identifier.sqlite")
    cursor = connection.cursor()
    print("Connected to sqlite")

    # Create table if it does not exist
    cursor.execute('CREATE TABLE IF NOT EXISTS expenses(date TEXT, vendor TEXT, category TEXT, amount INT, notes TEXT)')
    cursor.close()

    # Return the connection to be used later on
    return connection


def disconnect_from_db(connection):
    """
    Close the connection to sqlite database
    :param connection: connection object that represents the database
    :return: None
    """
    connection.close()
    print("Connection to sqlite closed")


def main():
    # Connect to database
    connection = connect_to_db()

    # Disconnect from database
    disconnect_from_db(connection)


if __name__ == "__main__":
    main()
