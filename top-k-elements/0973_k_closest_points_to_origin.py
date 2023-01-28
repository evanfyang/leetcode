from math import sqrt
from heapq import *

def k_closest_points_to_origin(points, k):
    x, y = 0, 1
    max_heap = list()
    for i in range(k):
        euclidean_distance = sqrt(points[i][x] ** 2 + points[i][y] ** 2)
        heappush(max_heap, (-euclidean_distance, points[i]))
    
    for i in range(k, len(points)):
        euclidean_distance = sqrt(points[i][x] ** 2 + points[i][y] ** 2)
        if -euclidean_distance > max_heap[0][0]:
            heappop(max_heap)
            heappush(max_heap, (-euclidean_distance, points[i]))
        else:
            continue
    
    return [point[1] for point in max_heap]

def main():
    points = [[1,2],[1,3]]
    k = 1
    print("Input: nums = " + str(points) + ", k = " + str(k))
    print("Output: " + str(k_closest_points_to_origin(points, k)))
    print()

    points = [[1,3],[3,4],[2,-1]]
    k = 2
    print("Input: nums = " + str(points) + ", k = " + str(k))
    print("Output: " + str(k_closest_points_to_origin(points, k)))
    print()

    points = [[1,3],[-2,2]]
    k = 1
    print("Input: nums = " + str(points) + ", k = " + str(k))
    print("Output: " + str(k_closest_points_to_origin(points, k)))
    print()

    points = [[3,3],[5,-1],[-2,4]]
    k = 2
    print("Input: nums = " + str(points) + ", k = " + str(k))
    print("Output: " + str(k_closest_points_to_origin(points, k)))
    print()

main()