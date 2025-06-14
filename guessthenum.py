import tkinter as tk
import random

# Function to start the game
def start_game():
    global number_to_guess, attempts
    number_to_guess = random.randint(1, 100)
    attempts = 0
    feedback_label.config(text="Guess a number between 1 and 100")
    attempts_label.config(text="Attempts: 0")
    guess_entry.delete(0, tk.END)
    guess_entry.config(state="normal")
    submit_button.config(state="normal")

# Function to handle player's guess
def guess_the_number():
    global attempts
    try:
        player_guess = int(guess_entry.get())
        attempts += 1
        attempts_label.config(text=f"Attempts: {attempts}")
        
        if player_guess < number_to_guess:
            feedback_label.config(text="Too low! Try again.")
        elif player_guess > number_to_guess:
            feedback_label.config(text="Too high! Try again.")
        else:
            feedback_label.config(text=f"Congratulations! You guessed it in {attempts} attempts.")
            guess_entry.config(state="disabled")
            submit_button.config(state="disabled")
    except ValueError:
        feedback_label.config(text="Please enter a valid number.")

# Set up the window
root = tk.Tk()
root.title("Guess the Number Game")
root.geometry("400x300")
root.config(bg="#D6EAF8")

# Game introduction
intro_label = tk.Label(root, text="Welcome to Guess the Number!", font=("Helvetica", 16, "bold"), bg="#D6EAF8")
intro_label.pack(pady=10)

instructions_label = tk.Label(root, text="I'm thinking of a number between 1 and 100.", font=("Helvetica", 12), bg="#D6EAF8")
instructions_label.pack(pady=5)

# User input
guess_entry = tk.Entry(root, font=("Helvetica", 14), bd=3, width=10)
guess_entry.pack(pady=10)

# Feedback
feedback_label = tk.Label(root, text="Guess a number between 1 and 100", font=("Helvetica", 14), bg="#D6EAF8")
feedback_label.pack(pady=5)

# Attempts Counter
attempts_label = tk.Label(root, text="Attempts: 0", font=("Helvetica", 12), bg="#D6EAF8")
attempts_label.pack(pady=5)

# Submit Button
submit_button = tk.Button(root, text="Submit Guess", font=("Helvetica", 14), bg="#5D6D7E", fg="white", command=guess_the_number)
submit_button.pack(pady=10)

# Reset Button
reset_button = tk.Button(root, text="Start New Game", font=("Helvetica", 14), bg="#58D68D", fg="white", command=start_game)
reset_button.pack(pady=5)

# Start the game
start_game()

# Run the application
root.mainloop()
