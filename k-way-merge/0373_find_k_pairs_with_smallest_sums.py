from heapq import *

def find_k_pairs_with_smallest_sums(nums1, nums2, k):
    max_heap = list()
    for i in range(min(k, len(nums1))):
        for j in range(min(k, len(nums2))):
            if len(max_heap) < k:
                heappush(max_heap, (-(nums1[i] + nums2[j]), i, j))
            else:
                if nums1[i] + nums2[j] > -max_heap[0][0]:
                    break
                else:
                    heappop(max_heap)
                    heappush(max_heap, (-(nums1[i] + nums2[j]), i, j))

    pairs = list()
    for (pair_sum, i, j) in max_heap:
        pairs.append([nums1[i], nums2[j]])
    
    return pairs

def find_k_pairs_with_largest_sums(nums1, nums2, k):
    min_heap = list()
    for i in range(0, min(k, len(nums1))):
        for j in range(min(k, len(nums2))):
            if len(min_heap) < k:
                heappush(min_heap, (nums1[i] + nums2[j], i, j))
            else:
                # if the sum of the two numbers from the two arrays is smaller than the 
                # smallest(top) element of the heap, we can 'break' here. Since the arrays are 
                # sorted in the descending order, we'll not be able to find a pair with a higher 
                # sum moving forward
                if nums1[i] + nums2[j] < min_heap[0][0]:
                    break
                else: # we've a pair with a larger sum, remove top and insert this pair in heap
                    heappop(min_heap)
                    heappush(min_heap, (nums1[i] + nums2[j], i, j))

    result = []
    for (pair_sum, i, j) in min_heap:
        result.append([nums1[i], nums2[j]])

    return result

def main():
    print("find k pairs with largest sums")
    print()
    
    nums1 = [9,8,2]
    nums2 = [6,3,1]
    k = 3
    print("Input: nums1 = " + str(nums1) + ", nums2 = " + str(nums2) + ", k = " + str(k))
    print("Output: " + str((find_k_pairs_with_largest_sums(nums1, nums2, k))))
    print()

    nums1 = [5,2,1]
    nums2 = [2,-1]
    k = 3
    print("Input: nums1 = " + str(nums1) + ", nums2 = " + str(nums2) + ", k = " + str(k))
    print("Output: " + str((find_k_pairs_with_largest_sums(nums1, nums2, k))))
    print()

    nums1 = [11,7,1]
    nums2 = [6,4,2]
    k = 3
    print("Input: nums1 = " + str(nums1) + ", nums2 = " + str(nums2) + ", k = " + str(k))
    print("Output: " + str((find_k_pairs_with_largest_sums(nums1, nums2, k))))
    print()

    nums1 = [2,1,1]
    nums2 = [3,2,1]
    k = 2
    print("Input: nums1 = " + str(nums1) + ", nums2 = " + str(nums2) + ", k = " + str(k))
    print("Output: " + str((find_k_pairs_with_largest_sums(nums1, nums2, k))))
    print()

    nums1 = [2, 1]
    nums2 = [3]
    k = 3
    print("Input: nums1 = " + str(nums1) + ", nums2 = " + str(nums2) + ", k = " + str(k))
    print("Output: " + str((find_k_pairs_with_largest_sums(nums1, nums2, k))))
    print()

    print("find k pairs with smallest sums")
    print()

    nums1 = [2,8,9]
    nums2 = [1,3,6]
    k = 3
    print("Input: nums1 = " + str(nums1) + ", nums2 = " + str(nums2) + ", k = " + str(k))
    print("Output: " + str((find_k_pairs_with_smallest_sums(nums1, nums2, k))))
    print()

    nums1 = [1,2,5]
    nums2 = [-1,2]
    k = 3
    print("Input: nums1 = " + str(nums1) + ", nums2 = " + str(nums2) + ", k = " + str(k))
    print("Output: " + str((find_k_pairs_with_smallest_sums(nums1, nums2, k))))
    print()

    nums1 = [1,7,11]
    nums2 = [2,4,6]
    k = 3
    print("Input: nums1 = " + str(nums1) + ", nums2 = " + str(nums2) + ", k = " + str(k))
    print("Output: " + str((find_k_pairs_with_smallest_sums(nums1, nums2, k))))
    print()

    nums1 = [1,1,2]
    nums2 = [1,2,3]
    k = 2
    print("Input: nums1 = " + str(nums1) + ", nums2 = " + str(nums2) + ", k = " + str(k))
    print("Output: " + str((find_k_pairs_with_smallest_sums(nums1, nums2, k))))
    print()

    nums1 = [1,2]
    nums2 = [3]
    k = 3
    print("Input: nums1 = " + str(nums1) + ", nums2 = " + str(nums2) + ", k = " + str(k))
    print("Output: " + str((find_k_pairs_with_smallest_sums(nums1, nums2, k))))
    print()

main()