import sqlite3

def remove_question_from_db(db_file='questions.db'):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Get and print all table names in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    if not tables:
        print("No tables found in the database.")
        conn.close()
        return
    
    # Display tables for the user to choose from
    print("Tables in the database:")
    for idx, table in enumerate(tables):
        print(f"{idx + 1}. {table[0]}")
    
    # Ask the user to select a table
    table_choice = input("Enter the number of the table you want to remove questions from: ")
    
    try:
        table_choice = int(table_choice)
        if table_choice < 1 or table_choice > len(tables):
            print("Invalid table number.")
            conn.close()
            return
    except ValueError:
        print("Invalid input. Please enter a number corresponding to the table.")
        conn.close()
        return
    
    # Get the selected table name
    table_name = tables[table_choice - 1][0]

    # Get and print all questions in the selected table
    cursor.execute(f"SELECT id, question FROM \"{table_name}\"")
    questions = cursor.fetchall()
    
    if not questions:
        print(f"No questions found in the table {table_name}.")
        conn.close()
        return
    
    # Display questions for the user to choose from
    print(f"Questions in the table '{table_name}':")
    for idx, (q_id, question) in enumerate(questions):
        print(f"{q_id}. {question}")
    
    # Ask the user for the ID of the question to remove
    question_choice = input("Enter the ID of the question you want to remove: ")
    
    try:
        question_id = int(question_choice)
        if not any(q_id == question_id for q_id, _ in questions):
            print("Invalid question ID. Please enter a valid ID.")
            conn.close()
            return
    except ValueError:
        print("Invalid input. Please enter a valid integer for the question ID.")
        conn.close()
        return
    
    # Delete the question from the selected table
    cursor.execute(f"DELETE FROM \"{table_name}\" WHERE id = ?", (question_id,))
    conn.commit()
    
    print(f"Question with ID {question_id} has been removed from the '{table_name}' table.")
    
    # Close the connection
    conn.close()

# Call the function to remove a question
remove_question_from_db()
