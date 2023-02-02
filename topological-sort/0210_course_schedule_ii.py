from collections import deque

def course_schedule(num_courses, prerequisites):
    sorted_order = list()
    
    if num_courses <= 0:
        return sorted_order
    
    in_degree = {i: 0 for i in range(num_courses)}
    graph = {i: list() for i in range(num_courses)}

    for prerequisite in prerequisites:
        parent, child = prerequisite[1], prerequisite[0]
        graph[parent].append(child)
        in_degree[child] += 1
    
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
    

    if len(sorted_order) != num_courses:
        return list()
    
    return sorted_order

def main():
    num_courses = 3
    prerequisites = [[0,1],[1,2]]
    print("Input: num_courses = " + str(num_courses) + ", prerequisites = " + str(prerequisites))
    print("Output: " + str(course_schedule(num_courses, prerequisites)))
    print()

    num_courses = 3
    prerequisites = [[0,1],[1,2],[2,0]]
    print("Input: num_courses = " + str(num_courses) + ", prerequisites = " + str(prerequisites))
    print("Output: " + str(course_schedule(num_courses, prerequisites)))
    print()

    num_courses = 6
    prerequisites = [[2,5],[0,5],[0,4],[1,4],[3,2],[1,3]]
    print("Input: num_courses = " + str(num_courses) + ", prerequisites = " + str(prerequisites))
    print("Output: " + str(course_schedule(num_courses, prerequisites)))
    print()

    num_courses = 2
    prerequisites = [[1,0]]
    print("Input: num_courses = " + str(num_courses) + ", prerequisites = " + str(prerequisites))
    print("Output: " + str(course_schedule(num_courses, prerequisites)))
    print()

    num_courses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    print("Input: num_courses = " + str(num_courses) + ", prerequisites = " + str(prerequisites))
    print("Output: " + str(course_schedule(num_courses, prerequisites)))
    print()

main()