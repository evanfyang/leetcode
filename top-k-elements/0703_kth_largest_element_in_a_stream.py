from heapq import *

class KthLargestElementInStream:
    def __init__(self, nums, k):
        self.min_heap = list()
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, value: int) -> int:
        if len(self.min_heap) < self.k:
            heappush(self.min_heap, value)
        else:
            if value > self.min_heap[0]:
                heappop(self.min_heap)
                heappush(self.min_heap, value)
        
        return self.min_heap[0]

def main():
    nums = [4,5,8,2]
    k = 3
    kth_largest_element_in_stream = KthLargestElementInStream(nums, k)
    print("Input: nums = " + str(nums) + ", k = " + str(k))
    print("Add 3: " + str(kth_largest_element_in_stream.add(3)))
    print("Add 5: " + str(kth_largest_element_in_stream.add(5)))
    print("Add 10: " + str(kth_largest_element_in_stream.add(10)))
    print("Add 9: " + str(kth_largest_element_in_stream.add(9)))
    print("Add 4: " + str(kth_largest_element_in_stream.add(4)))
    print()

    nums = [3,1,5,12,2,11]
    k = 4
    kth_largest_element_in_stream = KthLargestElementInStream(nums, k)
    print("Input: nums = " + str(nums) + ", k = " + str(k))
    print("Add 6: " + str(kth_largest_element_in_stream.add(6)))
    print("Add 13: " + str(kth_largest_element_in_stream.add(13)))
    print("Add 4: " + str(kth_largest_element_in_stream.add(4)))

main()