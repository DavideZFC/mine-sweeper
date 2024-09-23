import numpy as np
import matplotlib.pyplot as plt

class Agent:
    def __init__(self, m, n, mines=30):
        self.m = m
        self.n = n
        self.mines = mines
        self.known_table = -np.ones((m,n))

    def update(self, matrix):
        '''
            input matrix should have the number of neighouring mines for every known tile, and -1 for the unknown ones
        '''
        self.known_table = matrix

    def get_boundary(self):
        '''
            find indexes of tiles which are on the boundary, which means have a known tile near them
        '''
        self.boundary_matrix = np.zeros_like(self.known_table)
        boundary_list = []

        for x in range(self.m):
            for y in range(self.n):
                if self.known_table[x,y] == -1:
                    neig = self.get_neig_pairs(x, y)
                    for n in neig:
                        (i,j) = n
                        if self.known_table[i,j] > 0:
                            self.boundary_matrix[x,y] = 1
                            boundary_list.append((x,y))
                            break
        return boundary_list
    
    def verify_candidates(self, cand, boundary_list):
        '''
        takes a sequence cand of zeros and ones, corresponding to the elements one by one of the boundary list, and verify if that sequence is feasible
        '''
        

    def compute_boundary_probas(self):
        boundary_list = self.get_boundary()
        candidate_sequences = []
        for pair in boundary_list:
            new_candidate_sequences = []

            # is it possible that the current tile is a mine?
            for cand in candidate_sequences:
                cand.append(1)
                if self.verify_candidates(cand, boundary_list):
                    new_candidate_sequences.append(cand)
            # is it possible that the current tile is not a mine?
            for cand in candidate_sequences:
                cand.append(0)
                self.verify_candidates(cand)
                if self.verify_candidates(cand):
                    new_candidate_sequences.append(cand, boundary_list)

            candidate_sequences = new_candidate_sequences
        '''
            creates all feasible boundary sequences
        '''
        # super importante mettere vicini nella sequenza tile che sono vicini


    def show_boundary(self):
        self.get_boundary()
        plt.imshow(self.boundary_matrix)
        plt.title('Tiles of the boundary')
        plt.show()
        
    
    def get_neig_pairs(self, x, y):
        pairs = []
        for i in [x-1,x,x+1]:
            for j in [y-1,y,y+1]:
                if i<0 or i>self.m-1 or j<0 or j>self.n-1:
                    pass
                else:
                    pairs.append((i,j))
        return pairs
