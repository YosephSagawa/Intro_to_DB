import mysql.connector

def create_database():
    try:
        # Connect to MySQL server (update user & password as needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",        # Change if using another user
            password="yourpassword"   # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if it does not exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Ensure proper cleanup
        try:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed.")
        except NameError:
            # connection was never created
            pass

if __name__ == "__main__":
    create_database()
