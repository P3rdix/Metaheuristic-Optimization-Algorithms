# Ant Colony Optimization

### Description

Ant Colony Optimization works by simulating the movement of ants, where upon settling into a nest, initially, explorer ants are sent in search of food. Following this, worker ants are sent forth along the pheromone trails of the explorers, in order to retrieve the food. As the pheromones wear away as time passes, the ants tend to congregate along the fastest path to from the nest to the food.

Similarly, ACO sends out a set of ants initially, randomly choosing paths from the source, until they reach the destination. For each subsequent iteration, the probability of choosing a path at any given intersection in the road, until all ants in an iteration converge on a single path.

### Algorithm

* Initialize an array of ants. and a pheromone matrix containing the pheromone levels of each path
* Until the path converges, do:
  * Using the pheromone level at each intersection, select an edge to follow.
  * Once all ants have reached the destination, recalculate the pheromone as:
        p' = sum(n * cost of edge/ sum(cost of paths using edge)) + a * p

  * here, a is a constant, and p is the previous pheromone.
  * Repeat

### Uses

ACO is used in Path Planning primarily for Global Path Planning, where it is used for it's quick convergence rates, when compared to other meta-heuristic optimization methods. 