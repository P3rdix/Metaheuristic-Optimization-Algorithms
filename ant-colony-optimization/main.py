import numpy as np
import random
import matplotlib.pyplot as plt
from aco import AntColony



a = AntColony(50)
a.init_matrix("matrix.txt")
t = a.run(20)