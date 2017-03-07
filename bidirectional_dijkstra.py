import networkx as nx
import math
from time import time
from collections import deque
from priority_queue import PriorityQueue


def bi_dijkstra_PQ(G, start, target):
    # All the same data structures are used, except now there are structures for both the
    # forward and backward directions
    P_f = {start}
    P_b = {target}
    S_f = PriorityQueue()
    S_b = PriorityQueue()
    D_f = {}
    D_b = {}
    p_f = {}
    p_b = {}

    # Forward Initialisation
    for n in G.nodes():
        if n == start:
            D_f[n] = 0
        else:
            if G.has_edge(start, n):
                D_f[n] = G[start][n]["weight"]
            else:
                D_f[n] = math.inf

            p_f[n] = start
            S_f.add_task(n, D_f[n])

    # Backward Initialisation
    for n in G.nodes():
        if n == target:
            D_b[n] = 0
        else:
            if G.has_edge(target, n):
                D_b[n] = G[target][n]["weight"]
            else:
                D_b[n] = math.inf

            p_b[n] = target
            S_b.add_task(n, D_b[n])

    alg_continue = True
    while alg_continue != False:
        # Forward
        # pop_task() removes and returns the lowest priority task
        u, Du = S_f.pop_task()
        if u in P_f: continue

        P_f.add(u)

        for v, Dv in S_f:
            if v in P_f: continue
            if G.has_edge(u, v):
                if D_f[v] > D_f[u] + G[u][v]["weight"]:
                    D_f[v] = D_f[u] + G[u][v]["weight"]
                    p_f[v] = u
                    S_f.add_task(v, D_f[v])

        if u in P_b:
            alg_continue = False
            w = u
            continue
        else:
            pass

        # Backward
        # pop_task() removes and returns the lowest priority task
        u, Du = S_b.pop_task()
        if u in P_b: continue

        P_b.add(u)

        for v, Dv in S_b:
            if v in P_b: continue
            if G.has_edge(u, v):
                if D_b[v] > D_b[u] + G[u][v]["weight"]:
                    D_b[v] = D_b[u] + G[u][v]["weight"]
                    p_b[v] = u
                    S_b.add_task(v, D_b[v])

        if u in P_f:
            alg_continue = False
            w = u
            continue
        else:
            pass

    # The SP at the visited node is calculated
    min_dist = D_f[w] + D_b[w]

    # All nodes are now visited in both the forward and backward direction
    # The distance to these numbers in both directions are added and compared with the minimum
    # distance to the stopping node. If the new distance is smaller, the node is on the SP
    SP_node = w
    for i in G.nodes():
        if D_f[i] + D_b[i] < min_dist:
            min_dist = D_f[i] + D_b[i]
            SP_node = i
            SP = deque()
        else:
            SP = deque([SP_node])

    # The shortest path is created by going through all parent nodes from the min distance connection
    # node in both the forward and backward direction
    next = SP_node
    while next != start:
        for i, k in p_f.items():
            if i == next:
                SP.appendleft(k)
                next = k

    next = SP_node
    while next != target:
        for i, k in p_b.items():
            if i == next:
                SP.append(k)
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

    print("\n == Bidirectional Dijkstra PQ ===")
    start2 = time()
    print("Shortest Path:", bi_dijkstra_PQ(G, "A", "E"))
    end2 = time()
    print("Runtime: {0:6.8f}".format(end2 - start2))

if __name__ == '__main__':
    main()