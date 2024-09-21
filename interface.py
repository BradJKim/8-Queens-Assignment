import tkinter as tk
import webbrowser
import time
from Game import *  

game = Game()
r = tk.Tk()
queen_image = tk.PhotoImage(file="queen.png")  
queen_labels = []  

status_label = tk.Label(r, text="Current Status: Ready", font=("Arial", 12))

def main():
    r.title('8 Queens Genetic Algorithm')
    r.geometry("500x600")

    create_board(r)
    
    button_frame = tk.Frame(r)
    button_frame.grid(row=8, column=0, columnspan=8)


    reset_button = tk.Button(button_frame, text="Reset", command=reset_game)
    reset_button.pack(side=tk.LEFT, padx=10, pady=10)

    start_button = tk.Button(button_frame, text="Start", command=start_game)
    start_button.pack(side=tk.LEFT, padx=10, pady=10)

    status_label.grid(row=9, column=0, columnspan=8, pady=10)

    link_label = tk.Label(r, text="Click here to visit Github Repo", fg="blue", cursor="hand2")
    link_label.grid(row=10, column=0, columnspan=8, pady=10)
    link_label.bind("<Button-1>", lambda e: webbrowser.open("https://github.com/BradJKim/8-Queens-Assignment"))

    r.mainloop()

def create_board(root):
    for row in range(8):
        for col in range(8):
            color = 'white' if (row + col) % 2 == 0 else 'black'
            label = tk.Label(root, bg=color, width=60//10, height=60//20)
            label.grid(row=row, column=col)

def update_queens(positions):
    for queen_label in queen_labels:
        queen_label.destroy()
    queen_labels.clear()

    for i in range(len(positions)):
        col = positions[i]
        queen_label = tk.Label(r, image=queen_image, bg='black' if (i + col) % 2 != 0 else 'white', width=40, height=40)
        queen_label.grid(row=i, column=col)
        queen_labels.append(queen_label)

def start_game():
    def run_generation():
        if not game.is_found():
            top_individual = game.next_gen()
            update_queens(top_individual.board)
            set_text("Generation: {} Rows: {} Fitness: {}".format(game.generation, game.population[0].board, game.population[0].fitness))
            r.after(10, run_generation)

    run_generation()

def reset_game():
    game.reset_game()
    set_text("Current Status: Ready")
    update_queens([])

def set_text(status):
    status_label.config(text=status)

if __name__ == "__main__":
    main()