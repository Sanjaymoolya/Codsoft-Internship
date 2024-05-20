import tkinter as tk
from tkinter import messagebox
import random

# Game logic to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        return "You win!"
    else:
        return "Computer wins!"

# Function to handle the user's choice
def play(user_choice):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")

    # Update scores
    global user_score, computer_score
    if "win" in result:
        user_score += 1
    elif "Computer" in result:
        computer_score += 1

    score_label.config(text=f"User: {user_score}  Computer: {computer_score}")

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="Make your choice!")
    score_label.config(text=f"User: {user_score}  Computer: {computer_score}")

# Main window setup
root = tk.Tk()
root.title(" Codsoft Rock-Paper-Scissors Game")

# Initial scores
user_score = 0
computer_score = 0

# Instruction label
tk.Label(root, text="Choose Rock, Paper, or Scissors:").pack(pady=10)

# Buttons for user choices
tk.Button(root, text="Rock", command=lambda: play("Rock")).pack(side=tk.LEFT, padx=20)
tk.Button(root, text="Paper", command=lambda: play("Paper")).pack(side=tk.LEFT, padx=20)
tk.Button(root, text="Scissors", command=lambda: play("Scissors")).pack(side=tk.LEFT, padx=20)

# Label to display the result
result_label = tk.Label(root, text="Make your choice!", font=('Helvetica', 12))
result_label.pack(pady=20)

# Label to display the score
score_label = tk.Label(root, text=f"User: {user_score}  Computer: {computer_score}", font=('Helvetica', 12))
score_label.pack(pady=10)

# Reset button
tk.Button(root, text="Reset Game", command=reset_game).pack(pady=10)

# Start the main loop
root.mainloop()
