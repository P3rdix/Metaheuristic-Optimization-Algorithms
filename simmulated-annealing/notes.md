# Simulated Annealing

### Description

Annealing is the process of heating and then cooling metals repeatedly to increase the sturdiness of the metal. Simulated annealing functions on this concept.

At hotter temperatures, similar to metal molecules, the solution of the SA problem is allowed a higher degree of freedom, moving with less regard to the minima, in order to facilitate exploration. As the temperature decreases, the probability with which the solution becomes less optimal decreases, allowing the process to converge.

### Algorithm

* Select a search space and initialise a solution randomly.
* Calculate it's performance with respect to the objective function (E).
* Then repeat the following until the temperature cools or the change in energy decreases below your chosen threshold:
  * Find a random point in the vicinity of the current soln and calculate it's value in the objective function (En)
  * if there is an improvement, i.e. (dE := E-En && dE>0), accept the new solution
  * Otherwise, calculate the Boltzmann probability P(dE) = exp(dE/kT) where k is an arbitrary constant and T is the temperature.
  * Generate a random number [0,1) and if it's lower than P(dE), accept the solution
  * Decrease the Temperature if you accept the solution



### Uses in Path Planning

In path planning, Simmulated Annealing is used for the purpose of solving the TSP, or the allocation of jobs over multiple entities. TSP is solved by taking a single path as a solution and having the algorithm switch cities to generate alternates. In the case of multiple entities, each entity is assumed to have a set of jobs to complete. If a given entity has a job in it's vicinity, which it is closer to than the jobs original owner, the job may be allowed to change hands after giving it a penalty. The overall sum of ependiture, including the penalties is used as the objective function in this case.

![](/home/vedant/Documents/Projects/Metaheuristic-Optimization-Algorithms/resources/Simulated-Annealing-in-Path-Planning.png)

For two entities with paths P1 and P2, and m1 and m2 being the number of mismatches in both vehicles paths, the objective function of the system is given by:
$$
E = \sum_{i=1}^{n}(m_i\lambda + 1) * \sum_{j=1}^{len(P_i)-1}dist(x_i,x_{i+1})
$$


### Sources

* [A Modified Simulated Annealing Algorithm for SUAVs Path Planning](https://www.sciencedirect.com/science/article/pii/S2405896315009763?ref=pdf_download&fr=RR-2&rr=8ba9a3302a479374)
* [Baeldung.com](https://www.baeldung.com/cs/simulated-annealing)
* [machinelearningplus](https://www.machinelearningplus.com/machine-learning/simulated-annealing-algorithm-explained-from-scratch-python/)
* 



