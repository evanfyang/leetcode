# Definition for a Node.
class Node:
    def __init__(self, value = 0, neighbors = None):
        self.value = value
        self.neighbors = neighbors if neighbors is not None else []

def generate_graph_from_adjacency_list(adjacency_list):
    existing_nodes = dict()
    if len(adjacency_list) == 0:
        return None
    for vertex in range(len(adjacency_list)):
        node = Node(vertex + 1)
        if vertex + 1 == 1:
            root = node
        if vertex + 1 not in existing_nodes:
            existing_nodes[vertex + 1] = node
        else: 
            node = existing_nodes[vertex + 1]
        for neighbor in adjacency_list[vertex]:
            neighbor_node = Node(neighbor)
            if neighbor not in existing_nodes:
                existing_nodes[neighbor] = neighbor_node
            else:
                neighbor_node = existing_nodes[neighbor]
            node.neighbors.append(neighbor_node)
    return root

def generate_adjacency_list_from_graph(node, num_nodes):
    if node is None:
        return list()
    
    adjacency_list = [list() for _ in range(num_nodes)]
    visited_nodes = dict()

    def dfs(node):
        if node.value in visited_nodes:
            return
    
        visited_nodes[node.value] = node
        
        for neighbor in node.neighbors:
            adjacency_list[node.value - 1].append(neighbor.value)
            dfs(neighbor)
    
    dfs(node)
    return adjacency_list

def clone_graph(node):
    if node is None:
        return None
    
    old_to_new = dict()
    
    def dfs(node):
        if node in old_to_new:
            return old_to_new[node]
        
        copy = Node(node.value)
        old_to_new[node] = copy

        for neighbor in node.neighbors:
            copy.neighbors.append(dfs(neighbor))
        
        return copy
    
    return dfs(node) if node else None

def main():
    adjacency_list = [[2,4],[1,3],[2,4],[1,3]]
    print("Input: adjacency_list = " + str(adjacency_list))
    node = generate_graph_from_adjacency_list(adjacency_list)
    print("Ouput: " + str(generate_adjacency_list_from_graph(clone_graph(node), len(adjacency_list))))
    print()

    adjacency_list = [[]]
    print("Input: adjacency_list = " + str(adjacency_list))
    node = generate_graph_from_adjacency_list(adjacency_list)
    print("Ouput: " + str(generate_adjacency_list_from_graph(clone_graph(node), len(adjacency_list))))
    print()

    adjacency_list = []
    print("Input: adjacency_list = " + str(adjacency_list))
    node = generate_graph_from_adjacency_list(adjacency_list)
    print("Ouput: " + str(generate_adjacency_list_from_graph(clone_graph(node), len(adjacency_list))))
    print()

main()