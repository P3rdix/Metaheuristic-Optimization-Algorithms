import matplotlib.pyplot as plt
import random
import numpy as np

from functools import lru_cache

A = np.random.default_rng(42).random((10,10))

A = (A*10)//1

A = A.astype(np.int8)

class Tabu:

    def __init__(self, matrix):
        
        # initializing global variables

        self.m = np.asarray(matrix)
        self.m_size = [len(matrix),len(matrix[0])]
        self.soln_set = []
        self.all_solns = []
    
# function to calculate the entire solution space for the given problem.

    def calculate_solns(self):
        @lru_cache
        def arr(layer: int, position: int):
            if layer == len(self.m)-1:
                return np.asarray([self.m[layer, position]])
            
            x = arr( layer+1, max(0, position-1))
            y = arr( layer+1,  position)
            z = arr( layer+1, min(len(self.m[0])-1, position+1))
            f = np.concatenate((x,y,z))
            f = f + self.m[layer, position]
            return f
        
        output = np.concatenate([arr(0,i) for i in range(len(self.m))])
        self.all_solns = output

# function calculating the score of a solution. Currently : sum(matrix[path]) To be MINIMIZED

    def calc_score(self, path):
        t = 0
        for i,j in enumerate(path):
            t += self.m[i,j]
        return t
    
# the function that executes tabu.

    def execute(self, loops: int, history_size: int, neighbourhood=1):

        # generate initial solution and calculate it's score
        
        soln = [random.randrange(len(self.m[0]))]
        for _ in range(len(self.m)-1):
            x = random.randrange(3)-1
            soln.append( max(0, min(len(self.m[0])-1, soln[-1]+ x)))
        
        score = self.calc_score(soln)

        # initialize the best solution and score

        best_soln = soln
        best_score = score

        # initialise the history buffer.

        history = []

        # begin the loop
        print("soln = ", soln, score)
        for _ in range(loops):

            # find the new solution set and calculate their scores.

            solns = self.find_soln_space(history, soln, search_space=neighbourhood)
            if len(solns)==0: break
            scores = [self.calc_score(i) for i in solns]
            
            # select the highest scoring solution and make it the new solution
            
            t = [i for i,x in enumerate(scores) if x == min(scores)]
            index = random.choice(t)
            new_score = scores[index]
            new_soln = solns[index]

            # check the best score and if improved upon, replace it

            if new_score < best_score: 
                best_score = new_score
                best_soln = new_soln

            # enqueue the new solution to the history buffer and pop the earliest value if the buffer is full

            history.append(soln)
            if len(history) > history_size:
                history.pop(0)
            

            # replace the old solution

            soln = new_soln
            score = new_score
            print("soln = ", soln, score)
            
        # return the best solution

        return best_soln

# given a solution, the taboo solutions, the matrix and the maximum neighborhood (currently 1) that can be used, calculate the solution space.

    def find_soln_space(self, history, soln, search_space = 1):

        def generate_solns(soln_space, history, search_space):
            if search_space<=0:
                return [i for i in soln_space if i not in history]
            
            new_soln_space = []

            # looping over the old solution space

            for i in soln_space:
                
                # creating a new sln space which has a neighborhood of 1 with the old space

                for j in range(len(i)):
                    if i[j] == 0:
                        new_soln_space.append([t+1 if u==j else t for u,t in enumerate(i)])
                    elif i[j] == self.m_size[1]-1:
                        new_soln_space.append([t-1 if u==j else t for u,t in enumerate(i)])
                    else:
                        if j==0:
                            if i[j]==i[j+1]:
                                new_soln_space.append([t+1 if u==j else t for u,t in enumerate(i)])
                                new_soln_space.append([t-1 if u==j else t for u,t in enumerate(i)]) 
                            else:
                                new_soln_space.append([i[u+1]  if u==j else t for u,t in enumerate(i)])
                        elif j == self.m_size[0]-1:
                            if i[j]==i[j-1]:
                                new_soln_space.append([t+1 if u==j else t for u,t in enumerate(i)])
                                new_soln_space.append([t-1 if u==j else t for u,t in enumerate(i)])
                            else:
                                new_soln_space.append([i[u-1]  if u==j else t for u,t in enumerate(i)])
                        else:
                            if i[j]==i[j-1] and i[j]==i[j+1]:
                                new_soln_space.append([t+1 if u==j else t for u,t in enumerate(i)])
                                new_soln_space.append([t-1 if u==j else t for u,t in enumerate(i)])
                            elif (i[j]==i[j-1] and i[j]!=i[j+1]) or (i[j]!=i[j-1] and i[j]!=i[j+1] and i[j-1]==i[j+1]):
                                new_soln_space.append([i[u+1]  if u==j else t for u,t in enumerate(i)])
                            elif i[j]==i[j+1] and i[j]!=i[j-1]:
                                new_soln_space.append([i[u-1]  if u==j else t for u,t in enumerate(i)])

            return generate_solns(new_soln_space, history, search_space-1)
            
        return generate_solns([soln], history, search_space=search_space)
   
# function to graph all solutions. If executed after Tabu.execute, will also graph the solutions reached for comparison

    def graph_all_solns(self):
        plt.plot(self.all_solns)
        plt.show()






if __name__=="__main__":

    print(A)

    x = Tabu(A)
    print("best soln = ", x.execute(10,5))
    # x.calculate_solns()
    # x.graph_all_solns()











"""conditions:

i == j => i+1, i-1
else => i + i-j









"""


















# # conditions:
# position_greater_than = i[j] == i[j+1] if j!=self.m_size[0]-1 else False
# position_lesser_than = i[j] == i[j-1] if j!=0 else False

# print(i,j)
# print(position_greater_than, position_lesser_than)


# if j==0:
#     if position_greater_than and position_lesser_than:




# if j==0:
#     if i[j]==i[j+1] and (i[j] != 0 or i[j] != self.m_size[1]):
#         new_soln_space.append([t+1 if u==j else t for u,t in enumerate(i)])