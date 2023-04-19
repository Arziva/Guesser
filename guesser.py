import random
import tkinter as tk

class GuessNumberGUI:
    def __init__(self, master):
        self.master = master
        master.title("Guess the Number")

        self.secret_number = random.randint(1, 1000)
        self.max_attempts = min(15, int(self.secret_number / 50) + 5)
        self.attempts_left = self.max_attempts

        self.label = tk.Label(master, text="I'm thinking of a number between 1 and 1000. You have {} attempts to guess the number.".format(self.attempts_left))
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.button = tk.Button(master, text="Guess", command=self.check_guess)
        self.button.pack()

        self.status_label = tk.Label(master, text="")
        self.status_label.pack()

        self.play_again_button = tk.Button(master, text="Play Again", command=self.play_again, state="disabled")
        self.play_again_button.pack()

        self.high_scores_label = tk.Label(master, text="High Scores")
        self.high_scores_label.pack()

        self.high_scores = []
        self.high_scores_file = "high_scores.txt"

        try:
            with open(self.high_scores_file, "r") as f:
                for line in f:
                    name, score = line.strip().split(",")
                    self.high_scores.append((name, int(score)))
        except FileNotFoundError:
            with open(self.high_scores_file, "w") as f:
                pass

        self.high_scores_listbox = tk.Listbox(master, height=10)
        self.high_scores_listbox.pack()

        for name, score in self.high_scores:
            self.high_scores_listbox.insert(tk.END, "{}: {}".format(name, score))

    def check_guess(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            self.status_label.config(text="Invalid input! Please enter a number.")
            return

        if guess == self.secret_number:
            self.status_label.config(text=f"Congratulations! You guessed the number in {self.max_attempts - self.attempts_left + 1} attempts.")
            self.button.config(state="disabled")
            self.entry.config(state="disabled")
            self.play_again_button.config(state="normal")

            name = tk.simpledialog.askstring("High Score!", "You made a high score! Please enter your name:")
            self.high_scores.append((name, self.max_attempts - self.attempts_left + 1))
            self.high_scores.sort(key=lambda x: x[1])
            self.high_scores = self.high_scores[:10]

            with open(self.high_scores_file, "w") as f:
                for name, score in self.high_scores:
                    f.write("{},{}\n".format(name, score))

            self.high_scores_listbox.delete(0, tk.END)
            for name, score in self.high_scores:
                self.high_scores_listbox.insert(tk.END, "{}: {}".format(name, score))

            return

        if guess < self.secret_number:
            self.status_label.config(text="Your guess is too low.")
        else:
            self.status_label.config(text="Your guess is too high.")

        self.attempts_left -= 1
        self.label.config(text="I'm thinking of a number between 1 and 1000. You have {} attempts to guess the number.".format(self.attempts_left))

        self.entry.delete(0, tk.END)
        if self.attempts_left == 0:
            self.status_label.config(text=f"Sorry, you ran out of attempts. The number was {self.secret_number}.")
            self.button.config(state="disabled")
           
