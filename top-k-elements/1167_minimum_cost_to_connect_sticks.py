from heapq import *

def minimum_cost_to_connect_sticks(sticks):
    
    min_heap = list()
    for i in range(len(sticks)):
        heappush(min_heap, sticks[i])
    
    total_cost, temp_cost = 0, 0
    while len(min_heap) > 1:
        temp_cost = heappop(min_heap) + heappop(min_heap)
        total_cost += temp_cost
        heappush(min_heap, temp_cost)

    return total_cost

def main():
    sticks = [3,1,5,12,2,11]
    print("Input: nums = " + str(sticks))
    print("Output: " + str(minimum_cost_to_connect_sticks(sticks)))
    print()

    sticks = [3,4,5,6]
    print("Input: nums = " + str(sticks))
    print("Output: " + str(minimum_cost_to_connect_sticks(sticks)))
    print()

    sticks = [1,3,11,5,2]
    print("Input: nums = " + str(sticks))
    print("Output: " + str(minimum_cost_to_connect_sticks(sticks)))
    print()

main()