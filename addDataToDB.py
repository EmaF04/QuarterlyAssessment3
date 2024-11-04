import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('questions.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table named "BMGT 4410" for questions and answers
cursor.execute('''
CREATE TABLE IF NOT EXISTS "BMGT 4410" (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT NOT NULL,
    option_d TEXT NOT NULL,
    correct_answer TEXT NOT NULL
)
''')

# List of questions and answers
DS3850questions = [
    ("What function is used to create a new database connection in Python's sqlite3 module?",
     "sqlite3.create()", "sqlite3.connect()", "sqlite3.new_connection()", "sqlite3.init()", "B"),
    ("Which of the following is NOT a valid data type in Python?",
     "str", "int", "char", "list", "C"),
    ("How do you check the type of a variable 'x' in Python?",
     "typeof(x)", "checktype(x)", "type(x)", "gettype(x)", "C"),
    ("Which keyword is used to define a function in Python?",
     "func", "def", "lambda", "function", "B"),
    ("What will the expression '5 + 4 * 3 - 2' evaluate to?",
     "17", "21", "11", "25", "A"),
    ("What is the correct way to start a `for` loop that iterates through a list called `items`?",
     "for item from items:", "foreach item in items:", "for item in items:", "loop item in items:", "C"),
    ("How do you add a comment in Python?",
     "// This is a comment", "# This is a comment", "/* This is a comment */", "-- This is a comment", "B"),
    ("Which method can be used to remove whitespace from the beginning and end of a string?",
     "strip()", "trim()", "cut()", "remove_whitespace()", "A"),
    ("What will be the result of 'print(2 ** 3)'?",
     "5", "8", "6", "Error", "B"),
    ("Which keyword is used to import a module in Python?",
     "include", "require", "import", "load", "C")
]

DS4210questions = [
    ("What is the primary function of Business Intelligence (BI) tools like Tableau and Power BI?",
     "Data storage", "Data visualization and analysis", "Data encryption", "Software development", "B"),
    ("In Tableau, what is the 'Sheet' used for?",
     "Creating dashboards", "Creating individual visualizations", "Data extraction", "Running scripts", "B"),
    ("Which type of chart is best for showing the relationship between two variables?",
     "Bar chart", "Line chart", "Scatter plot", "Pie chart", "C"),
    ("What is the main purpose of a dashboard in BI tools?",
     "To write code for data processing", "To display multiple visualizations in one place", "To store data securely", "To connect to databases", "B"),
    ("In Power BI, what is 'Power Query' used for?",
     "Creating visualizations", "Extracting, transforming, and loading data", "Running machine learning models", "Data encryption", "B"),
    ("Which file format is commonly used to export Tableau workbooks?",
     ".csv", ".twbx", ".xlsx", ".docx", "B"),
    ("In Tableau, what does the 'Show Me' feature do?",
     "Filters data", "Suggests the best type of visualization for selected data", "Connects to external databases", "Runs Python scripts", "B"),
    ("What language is used to create custom measures and calculated fields in Power BI?",
     "SQL", "DAX (Data Analysis Expressions)", "R", "Python", "B"),
    ("Which of the following is a key advantage of using Tableau?",
     "It requires advanced coding knowledge", "It has a steep learning curve", "It is user-friendly with drag-and-drop features", "It only supports static data sources", "C"),
    ("In Power BI, what is the function of the 'Power BI Service'?",
     "A tool for coding custom reports", "A cloud-based platform for sharing and collaborating on reports", "A feature to design dashboards", "An ETL tool", "B")
]

questions = [
    ("What is the main goal of conflict management in the workplace?",
     "To ignore conflicts", "To eliminate conflicts completely", "To manage and resolve conflicts effectively", "To escalate conflicts for management intervention", "C"),
    ("Which of the following is NOT a common conflict management style?",
     "Avoiding", "Competing", "Listening", "Collaborating", "C"),
    ("What is a key benefit of using the 'collaborating' conflict management style?",
     "Quick resolution without considering all viewpoints", "Finding a win-win solution for all parties", "Ignoring the conflict to avoid stress", "Dominating the discussion to achieve one's goals", "B"),
    ("In negotiation, what does the term 'BATNA' stand for?",
     "Best Alternative to a Negotiated Agreement", "Basic Agreement for Transparent Negotiation Assessment", "Balanced Approach to Negotiation Aims", "Business And Transactional Negotiation Analysis", "A"),
    ("Which skill is crucial for effective negotiation?",
     "Technical knowledge", "Active listening", "Financial expertise", "Programming skills", "B"),
    ("What is a common cause of conflict in the workplace?",
     "Well-defined roles", "Effective communication", "Poor communication and misunderstandings", "Abundant resources", "C"),
    ("Which of the following strategies involves finding a middle ground where both parties give up something?",
     "Competing", "Avoiding", "Compromising", "Accommodating", "C"),
    ("During a conflict resolution process, why is it important to separate the people from the problem?",
     "To assign blame easily", "To focus on attacking individuals", "To avoid personal biases and focus on resolving the issue", "To ensure emotions drive the negotiation", "C"),
    ("What is 'active listening' characterized by?",
     "Nodding without paying attention", "Repeating everything said by the speaker", "Giving full attention and providing feedback to the speaker", "Interrupting frequently to share opinions", "C"),
    ("In conflict management, what is the 'win-win' approach?",
     "Both parties lose equally", "One party wins at the expense of the other", "Both parties find a mutually beneficial solution", "The conflict remains unresolved", "C")
]


# Insert questions into the "BMGT 4410" table
for q in questions:
    cursor.execute('''
    INSERT INTO "BMGT 4410" (question, option_a, option_b, option_c, option_d, correct_answer)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', q)

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database created and questions inserted into the 'BMGT 4410' table successfully.")
