## Dijkstra's Single Source Algorithm

Dijkstra's algorithm is an iterative algorithm that can be used to find both the shortest path spanning tree (SPST) from a given starting node to all other nodes in the graph or the direct shortest path (SP) from a given starting node to a given end node.

The algorithm iteratively steps through a graph, beginning at a defined start point (the root). The algorithm first visits the lowest priority child node from the starting node. If the node has not already been visited, each successive neighbour of the node is visited and analysed. First, a connectivity check is made and then the neighbours current SP is compared with the SP from this node. If this node indeed has a shorter path, the distance to the neighbouring node is updated to the new SP and the node is added as the parent of the neighbour. This process continues until the target node has been visited and processed. The final step of the algorithm is to step back through the parent list from the target node until the source node is found. This path is the SP.

A key requirement for this algorithm is for all edge weights must be non-negative. If non negative edges weights are present, the algorithm may encounter negative cycles and this would this would result in the SP problem having no solution. 

## Bidirectional Dijkstra's Algorithm

The bidirectional Dijkstra algorithm utilises bidirectional search. This method uses the same basics steps of Dijkstra's algorithm, however, it alternates the search steps between the forwards direction (from the defined source) to the backward direction (defined target node). 

The algorithm terminates once the same node has been visited twice, i.e. when the forward search and backward search meet. However, this node may not necessarily be on the SP. As a result, one extra step is needed to find the true shortest path. To do this, node x needs to be found which has the minimum value of df(x) + db(x), i.e. The forward SP to node x and the backward SP to node x. 


