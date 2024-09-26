import random

# Index = Row, Value = Column
class Individual(object):
    def __init__(self, board = None):
        if(board):
            self.board = board 
        else:
            self.board = self.create_board()

        self.fitness = self.cal_fitness()

    def mutate_col(self):
        return int(random.random() * 8)
    
    def create_board(self):
        gnome_len = 8
        return [self.mutate_col() for i in range(gnome_len)]
    
    def mate(self, par2):
        new_board = []
        for row in range(8):
            prob = random.random()

            if prob < 0.45:
                new_board.append(self.board[row])
            elif prob < 0.9:
                new_board.append(par2.board[row])
            else:
                new_board.append(self.mutate_col())
        
        return Individual(new_board)
    
    def cal_fitness(self):
        board = self.board
        fitness = 0

        # check for same columns or diagonals using slope between points
        for row1 in range(8):
            for row2 in range(row1+1, 8):
                col1 = board[row1]
                col2 = board[row2]
                if(col1 == col2):
                    fitness += 1
                elif( abs((row2 - row1) / (col2 - col1)) == 1 ): 
                    fitness += 1

        return fitness