from heapq import *

class SlidingWindowMedian:
    def __init__(self):
        self.max_heap = list()
        self.min_heap = list()

    def median_sliding_window(self, nums, k):
        medians = [0.0 for _ in range(len(nums) - k + 1)]
        for i in range(len(nums)):
            if not self.max_heap or -self.max_heap[0] >= nums[i]:
                heappush(self.max_heap, -nums[i])
            else:
                heappush(self.min_heap, nums[i])
            
            self.rebalance_heaps()

            if i - k + 1 >= 0:
                if len(self.max_heap) == len(self.min_heap):
                    medians[i - k + 1] = (-self.max_heap[0] + self.min_heap[0]) / 2.0
                else:
                    medians[i - k + 1] = -self.max_heap[0] / 1.0

                element_to_remove_from_window = nums[i - k + 1]

                if element_to_remove_from_window <= -self.max_heap[0]:
                    self.remove_element(self.max_heap, -element_to_remove_from_window)
                else:
                    self.remove_element(self.min_heap, element_to_remove_from_window)

                self.rebalance_heaps()

        return medians 
    
    def remove_element(self, heap, element):
        index = heap.index(element)
        heap[index] = heap[-1]
        del heap[-1]

        if index < len(heap):
            heapq._siftup(heap, index)
            heapq._siftdown(heap, 0, index)

    def rebalance_heaps(self):
        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

def main():

  sliding_window_median = SlidingWindowMedian()
  result = sliding_window_median.find_sliding_window_median([1, 2, -1, 3, 5], 2)
  print("Sliding window medians are: " + str(result))

  sliding_window_median = SlidingWindowMedian()
  result = sliding_window_median.find_sliding_window_median([1, 2, -1, 3, 5], 3)
  print("Sliding window medians are: " + str(result))


main()