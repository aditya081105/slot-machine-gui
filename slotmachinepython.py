import tkinter as tk
import random
from tkinter import messagebox

# Slot symbols and their multipliers
symbols = {
    "🍒": 3,
    "🍋": 4,
    "🔔": 5,
    "⭐": 10,
    "     7️": 20
}

# Starting balance
balance = 200

def spin():
    global balance

    try:
        bet = int(bet_entry.get())
        if bet <= 0:
            messagebox.showwarning("Invalid Bet", "Bet must be a positive number.")
            return
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid number.")
        return

    if bet > balance:
        messagebox.showerror("Insufficient Balance", "You don’t have enough balance!")
        return

    balance -= bet

    # Spin the slots
    results = [random.choice(list(symbols.keys())) for _ in range(3)]
    for i, r in enumerate(results):
        slot_labels[i].config(text=r)

    if results[0] == results[1] == results[2]:
        symbol = results[0]
        multiplier = symbols[symbol]
        winnings = bet * multiplier
        balance += winnings
        result_label.config(text=f"🎉 You hit {symbol*3}! You won {winnings} Rs!")
    else:
        result_label.config(text="❌ You lost! Try again.")

    update_balance()

def update_balance():
    balance_label.config(text=f"Balance: {balance} Rs")
    if balance == 0:
        messagebox.showinfo("Game Over", "You lost all your money!\nThat's why you should never gamble 😄")
        root.destroy()

def reset_game():
    global balance
    balance = 200
    update_balance()
    result_label.config(text="")
    for lbl in slot_labels:
        lbl.config(text="❔")
    bet_entry.delete(0, tk.END)

def quit_game():
    root.destroy()

# GUI Setup
root = tk.Tk()
root.title("Slot Machine 💰")
root.geometry("400x450")
root.config(bg="#222")

# Title
tk.Label(root, text="🎰 Slot Machine 🎰", font=("Helvetica", 20, "bold"), fg="gold", bg="#222").pack(pady=10)

# Balance display
balance_label = tk.Label(root, text=f"Balance: {balance} Rs", font=("Helvetica", 14), fg="white", bg="#222")
balance_label.pack()

# Slot display
slot_frame = tk.Frame(root, bg="#222")
slot_frame.pack(pady=15)

slot_labels = []
for _ in range(3):
    lbl = tk.Label(slot_frame, text="❔", font=("Helvetica", 32), width=4, bg="#000", fg="white")
    lbl.pack(side="left", padx=10)
    slot_labels.append(lbl)

# Bet input
tk.Label(root, text="Enter your bet:", font=("Helvetica", 12), fg="white", bg="#222").pack(pady=5)
bet_entry = tk.Entry(root, font=("Helvetica", 12), justify="center")
bet_entry.pack(pady=5)

# Spin button
spin_button = tk.Button(root, text="🎲 Spin", font=("Helvetica", 14, "bold"), bg="green", fg="white", width=15, command=spin)
spin_button.pack(pady=10)

# Result message
result_label = tk.Label(root, text="", font=("Helvetica", 14), fg="cyan", bg="#222")
result_label.pack(pady=10)

# Control buttons
control_frame = tk.Frame(root, bg="#222")
control_frame.pack(pady=10)

tk.Button(control_frame, text="🔄 Reset", command=reset_game, width=10).grid(row=0, column=0, padx=10)
tk.Button(control_frame, text="❌ Quit", command=quit_game, width=10).grid(row=0, column=1, padx=10)

root.mainloop()
