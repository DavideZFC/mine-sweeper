import numpy as np
import matplotlib.pyplot as plt

class MineSweeper:
    def __init__(self, m=10, n=10, mines=30):
        self.m = m
        self.n = n
        self.mines = mines

        # this veriable contains index of the mines
        self.mines_indexes = np.sort(np.random.choice(n*m, mines, replace=False))

        # this variable contains -1 if a given tile is a mine, the number of neighbouring mines otherwise otherwise
        self.hidden_table = np.zeros((m,n))
        self.insert_mines()

        # this variables containes what can be seen by the agent, with all unkwown tiles treated as -1
        self.known_table = -np.ones((m,n))
    
    def insert_mines(self):
        for i in range(self.mines):
            x = self.mines_indexes[i]//self.m
            y = self.mines_indexes[i] - self.m*x
            self.hidden_table[int(x), int(y)] = -1

        for i in range(self.m):
            for j in range(self.n):
                if self.hidden_table[i,j] == 0:
                    pairs = self.get_neig_pairs(i,j)
                    for p in pairs:
                        if self.hidden_table[p] == -1:
                            self.hidden_table[i,j] += 1

    def get_neig_pairs(self, x, y):
        pairs = []
        for i in [x-1,x,x+1]:
            for j in [y-1,y,y+1]:
                if i<0 or i>self.m-1 or j<0 or j>self.n-1:
                    pass
                else:
                    pairs.append((i,j))
        return pairs


    def pick_index(self, x, y):
        if x<0 or x>self.m-1 or y<0 or y>self.n-1:
            return False
        
        if self.hidden_table[int(x), int(y)] == -1:
            print('you lose')
            return True
        else:
            c = self.hidden_table[int(x), int(y)]
            self.known_table[int(x), int(y)] = c
            if c == 0:
                pairs = self.get_neig_pairs(x, y)
                for p in pairs:
                    if self.known_table[p] == -1:
                        self.pick_index(p[0], p[1])
            return False
        
    def step(self, x, y):
        done = self.pick_index(x, y)
        if np.sum(self.hidden_table) == np.sum(self.known_table):
            print('you won!')
            done = True
        return np.copy(self.known_table), done
        
    def render(self):
        plt.imshow(self.known_table)
        plt.colorbar()
        plt.show()

