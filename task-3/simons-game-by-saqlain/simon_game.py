import tkinter as tk
import random

import random

class SimonGameLogic:
    def __init__(self):
        self.sequence = []
        self.player_sequence = []
        self.colors = ["red", "green", "blue", "yellow"]
        self.score = 0

    def start_game(self):
        self.sequence = []
        self.player_sequence = []
        self.score = 0
        self.add_to_sequence()
        return self.sequence

    def add_to_sequence(self):
        self.sequence.append(random.choice(self.colors))

    def check_sequence(self, color):
        self.player_sequence.append(color)
        if self.player_sequence == self.sequence:
            self.score += 1
            self.add_to_sequence()
            self.player_sequence = []
            return self.score
        elif not color == self.sequence[len(self.player_sequence) - 1]:
            return -1

    def get_colors(self):
        return self.colors


class SimonGameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Simon Game")
        self.master.geometry("400x400")

        self.sequence = []
        self.player_sequence = []
        self.colors = ["red", "green", "blue", "yellow"]
        self.score = 0

        self.create_widgets()

    def create_widgets(self):
        self.info_label = tk.Label(self.master, text="Click Start to Begin", font=("Arial", 12))
        self.info_label.pack(pady=10)

        self.start_button = tk.Button(self.master, text="Start", command=self.start_game)
        self.start_button.pack(pady=10)

        self.buttons_frame = tk.Frame(self.master)
        self.buttons_frame.pack()

        self.buttons = []
        for color in self.colors:
            button = tk.Button(self.buttons_frame, bg=color, width=10, height=5, command=lambda c=color: self.check_sequence(c))
            button.grid(row=self.colors.index(color)//2, column=self.colors.index(color)%2, padx=5, pady=5)
            self.buttons.append(button)

    def start_game(self):
        self.sequence = []
        self.player_sequence = []
        self.score = 0
        self.update_info("Watch the pattern")
        self.add_to_sequence()
        self.display_sequence()

    def add_to_sequence(self):
        self.sequence.append(random.choice(self.colors))

    def display_sequence(self):
        for i, color in enumerate(self.sequence, 1):
            self.master.after(i * 1000, self.highlight_button, color)
            self.master.after((i + 1) * 1000, self.reset_button_color)
        self.update_info("Repeat the pattern")

    def highlight_button(self, color):
        index = self.colors.index(color)
        self.buttons[index].config(relief=tk.SUNKEN)
        self.master.update()
        self.master.after(500, lambda: self.buttons[index].config(relief=tk.RAISED))

    def reset_button_color(self):
        for button in self.buttons:
            button.config(relief=tk.RAISED)

    def check_sequence(self, color):
        self.player_sequence.append(color)
        if self.player_sequence == self.sequence:
            self.score += 1
            self.update_info(f"Score: {self.score}")
            self.add_to_sequence()
            self.player_sequence = []
            self.display_sequence()
        elif not color == self.sequence[len(self.player_sequence) - 1]:
            self.game_over()

    def game_over(self):
        self.update_info(f"Game Over! Your score: {self.score}")
        self.player_sequence = []
        self.sequence = []

    def update_info(self, message):
        self.info_label.config(text=message)

if __name__ == "__main__":
    root = tk.Tk()
    simon_game = SimonGameGUI(root)
    root.mainloop()

