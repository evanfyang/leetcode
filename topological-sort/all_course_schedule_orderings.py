from collections import deque

def all_course_schedule_orderings(num_courses, prerequisites):
    sorted_order = list()
    all_course_schedule_orderings = list()
    
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
    
    generate_all_course_schedule_orderings(graph, in_degree, sources, sorted_order, all_course_schedule_orderings)
    return all_course_schedule_orderings

def generate_all_course_schedule_orderings(graph, in_degree, sources, sorted_order, all_course_schedule_orderings):
    if sources:
        for vertex in sources:
            sorted_order.append(vertex)
            sources_for_next_call = deque(sources)  # make a copy of sources
            # only remove the current source, all other sources should remain in the queue for
            # the next call
            sources_for_next_call.remove(vertex)
            # get the node's children to decrement their in-degrees
            for child in graph[vertex]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    sources_for_next_call.append(child)

            # recursive call to print other orderings from the remaining (and new) sources
            generate_all_course_schedule_orderings(graph, in_degree, sources_for_next_call, sorted_order, all_course_schedule_orderings)

            # backtrack, remove the vertex from the sorted order and put all of its children 
            # back to consider the next source instead of the current vertex
            sorted_order.remove(vertex)
            for child in graph[vertex]:
                in_degree[child] += 1

    # if sorted_order doesn't contain all tasks, either we've a cyclic dependency between 
    # tasks, or we have not processed all the tasks in this recursive call
    if len(sorted_order) == len(in_degree):
        all_course_schedule_orderings.append(list(sorted_order))
    
def main():
    num_courses = 3
    prerequisites = [[0,1],[1,2]]
    print("Input: num_courses = " + str(num_courses) + ", prerequisites = " + str(prerequisites))
    print("Output: " + str(all_course_schedule_orderings(num_courses, prerequisites)))
    print()

    num_courses = 4
    prerequisites = [[3,2],[3,0],[2,0],[2,1]]
    print("Input: num_courses = " + str(num_courses) + ", prerequisites = " + str(prerequisites))
    print("Output: " + str(all_course_schedule_orderings(num_courses, prerequisites)))
    print()

    num_courses = 6
    prerequisites = [[2,5],[0,5],[0,4],[1,4],[3,2],[1,3]]
    print("Input: num_courses = " + str(num_courses) + ", prerequisites = " + str(prerequisites))
    print("Output: " + str(all_course_schedule_orderings(num_courses, prerequisites)))
    print()

main()