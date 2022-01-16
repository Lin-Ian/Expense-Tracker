import pandas as pd
import sqlite3


# Dictionary of supported categories
categories = {
    "H": "Housing",
    "G": "Grocery",
    "R": "Restaurant",
    "T": "Transportation",
    "P": "Personal",
    "M": "Miscellaneous"
}


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

    # Create cursor object
    cursor = connection.cursor()

    # Continue inserting data for as long as user requires
    while input("Would you like to enter a transaction?") == "y":
        # Get transaction data
        date = input("Date (YYYY-MM-DD): ")
        vendor = input("Vendor: ")
        category = get_category()
        amount = float(input("Amount ($): "))
        notes = input("Additional Notes: ")

        # Insert data into database
        cursor.execute("INSERT INTO expenses (date, vendor, category, amount, notes) VALUES (?,?,?,?,?)",
                       (date, vendor, category, amount, notes))
    connection.commit()

    cursor.close()


def read_csv(connection):
    """
    Read in a .csv file
    :param connection: connection object that represents the database
    :return: None
    """

    # Get file name from user
    file_name = input("Enter file name: ")
    df = pd.read_csv(file_name)

    # Convert dataframe to sql
    df.to_sql('expenses', connection, if_exists='append', index=False)

    connection.commit()


def get_category():
    category = input("Category: ")
    while category not in categories:
        category = input("Invalid category; Enter category: ")
    else:
        return categories[category]


def main():
    # Connect to database
    connection = connect_to_db()

    # Enter transaction data
    enter_transaction(connection)

    # Read file
    read_csv(connection)

    # Disconnect from database
    disconnect_from_db(connection)


if __name__ == "__main__":
    main()
