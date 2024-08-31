# Tabu Search

### Description

The tabu search works by creating a set of solutions which are taboo, i.e., which cannot be visited for a given period of time by the algorithm, in order to avoid local minima and traverse the search space, finding the global minimum. It is used for finding solutions to Combinatorial Optimization Problems.

### Algorithm

* Initialise the algorithm to a random solution to the problem and calculate it's score
* Generate a set of feasible solutions in the neighborhood of the solution
* Find the best solution in this set
* Add the old solution to the history buffer, dequeuing the earliest if there is no space.
* replace it with the new solution
* Compare it to the current best, and if it performs better, replace the best.
* Repeat this for however many iterations are decided.

### Use in Path Planning

There is limited literature on the use of TS for path planning. However it has been shown that it is capable of adequately handling the Assignment Problem (Find a mapping between facilities and locations such that the transport cost [flow*distance] between facilities is minimized), the Location Routing Problem (Set up a set of Facilities and travel routes around said facilities to minimize the expenditure delivering goods to a set of locations) and for Robot Path planning in Grid Environments. Path planning in the latter is global path planning, not local.

In Robot Path planning, it can be seen that from the comparisons made, it can be seen that A* always converges faster than TS, and that TS will perform better than Genetic Algorithms. In addition, while A* always converges to the best option, TS and GA don't necessarily do so.

Alternately, TS is also used for planning around visitiing multiple goals. In this case, TS determines the order in which the goals are visited, and another algorithm must be used to determine the exact route (Could potentially use TS itself re: On the Adequacy of Tabu Search for Global Robot Path Planning Problem in Grid Environments).



### Sources

* [On the Adequacy of Tabu Search for Global Robot Path Planning Problem in Grid Environments](https://pdf.sciencedirectassets.com/280203/1-s2.0-S1877050914X00074/1-s2.0-S1877050914006668/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLWVhc3QtMSJHMEUCIQDG3iEWepIsvbrudpubEOzO888LRGEU2ZU9xNOR6dHlkwIgV4BHpTyx2Srh2v3a8N3O0h0EOCMGnUcoGnCOEYyeCvwqswUIdBAFGgwwNTkwMDM1NDY4NjUiDGEEs1Mb%2BlvC2Cuw6yqQBS0IBYS3KDZ08oRf3rZpDXxCzaBLL7D9bqksIRDHo425CD%2FHc%2BDT7MaByAxMMHm1iV1dHc29Uo3Gdp4vSpbiJ35zGCruIynrDI%2BAYy2Sm6L4%2BDJCpiEhtQEXlw1PsiatG97VWPNOLqXGIai51mNH7rLZhGZJHBM16y0EJHi2jkPv7BRno1zV%2BYsAYCVzDZ2g5ZfE7pGMmAkkBjcSTTWfFLGnSODNlUaEdg0vo8vpX0gVeK4F5TjsBxSyyHyPk85pD3XGBXL00sYQpwjUqE06ZoEVRScz7U0ZTpUmI%2BkVz70%2F%2FLYa5wzNbUXYxoXONl71y4KqN%2BLSGw8%2FKW8I142xAqtTm2HO7W%2FHZAtKoHbE3FAaKogvvXkCsmqmbThIhOW9QHBFvaC2HqhunknDgWogc6kS2MUsipZwty6nHsCCcXpDf%2BvlcbGEQPfP2%2BBYcHAStArJlzb5nM4ZmFexweLsifQttdAo%2BLeazdkET2vvxZ9VIv6hTWaJwN97CWLzpEuvQfkygoTWK7vI%2BIdREDTYVKe3qkQqs1e9JXal6yib5%2BUZXZXsEh%2BGrYDezj3Rs7pNEJBIDyNNwCk7wbnPgw2c%2BIBqHHgr9HwyrCW%2F9j%2Fk9%2BmKPTBnXMhPTK6QVZt1rN7foZwHOXJs2SJaiBDntbTrs9ETqyo4I%2BzQGqSoSpkSkJMvdZnftqkc3KeNICYb%2FXinQkBavQJW9kd2WwRegCnWM6voIYJ10bOjT6iu%2FIy%2Fi%2FgA7khd4qBuS1qEZ0uR0I4uh6hOH4LfkkzoVzohcO8dYfR0PdswrPxwe9Itlf5%2F97BbGG1bQKe7tqpJg8o0TUHJZl2mrjXOHrvhB87T18JAfZKvrrcET7wkJj77DhyWA1UKMKTjy7YGOrEBpXApUsIael73lRMjMemza6ET0agcUbwj0BaW0d%2B44PFYGvdMhR1BTh7nR%2Bt9S9Y%2Fh70Mtb%2FC4AlTmLbqTgasf1bzyHCRMeQMGviKKY4r7bgWGIa7kls1c9AA8%2BJGDhpuGn6DQfBMEI%2Fz%2B%2BWh03j7qSD7BTTSsMYHkfId0aIzwV4K6PIER4C6hJNmCajBVIc7c8DU7BuWl7x1KFwZ3omW9KXuu4SIAmd81UFKCcxwKe2V&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240831T114527Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQ3PHCVTY25PT2JKW%2F20240831%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=8eaf12918528dfb45cac8573d88f98dc4dee8349079d1a861c6b78011055026e&hash=077a59c263f7ed161e180fc45878edee05a815a4b6f77c536bfe64bc99da9cb1&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=S1877050914006668&tid=spdf-f8be756a-88be-4649-aeda-2b44819c443a&sid=06229df2903ad947521a010008c94fbd2d14gxrqb&type=client&tsoh=d3d3LnNjaWVuY2VkaXJlY3QuY29t&ua=0f005e01020603535601&rr=8bbcc63eeaec9379&cc=in)
* [Baeldung.com](https://www.baeldung.com/cs/tabu-search)
* [A GPU-based Iterated Tabu Search for Solving the Quadratic 3-dimensional Assignment Problem](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=5587019)
* [A Tabu search and Ant colony system Approach for the Capacitated Location-Routing Problem](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=4617346)
* [Optimal Trajectory Planning for Multiple Waypoint Path Planning using Tabu Search](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8796810)

