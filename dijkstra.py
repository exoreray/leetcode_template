import heapq

def dijkstra(graph, start_node):
    node_amount = len(graph)
    dist_from_start_node_to = [float('inf')] * node_amount
    dist_from_start_node_to[start_node] = 0
    q = [(0, start_node)]
    while q:
        dist_from_start_to_currnode, currnode = heapq.heappop(q)
        if dist_from_start_node_to[currnode] < dist_from_start_to_currnode:
            continue
        for neighbor, dist_from_start_to_currnode in graph[currnode]: # iterate all edge going out from currnode
            if (dist_to_neighbor_from_start_passing_currnode := dist_from_start_node_to[currnode] + dist_from_start_to_currnode) < dist_from_start_node_to[neighbor]:
                dist_from_start_node_to[neighbor] = dist_to_neighbor_from_start_passing_currnode
                heapq.heappush(q, (dist_to_neighbor_from_start_passing_currnode, neighbor))

    print(dist_from_start_node_to)
    return dist_from_start_node_to



'''
Dijkstra:
 可以找出一个点到所有其他点的最短路径（前提所有路径权重 > 0)

 图用的邻接表形式。

 每个node都是用index代表的 A, B, C, D, E = 0, 1, 2, 3, 4

 方向： nodeX = row X: adj nodes = (node, distance) 
'''

graph = [[(1,4), (2,2)],
         [(2,3), (3,2), (4,3)],
         [(1,1), (3,4), (4,5)],
         [],
         [(3,1)]]

dijkstra(graph, 0)
dijkstra(graph, 1)
dijkstra(graph, 2)
dijkstra(graph, 3)
dijkstra(graph, 4)

'''

      B ----2--->D
   ^ ^ |\      ^ ^
 4/  | |  \  4/  |
 /   | |   \ /   |
A   1| |3   X   1|
 \   | |   / \   |
 2\  | |  /  3\  |
   v | v /     v |
      C ----5--->E

(q) =list of dis from A to:
                            A: 0
                            B: 3
                            C: 2
                            D: 5
                            E: 6

unvisited Nodes: {A,B,C,D,E}

'''

# def dijkstra(n, e): 
#     from heapq import heappush, heappop
#     q = [[0, 0]]
#     dist = [10 ** 8] * n 
#     while q:
#         d, u = heappop(q)
#         if dist[u] != 10 ** 8: continue 
#         dist[u] = d 
#         for dv, v in e[u]:
#             if dist[v] == 10 ** 8:
#                 heappush(q, [d + dv, v])
#     return dist 
