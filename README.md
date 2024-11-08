# QuarterlyAssessment3

# userQuiz.py
Description:
This Python application uses the Tkinter library to create a graphical user interface (GUI) that allows users to select a category of questions from a database (questions.db) and then go through a quiz. The quiz presents one question at a time, along with multiple-choice options, and provides feedback on whether the selected answer is correct or not. The user's score is tracked, and at the end of the quiz, the final score is displayed.

The application interacts with an SQLite database where questions and their corresponding answer options are stored in different tables, each representing a course or category.

Features:
Category Selection: Users can select from several predefined categories (e.g., MKT 4200, DS 3850, etc.).
Quiz Interaction: Once a category is selected, the user is presented with a series of multiple-choice questions one at a time.
Answer Feedback: After submitting an answer, the user is given feedback on whether their answer was correct or incorrect.
Score Tracking: The user's score is tracked throughout the quiz and displayed at the end.
Question Display: The questions, answer options, and correct answers are fetched from the SQLite database based on the selected category.
Requirements:
Python 3.x
Tkinter (usually included with Python installations)
sqlite3 (usually included with Python installations)
A database file (questions.db) with tables containing the questions for each category (e.g., MKT 4200, DS 3850).
How it Works:
Database Structure:

The questions.db file should contain multiple tables, each representing a course or category (e.g., "MKT 4200", "DS 3850").
Each table should have the following columns:
id: Unique identifier for each question (integer).
question: The question text (text).
option_a, option_b, option_c, option_d: The answer options (text).
correct_answer: The correct answer (string, should be "A", "B", "C", or "D").
GUI Interface:

Upon running the program, a main window is displayed where users can select a question category.
After choosing a category and clicking "Submit", the program loads and displays questions from the selected category one by one.
For each question, users can choose one of the options (A, B, C, or D) and submit their answer.
Feedback is given after each question, indicating whether the answer was correct or incorrect.
Once all questions are answered, the final score is shown.
Error Handling:

If the user tries to submit without selecting a category, a warning message is displayed.
If there are no more questions in the selected category, a message is shown indicating that the quiz has ended.

# addDataToDB.py
Description:
This Python script provides a template for adding more tables (classes) to the questions.db database. The most recently added table was DS 4220

The script ensures that the table is created only if it does not already exist. It then inserts a series of questions related to various subjects (e.g., Business Intelligence, Python programming, statistical methods) into the table. After all questions are inserted, the script commits the changes and closes the database connection.

Requirements:
Python 3.x
sqlite3 module (built-in in Python)
Features:
Database Creation: The script connects to an SQLite database (questions.db). If the database doesn't exist, it will be created.
Table Creation: The script creates a table named "DS 4220" if it doesn't already exist. This table will store questions for the specified course.
Question Insertion: A predefined list of questions (with options and the correct answer) is inserted into the table.
Data Integrity: The table creation is checked with CREATE TABLE IF NOT EXISTS to avoid redundant table creation.
Database Structure:
Table Name: "DS 4220"
Columns:
id (INTEGER PRIMARY KEY AUTOINCREMENT): A unique identifier for each question.
question (TEXT): The question text.
option_a, option_b, option_c, option_d (TEXT): The four possible answer options.
correct_answer (TEXT): The correct answer (one of "A", "B", "C", or "D").
Example Table Structure:
sql
Copy code
CREATE TABLE IF NOT EXISTS "DS 4220" (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT NOT NULL,
    option_d TEXT NOT NULL,
    correct_answer TEXT NOT NULL
);
How It Works:
Database Connection: The script connects to the SQLite database file questions.db. If the file does not exist, SQLite automatically creates it.
Table Creation: The script checks if the table "DS 4220" exists. If it does not exist, the table is created to store the quiz questions.
Question Insertion: A set of predefined questions related to Python, statistical analysis, and business intelligence is inserted into the database. Each question is inserted with its answer options and the correct answer.
Commit Changes: After all questions are inserted, the changes are committed to the database.
Close Connection: The database connection is closed to finalize the operations.

# deleteQuestions.py
Description:
This Python script allows the user to remove a question from a specified table in an SQLite database (questions.db). The script provides an interactive way for users to select a table and a question from that table, and then delete the chosen question. This functionality is useful for managing and maintaining the database of quiz or test questions.

The script connects to the SQLite database, lists available tables, prompts the user to select a table and a question, and then deletes the selected question from the database. It handles errors such as invalid input and missing data gracefully, ensuring the user can navigate the process smoothly.

Requirements:
Python 3.x
sqlite3 module (built-in in Python)
Features:
Database Connection: The script connects to an SQLite database (questions.db), ensuring the user can interact with the tables stored within.
Table Selection: The user is presented with a list of all available tables in the database, which allows them to choose the one containing the questions they want to modify.
Question Selection: After selecting a table, the user can view all questions in that table and choose one by its ID for removal.
Error Handling: The script handles errors such as invalid table numbers, invalid question IDs, and non-integer inputs gracefully.
Database Structure:
Table Structure: The script assumes the database (questions.db) contains one or more tables with the following columns:
id (INTEGER PRIMARY KEY AUTOINCREMENT): A unique identifier for each question.
question (TEXT): The question text.
Example Table Structure:
sql
Copy code
CREATE TABLE "DS 4220" (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL
);
How It Works:
Database Connection: The script connects to the questions.db SQLite database. If no database file exists, the user will not be able to proceed.
Table Listing: The script retrieves and displays all table names in the database.
Table Selection: The user is asked to select the table from which they want to remove a question.
Question Listing: Once a table is selected, the script fetches and displays all questions in that table with their unique IDs.
Question Removal: The user selects the ID of the question they wish to delete. The script then removes the chosen question from the table.
Confirmation and Cleanup: After the question is removed, a confirmation message is displayed, and the database connection is closed.

# viewData.py
Description:
This Python script allows users to interact with an SQLite database (questions.db) to view its structure and the data stored in its tables. The script connects to the database, lists all available tables, and allows the user to select a table to view the contents. The user can view the column headers and all the data rows within the selected table.

The script is designed for ease of use, providing clear prompts and error handling to ensure smooth interaction.

Requirements:
Python 3.x
sqlite3 module (built-in in Python)
Features:
Database Connection: Connects to the questions.db SQLite database.
Table Listing: Displays all available tables in the database.
Table Selection: Prompts the user to select a table by its name.
Data Viewing: Displays all the data from the selected table, including column names and rows.
Error Handling: Handles errors such as invalid table names or connection issues.
Database Structure:
The script assumes the database (questions.db) contains one or more tables. Each table should have columns and rows with data, and the script will display all of this information for the selected table.

Example table structure might look like:

sql
Copy code
CREATE TABLE "DS 4220" (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT NOT NULL,
    option_d TEXT NOT NULL,
    correct_answer TEXT NOT NULL
);
How It Works:
Database Connection: The script connects to the questions.db SQLite database.
Table Listing: All available tables in the database are retrieved and listed for the user.
Table Selection: The user is asked to enter the name of the table they want to view.
Data Display: Once a table is selected, the script retrieves all rows from that table and prints the data in a tabular format. The column names are displayed at the top of the table.
Error Handling: If the user selects an invalid table or an error occurs while querying the database, appropriate error messages are displayed.