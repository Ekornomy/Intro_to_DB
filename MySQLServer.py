 #!/usr/bin/python3
"""
MySQLServer.py - Creates alx_book_store database
"""

import mysql.connector
from mysql.connector import Error

def main():
    """Main function to create database"""
    # Initialize connection as None
    connection = None
    
    try:
        # Try to establish connection
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )
        
        # Check if connected
        if connection.is_connected():
            # Create cursor
            cursor = connection.cursor()
            
            # Create database without using SELECT or SHOW
            create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
            
            # Execute the query
            cursor.execute(create_db_query)
            
            # Print success message
            print("Database 'alx_book_store' created successfully!")
            
            # Close cursor
            cursor.close()
    
    except Error as e:
        # Handle MySQL connection errors
        print(f"Error connecting to MySQL: {e}")
        
    except Exception as e:
        # Handle any other exceptions
        print(f"An error occurred: {e}")
        
    finally:
        # Always close the connection if it was opened
        if connection is not None and connection.is_connected():
            connection.close()
            print("MySQL connection closed")

if __name__ == "__main__":
    main()