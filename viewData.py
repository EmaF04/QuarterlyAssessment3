import sqlite3

def view_database_tables(db_file='questions.db'):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    # Get and print all table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables in the database:")
    for idx, table in enumerate(tables):
        print(f"{idx + 1}. {table[0]}")
    
    # Check if there are any tables
    if not tables:
        print("No tables found in the database.")
        conn.close()
        return
    
    # Ask the user to select a table
    table_choice = input("Enter the name of the table you want to view: ")
    
    # Check if the entered table exists
    if (table_choice,) not in tables:
        print("Table not found. Please enter a valid table name.")
        conn.close()
        return
    
    # Retrieve and print all data from the selected table
    try:
        cursor.execute(f"SELECT * FROM '{table_choice}'")
        rows = cursor.fetchall()
        
        # Print column headers
        column_names = [description[0] for description in cursor.description]
        print("\n" + "\t".join(column_names))
        
        # Print rows
        for row in rows:
            print("\t".join(str(item) for item in row))
    except Exception as e:
        print(f"An error occurred: {e}")
    
    # Close the connection
    conn.close()

# Call the function to view data in 'questions.db'
view_database_tables()
