# Pandemaniac

## Overview
In this project, we studied the spread of epidemics and the effects of “cascading”. Given an uncolored
graph, teams were allowed a certain number of colored seed nodes to place on the graph. The adjacent
nodes would then be influenced by these seeds and change their color to match that of the majority color,
as specified by the rules. If there was no majority, the nodes would remain at its original color. This
continued until either one team successfully spread their color all throughout the graph, or until there is no
convergence possible and the designated number of iterations is reached. The objective of our team was
then to explore the different possible methods of picking seed nodes that will spread our color the fastest
throughout the graph. We also applied game theory to avoid being overpowered by other colors and ensure
maximum chance of success.

## Approach
1. Our team decided to first secure the Early Bird points by focusing on submitting random nodes in the
proper format. We parsed command line arguments to find the filename and desired number of
seeds in the graph. We then utilized python’s json package and networkx to load and generate the
graph. From the graph, we randomly picked a number of seed nodes equal to the desired number of
seeds, and printed these nodes 50 times in a file. This allowed us to successfully upload our
submissions and secure the early bird points.

2. Our next step was to research different methods of choosing the most important nodes. We looked
at different methods of measuring centrality, and explored different graph/network algorithms that
would pick a subset of the full list of nodes.

3. We first implemented the degree centrality strategy, picking the nodes with highest degree. While
this strategy clearly gave us a score of zero against TA_degree, this strategy was a marked
improvement over the random strategy.

4. Next, we used networkx's graph functions to implement the closeness, betweenness, eigenvector,
and katz centrality strategies. We also looked into finding the dominating set of the graphs, a subset
of vertices such that all nodes not in the subset is adjacent to at least one node in the subset. The
dominating subsets for the graphs we tested on were all larger than the number of allowed seed
nodes, so we implemented this strategy by randomly selecting nodes from the dominating subset to
be seed nodes. We tested all of the above strategies on graphs that we downloaded from the first
few days of the regular season and found that some of the strategies worked much better than
others. Notably, the closeness and eigenvector centrality strategies performed the best. In the end,
we decided to use a mixed strategy: half of our submitted rounds used the eigenvector centrality
strategy and half used the closeness strategy. Together, these strategies were able to beat
TA_fewer and TA_degree.

5. Following the success of our half-closeness and half-eigenvector strategy, we closely analyzed our
performance on all 50 rounds of each graph to assess the performance of each strategy. From our
assessment, we determined that the closeness strategy acquired a majority of nodes consistently
and more frequently than the eigenvector strategy. As a result, we changed our strategy to use
closeness for all 50 rounds of the graph. This change allowed us to win a majority of rounds against
TA_more when testing locally. However, it was unable to defeat TA_more in round 5.

6. In the end, we realized that the success of each strategy in beating the TA differs with the graph. In
some graphs, closeness centrality performs better than all other strategies when we simulate the
cascading effect locally. However, in other graphs, neighbor of highest nodes and highest nodes
beats closeness and other centrality measures in defeating the TA. As a result, we ran multiple
simulations and choose the strategy that performs consistently across all graphs. Our final
submission uses the closeness centrality measure.

## Conclusion

### Results
In the end, we are able to defeat TA_fewer and TA_degree using the mixed strategy of closeness centrality
measure and eigenvector centrality. From examining the result of round three, we determined that
closeness centrality outperforms eigenvector centrality. Therefore, we decided to use closeness centrality
as the final algorithm. This algorithm was able to claim a majority in most of the 50 rounds against TA_more
in the final round.

### Challenges
Some of the centrality strategies that we implemented had a much longer runtime compared to the other
strategies. For example, we need to find all shortest paths in a graph to find the closeness centrality, which
takes time if we use Floyd-Warshall. On the other hand, strategies like degree centrality O(V 3) only take
O(V ) time to find. We initially did not use the closeness centrality strategy on larger graphs because we
were worried that the algorithm may not terminate in the time limit. However, after using networkx's
functions and additional testing, we made sure that we could run the algorithm within the given time.

### Concluding Remarks
In the end, our team decided to using a pure strategy of closeness centrality. By using a pure strategy, we
are risking the possibility of selecting the same nodes as other team (if they also use closeness centrality).
Our team decided to take the risk since closeness centrality algorithm outperforms other algorithms
implemented frequently. We also noted that some centrality measure such as eigenvector centrality,
closeness centrality, and katz centrality selects nodes that are largely the same.
