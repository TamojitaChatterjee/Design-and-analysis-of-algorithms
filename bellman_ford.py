#bellman-ford algorithm --> dynamic programming
import math

def bellman_ford(graph: list[list[int]], source: int) -> tuple[list[int], bool]:
    '''
    Single source shortest path
    Args:
        graph: a list of lists representing adjacency matrix of graph
            graph[i][j] is weight of edge from i to j
            math.inf --> no edge
        source: index of source vertex
        
    Returns:
        tuple containing:
            - list of shortest path distances from source to each vertext
            - boolean indicating whether a negative cycle has been detected
    '''
    
    #initialize distances from source to all vertices as INF
    n=len(graph) #number of vertices
    dist = [math.inf] * n
    dist[source] = 0 #source vertex
    
    #relaxation for n-1 times
    for _ in range(n-1):
        for u in range(n):
            for v in range(n):
                weight = graph[u][v]
                if weight != math.inf and dist[u] != math.inf and dist[u] + weight<dist[v]:
                    dist[v] = dist[u] + weight
                    
    #check for negative weight cycles
    negative_cycle = False
    for u in range(n):
        for v in range(n):
            weight = graph[u][v]
            if weight != math.inf and dist[u] != math.inf and dist[u]+weight < dist[v]:
                negative_cycle = True
                break
        if negative_cycle:
            break
        
    return dist, negative_cycle