import tkinter as tk
import random

# Initialize scores
user_score = 0
computer_score = 0
choices = ["Rock", "Paper", "Scissors"]
icons = {"Rock": "🪨", "Paper": "📄", "Scissors": "✂️"}

# Function to play the game
def play(choice):
    global user_score, computer_score
    computer_choice = random.choice(choices)

    # Result logic
    if choice == computer_choice:
        result = "It's a Tie! 😐"
    elif (choice == "Rock" and computer_choice == "Scissors") or \
         (choice == "Paper" and computer_choice == "Rock") or \
         (choice == "Scissors" and computer_choice == "Paper"):
        user_score += 1
        result = "You Win! 🎉"
    else:
        computer_score += 1
        result = "You Lose! 😢"

    # Update GUI
    user_choice_label.config(text=f"👤 You: {icons[choice]} {choice}")
    comp_choice_label.config(text=f"💻 Computer: {icons[computer_choice]} {computer_choice}")
    result_label.config(text=result)
    score_label.config(text=f"Score — You: {user_score} | Computer: {computer_score}")

# Function to reset the game
def reset():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_choice_label.config(text="👤 You: -")
    comp_choice_label.config(text="💻 Computer: -")
    result_label.config(text="Result: -")
    score_label.config(text="Score — You: 0 | Computer: 0")

# Main GUI window
root = tk.Tk()
root.title("Rock Paper Scissors - CodSoft Task")
root.geometry("420x500")
root.config(bg="#e3f2fd")

# Title
tk.Label(root, text="Rock 🪨 Paper 📄 Scissors ✂️", font=("Helvetica", 20, "bold"), fg="#0d47a1", bg="#e3f2fd").pack(pady=20)

# Choices Buttons
btn_frame = tk.Frame(root, bg="#e3f2fd")
btn_frame.pack(pady=10)

def create_button(text, bg, cmd):
    return tk.Button(btn_frame, text=text, width=10, height=2, font=("Arial", 12, "bold"), bg=bg, fg="white",
                     activebackground="white", activeforeground=bg, command=cmd)

create_button("🪨 Rock", "#42a5f5", lambda: play("Rock")).grid(row=0, column=0, padx=10)
create_button("📄 Paper", "#66bb6a", lambda: play("Paper")).grid(row=0, column=1, padx=10)
create_button("✂️ Scissors", "#ef5350", lambda: play("Scissors")).grid(row=0, column=2, padx=10)

# Choice Labels
user_choice_label = tk.Label(root, text="👤 You: -", font=("Arial", 14), bg="#e3f2fd")
user_choice_label.pack(pady=10)

comp_choice_label = tk.Label(root, text="💻 Computer: -", font=("Arial", 14), bg="#e3f2fd")
comp_choice_label.pack(pady=5)

# Result
result_label = tk.Label(root, text="Result: -", font=("Arial", 16, "bold"), fg="#1b5e20", bg="#e3f2fd")
result_label.pack(pady=10)

# Scoreboard
score_label = tk.Label(root, text="Score — You: 0 | Computer: 0", font=("Arial", 14, "bold"), fg="#4a148c", bg="#e3f2fd")
score_label.pack(pady=10)

# Reset Button
tk.Button(root, text="🔄 Reset Score", font=("Arial", 12), bg="#ffd54f", command=reset).pack(pady=10)

# Exit
tk.Button(root, text="🚪 Exit", font=("Arial", 12), bg="#b0bec5", command=root.quit).pack(pady=5)

root.mainloop()
