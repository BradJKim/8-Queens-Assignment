import tkinter as tk
import webbrowser
from Game import *

game = Game()

def main():
    r = tk.Tk()
    r.title('8 Queens Genetic Algorithm')

    r.geometry("500x600")

    rows, cols = 8, 8
    square_size = 60  # Size of each square

    for row in range(rows):
        for col in range(cols):
            color = 'white' if (row + col) % 2 == 0 else 'black'

            label = tk.Label(r, bg=color, width=square_size//10, height=square_size//20)
            label.grid(row=row, column=col)

    button_frame = tk.Frame(r)
    button_frame.grid(row=rows+1, column=0, columnspan=cols)

    reset_button = tk.Button(button_frame, text="Reset", command=lambda: reset_game())
    reset_button.pack(side=tk.LEFT, padx=10, pady=10)

    start_button = tk.Button(button_frame, text="Start", command=lambda: start_game())
    start_button.pack(side=tk.LEFT, padx=10, pady=10)

    link_label = tk.Label(r, text="Click here to visit Github Repo", fg="blue", cursor="hand2")
    link_label.grid(row=rows+2, column=0, columnspan=cols, pady=10)
    link_label.bind("<Button-1>", lambda e: webbrowser.open("https://github.com/BradJKim/8-Queens-Assignment"))

    r.mainloop()

def start_game():
    found = False
    while(not found):
        found = game.next_gen()

def reset_game():
    game.reset_game()


if __name__=="__main__":
    main()