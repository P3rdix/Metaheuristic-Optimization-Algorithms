import numpy as np
import re

class AntColony:
    def __init__(self, n: int):
        self.num_ants = n
        self.grid = [[]]
        self.pheromones = np.zeros((0))

    def init_matrix(self,input_file: str):
        with open(input_file, "r") as f:
            tmp = f.readlines()[1:]
            tmp = "".join(tmp).split("\n")
            tmp = [[int(i) for i in j.split()]for j in tmp]
            tmp = [i for i in tmp if len(i)== len(tmp)]
            self.grid = np.pad(np.asarray(tmp), [(1,1),(1,1)], mode='constant', constant_values=-1)

        self.pheromones = np.zeros((self.grid.shape[0]-2, self.grid.shape[1]-2, 9), dtype=np.float64)

        def init_pheromone(array):
            x = []
            if array[1,1]!=0:
                return np.zeros((9))
            for i in range(3):
                for j in range(3):
                    if array[j][i] != 0 or (i == 1 and j == 1):
                        x.append(0)
                    else:
                        x.append(1)

            x = np.asarray(x, dtype=np.float64)
            x /= np.sum(x)
            return x


        for i in range(1,self.grid.shape[0]-1):
            for j in range(1,self.grid.shape[1]-1):
                self.pheromones[i-1,j-1] = self.pheromones[i-1,j-1] + init_pheromone(self.grid[i-1:i+2,j-1:j+2])

        return

    def forward_propogate(self, max_len, goal):

        # initialise vectors tracking the completeness of the ants path (cpl), iterations covered, and the path vector of the ant

        iters = np.zeros((self.num_ants),dtype=np.int16)
        cpl = np.zeros((self.num_ants), dtype=np.int8)
        paths = np.zeros((1,self.num_ants,2), dtype=np.uint8)


        def fetch_neighbor(x: int):
            neighborhood = [(-1,-1),(0,-1),(1,-1),(-1,0),(0,0),(1,0),(-1,1),(0,1),(1,1)]
            if x>=0 and x<9:
                return neighborhood[x]
            return -1

        # loop for the max number of iterations

        for _ in range(max_len):

            # initialize random numbers for each ant and their new step

            n = np.random.rand((self.num_ants))
            new_step = np.zeros((1,self.num_ants, 2), dtype=np.int8)


            # increment the iteration number of the ants that haven't reached the goal yet
            iters += np.absolute(cpl-1)

            # loop for each ant
            for i in range(self.num_ants):


                # if the ant hasn't reached the destination then
                if cpl[i]!=1:


                    # temporary variables
                    t = 0
                    r = self.pheromones[paths[-1,i,0], paths[-1,i,1], t]


                    # find the slot for the point
                    while(r<n[i] and t <9):

                        t +=1
                        r += self.pheromones[paths[-1,i,0], paths[-1,i,1], t]


                    # find the x and y coordinate change
                    coords = fetch_neighbor(t)

                    # update it in the new step vector
                    new_step[0,i,0] += coords[0] + paths[-1,i,0]
                    new_step[0,i,1] += coords[1] + paths[-1,i,1]


                    # check if the new step moves the ant to the goal
                    if new_step[0,i,0] == goal[0] and new_step[0,i,1] == goal[1]:
                        cpl[i] +=1
                else:
                    new_step[0,i,0] += paths[-1,i,0]
                    new_step[0,i,1] += paths[-1,i,1]


            paths = np.append(paths, new_step, axis=0)
            if np.sum(cpl) == self.num_ants:
                break


        for i in range(cpl.size):
            if cpl[i]==0:
                iters[i] = -1

        # pruning and reshaping the matrix
        paths = paths[:np.max(iters)+1]
        ren = np.where(iters!=-1)
        paths = np.asarray([i[ren] for i in paths])
        return (paths, iters[ren])

    def update_pheromones(self, paths, iters, goal_node, alpha = 0.1):
        def convert(y):
            neighborhood = [(-1,-1),(0,-1),(1,-1),(-1,0),(0,0),(1,0),(-1,1),(0,1),(1,1)]
            for i in range(len(neighborhood)):
                if neighborhood[i][0] == y[0] and neighborhood[i][1] == y[1]:
                    return i
            return -1


        for i in range(paths.shape[0]-1):
            for j in range(len(iters)):
                if (paths[i,j,0] != goal_node[0] or paths[i,j,1] != goal_node[1]):
                    f = (paths[i+1,j,0]-paths[i,j,0], paths[i+1,j,1]-paths[i,j,1])
                    m = convert(f)
                    self.pheromones[paths[i,j,0],paths[i,j,1], m] += alpha * (1/iters[j])

        for i in range(paths.shape[0]-1):
            for j in range(len(iters)):
                if (paths[i,j,0] != goal_node[0] or paths[i,j,1] != goal_node[1]):
                    self.pheromones[paths[i,j,0],paths[i,j,1]] = self.pheromones[paths[i,j,0],paths[i,j,1]]/np.sum(self.pheromones[paths[i,j,0],paths[i,j,1]])
        return



    def run(self,n_iter: int):
        for _ in range(20):
            x = self.forward_propogate(n_iter, [4,4])
            self.update_pheromones(x[0],x[1],(4,4),1)
        x = self.forward_propogate(n_iter, [4,4])
        return x
