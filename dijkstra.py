import networkx as nx
import math
from time import time
from collections import deque
from priority_queue import PriorityQueue


def dijkstra_PQ(G, start, target):
    P = {start} # Visited Nodes
    S = PriorityQueue() # Nodes to visit
    D = {} # Current SP to each node
    p = {} # Current best parent for each node

    # Initialise D, p and S
    for n in G.nodes():
        if n == start:
            D[n] = 0
        else:
            if G.has_edge(start, n):
                D[n] = G[start][n]["weight"]
            else:
                D[n] = math.inf

            p[n] = start
            # S is updated with each node and the current SP to each node. The SP value is also
            # called the priority of that node
            S.add_task(n, D[n])

    # Begin Dijkstra search - The algorithm continues visiting nodes until the target node is
    # visited and processed
    alg_continue = True
    while alg_continue != False:
        # pop_task() removes and returns the lowest priority task
        u, Du = S.pop_task()
        if u in P: continue

        # Node is added to the list of seen nodes P
        P.add(u)

        # All neighbours of u, not already visited are now processed
        for v, Dv in S:
            if v in P: continue
            if G.has_edge(u, v):
                if D[v] > D[u] + G[u][v]["weight"]:
                    D[v] = D[u] + G[u][v]["weight"]
                    p[v] = u
                    S.add_task(v, D[v])

        # Stopping Criteria - If the target node has been added to P (i.e. processed)
        # then the algorithm stopping criteria is updated and the while loop terminates
        if target in P:
            alg_continue = False
        else:
            continue

    # Create Shortest Path
    next = target
    SP = deque([target])
    while next != start:
        for i, k in p.items():
            if i == next:
                SP.appendleft(k)
                next = k

    return list(SP)


def main():
    ### Graph 1 ###
    G = nx.Graph()
    E = (
        ("A", "B", 2),
        ("A", "C", 6),
        ("A", "D", 8),

        ("B", "G", 10),
        ("B", "C", 8),

        ("C", "D", 1),
        ("C", "E", 5),
        ("C", "G", 9),
        ("C", "F", 3),

        ("D", "F", 9),
        ("G", "E", 4),
        ("E", "F", 1)
    )
    G.add_weighted_edges_from(E)


    print(" === NetworkX Shortest Path === ")
    start1 = time()
    print("Shortest Path:", nx.dijkstra_path(G, "A", "E"))
    end1 = time()
    print("Runtime: {0:6.8f}".format(end1 - start1))

    print("\n == Dijkstra PQ ===")
    start2 = time()
    print("Shortest Path:", dijkstra_PQ(G, "A", "E"))
    end2 = time()
    print("Runtime: {0:6.8f}".format(end2 - start2))


if __name__ == '__main__':
    main()
