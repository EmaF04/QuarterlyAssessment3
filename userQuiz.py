import tkinter as tk
from tkinter import messagebox
import sqlite3

# Connect to the database
conn = sqlite3.connect('questions.db')
cursor = conn.cursor()

# Function to display the selected category's questions one at a time
def show_questions_window(category):
    root.destroy()  # Close the first window

    # Fetch questions from the database for the selected category
    cursor.execute(f'SELECT id, question, option_a, option_b, option_c, option_d, correct_answer FROM "{category}"')
    questions = cursor.fetchall()

    # Create a new window for questions
    questions_window = tk.Tk()
    questions_window.title(f"Questions for {category}")
    questions_window.geometry("600x400")

    # Track the current question index
    current_question_index = 0
    score = 0

    # Function to display the next question
    def display_question():
        # Clear previous question widgets
        for widget in questions_window.winfo_children():
            widget.destroy()

        # Check if there are more questions
        if current_question_index < len(questions):
            question_id, question_text, option_a, option_b, option_c, option_d, correct_answer = questions[current_question_index]

            # Display the question text
            tk.Label(questions_window, text=f"Q{current_question_index + 1}: {question_text}").pack(anchor='w', padx=20, pady=10)

            # Variable to hold the selected answer
            answer_var = tk.StringVar(value="")

            # Function to check the answer and provide feedback
            def check_answer():
                nonlocal score, current_question_index
                selected_answer = answer_var.get()

                # Provide feedback on the answer
                if selected_answer == correct_answer:
                    messagebox.showinfo("Feedback", "Correct!")
                    score += 1
                else:
                    messagebox.showinfo("Feedback", f"Incorrect! The correct answer was {correct_answer}.")

                # Move to the next question
                current_question_index += 1
                display_question()

            # Display radio buttons for each answer option
            tk.Radiobutton(questions_window, text=option_a, variable=answer_var, value="A").pack(anchor='w', padx=40)
            tk.Radiobutton(questions_window, text=option_b, variable=answer_var, value="B").pack(anchor='w', padx=40)
            tk.Radiobutton(questions_window, text=option_c, variable=answer_var, value="C").pack(anchor='w', padx=40)
            tk.Radiobutton(questions_window, text=option_d, variable=answer_var, value="D").pack(anchor='w', padx=40)

            # Button to submit the answer and move to the next question
            tk.Button(questions_window, text="Submit Answer", command=check_answer).pack(pady=20)

        else:
            # No more questions left, display the final score
            messagebox.showinfo("Quiz Completed", f"You scored {score} out of {len(questions)}")
            questions_window.destroy()

    # Display the first question
    display_question()

    # Run the questions window loop
    questions_window.mainloop()

# Function to select a category and open the questions window
def select_category():
    selected_category = category_var.get()
    if selected_category:
        show_questions_window(selected_category)  # Use the selected category name as is
    else:
        messagebox.showwarning("No Selection", "Please select a category.")

# Create the main window for category selection
root = tk.Tk()
root.title("Select Question Category")
root.geometry("300x250")

# Label for instructions
label = tk.Label(root, text="Select a category of questions:")
label.pack(pady=10)

# Variable to hold the selected category
category_var = tk.StringVar(value="")

# Categories for questions
categories = ["MKT 4200", "DS 3850", "DS 4220", "DS 4210", "BMGT 4410"]

# Radio buttons for each category
for category in categories:
    tk.Radiobutton(root, text=category, variable=category_var, value=category).pack(anchor='w')

# Submit button to confirm the selection
tk.Button(root, text="Submit", command=select_category).pack(pady=20)

# Run the main event loop
root.mainloop()

# Close the database connection when the application exits
conn.close()
