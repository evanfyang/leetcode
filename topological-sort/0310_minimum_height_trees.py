from collections import deque

def minimum_height_trees(vertices, edges):
    if vertices <= 0:
        return []
    
    # with only one node, its in-degrees will be 0; thus, we need to handle it separately
    if vertices == 1:
        return [0]
    
    # 1. initialize the graph
    in_degree = {i: 0 for i in range(vertices)}
    graph = {i: list() for i in range(vertices)}

    # 2. build the graph
    for edge in edges:
        vertex1, vertex2 = edge[0], edge[1]
        # since this is an undirected graph, we add a link for both vertices in the graph
        graph[vertex1].append(vertex2)
        graph[vertex2].append(vertex1)
        # increment the in-degrees of both the vertices
        in_degree[vertex1] += 1
        in_degree[vertex2] += 1
    
    # 3. find all leaves, i.e. all vertices with 1 in-degrees
    leaves = deque()
    for vertex in in_degree:
        if in_degree[vertex] == 1:
            leaves.append(vertex)
    
    # 4. remove leaves level by level and subtract each leaf's children's in-degrees; 
    # repeat this until we are left with 1 or 2 nodes, which will be our answer; any 
    # node that has already been a leaf cannot be the root of a minimum height tree 
    # because its adjacent non-leaf node will always be a better candidate
    total_num_vertices = vertices
    while total_num_vertices > 2:
        num_leaves = len(leaves)
        total_num_vertices -= num_leaves
        for _ in range(num_leaves):
            # decrement the in-degree for a vertex's children
            vertex = leaves.popleft()
            for child in graph[vertex]:
                in_degree[child] -= 1
                if in_degree[child] == 1:
                    leaves.append(child)
    
    return list(leaves)

def main():
    vertices = 5
    edges = [[0,1],[1,2],[1,3],[2,4]]
    print("Input: vertices = " + str(vertices) + ", edges = " + str(edges))
    print("Output: " + str(minimum_height_trees(vertices, edges)))
    print()

    vertices = 4
    edges = [[0,1],[0,2],[2,3]]
    print("Input: vertices = " + str(vertices) + ", edges = " + str(edges))
    print("Output: " + str(minimum_height_trees(vertices, edges)))
    print()

    vertices = 4
    edges = [[0,1],[1,2],[1,3]]
    print("Input: vertices = " + str(vertices) + ", edges = " + str(edges))
    print("Output: " + str(minimum_height_trees(vertices, edges)))
    print()

    vertices = 4
    edges = [[1,0],[1,2],[1,3]]
    print("Input: vertices = " + str(vertices) + ", edges = " + str(edges))
    print("Output: " + str(minimum_height_trees(vertices, edges)))
    print()

    vertices = 6
    edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
    print("Input: vertices = " + str(vertices) + ", edges = " + str(edges))
    print("Output: " + str(minimum_height_trees(vertices, edges)))
    print()

main()