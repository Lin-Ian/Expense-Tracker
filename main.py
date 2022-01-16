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


def enter_transaction(connection):
    """
    Get transaction data from user and insert it into the database
    :param connection: connection object that represents the database
    :return: None
    """

    # Get transaction data
    date = input("Date (YYYY-MM-DD): ")
    vendor = input("Vendor: ")
    category = input("Category: ")
    amount = float(input("Amount ($): "))
    notes = input("Additional Notes: ")

    # Insert data into database
    cursor = connection.cursor()
    cursor.execute("INSERT INTO expenses (date, vendor, category, amount, notes) VALUES (?,?,?,?,?)",
                   (date, vendor, category, amount, notes))
    connection.commit()
    cursor.close()


def main():
    # Connect to database
    connection = connect_to_db()

    # Enter transaction data
    enter_transaction(connection)

    # Disconnect from database
    disconnect_from_db(connection)


if __name__ == "__main__":
    main()
