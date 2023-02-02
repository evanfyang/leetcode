from collections import deque

def topological_sort(vertices, edges):
    sorted_order = list()
    
    if vertices <= 0:
        return sorted_order
    
    # 1. initialize the graph
    in_degree = {i: 0 for i in range(vertices)} # count of incoming edges
    graph = {i: list() for i in range(vertices)} # adjacency list graph

    # 2. build the graph
    for edge in edges:
        parent, child = edge[0], edge[1]
        graph[parent].append(child) # put the child into it's parent's list
        in_degree[child] += 1 # increment child's inDegree
    
    # 3. find all sources i.e., all vertices with 0 in-degrees
    sources = deque()
    for vertex in in_degree:
        if in_degree[vertex] == 0:
            sources.append(vertex)
    
    while sources:
        vertex = sources.popleft()
        sorted_order.append(vertex)
        for child in graph[vertex]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)
    
    if len(sorted_order) != vertices:
        return list()
    
    return sorted_order

def main():
    vertices = 4
    edges = [[3,2],[3,0],[2,0],[2,1]]
    print("Input: vertices = " + str(vertices) + ", edges = " + str(edges))
    print("Output: " + str(topological_sort(vertices, edges)))
    print()

    vertices = 5
    edges = [[4,2],[4,3],[2,0],[2,1],[3,1]]
    print("Input: vertices = " + str(vertices) + ", edges = " + str(edges))
    print("Output: " + str(topological_sort(vertices, edges)))
    print()

    vertices = 7
    edges = [[6,4],[6,2],[5,3],[5,4],[3,0],[3,1],[3,2],[4,1]]
    print("Input: vertices = " + str(vertices) + ", edges = " + str(edges))
    print("Output: " + str(topological_sort(vertices, edges)))
    print()

main()