import tkinter as tk
from tkinter import messagebox

# Create the Tkinter window
window = tk.Tk()
window.title("Tic-Tac-Toe")

# Define the players
players = ['X', 'O']
current_player = players[0]

# Create the game board
board = [' ' for _ in range(9)]

# Function to handle button clicks
def handle_click(position):
    global current_player
    if board[position] == ' ':
        board[position] = current_player
        buttons[position].config(text=current_player)
        
        if check_win():
            messagebox.showinfo("Game Over", "Player " + current_player + " wins!")
            reset_game()
        elif ' ' not in board:
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_game()
        else:
            current_player = players[1] if current_player == players[0] else players[0]

# Function to check for a win
def check_win():
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]               # Diagonals
    ]

    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return True

    return False

# Function to reset the game
def reset_game():
    global current_player, board
    current_player = players[0]
    board = [' ' for _ in range(9)]
    for button in buttons:
        button.config(text=' ', state='normal')

# Create the buttons for the game board
buttons = []
for i in range(9):
    button = tk.Button(window, text=' ', width=10, height=5, command=lambda pos=i: handle_click(pos))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

# Start the Tkinter event loop
window.mainloop()
