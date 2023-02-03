import math

class ArrayReader:
    def __init__(self, array):
        self.array = array

    def get(self, index):
        if index >= len(self.array):
            return math.inf
        return self.array[index]

    def __str__(self):
        return str(self.array)

def search_in_sorted_array_of_unknown_size(reader, target):
    start, end = 0, 1
    
    while reader.get(end) < target:
        new_start = end + 1
        end += (end - start + 1) * 2
        start = new_start
    
    return binary_search(reader, start, end, target)

def binary_search(reader, start, end, target):
    while start <= end:
        middle = (start + end) // 2
        
        if target < reader.get(middle):
            end = middle - 1
        elif target > reader.get(middle):
            start = middle + 1
        else: # target == reader.get(middle):
            return middle
    
    return -1

def main():
    reader = ArrayReader([4,6,8,10,12,14,16,18,20,22,24,26,28,30])
    target = 16
    print("Input: reader = " + str(reader) + ", target = " + str(target))
    print("Output: " + str(search_in_sorted_array_of_unknown_size(reader, target)))
    print()

    reader = ArrayReader([4,6,8,10,12,14,16,18,20,22,24,26,28,30])
    target = 11
    print("Input: reader = " + str(reader) + ", target = " + str(target))
    print("Output: " + str(search_in_sorted_array_of_unknown_size(reader, target)))
    print()

    reader = ArrayReader([1,3,8,10,15])
    target = 15
    print("Input: reader = " + str(reader) + ", target = " + str(target))
    print("Output: " + str(search_in_sorted_array_of_unknown_size(reader, target)))
    print()

    reader = ArrayReader([1,3,8,10,15])
    target = 200
    print("Input: reader = " + str(reader) + ", target = " + str(target))
    print("Output: " + str(search_in_sorted_array_of_unknown_size(reader, target)))
    print()

    reader = ArrayReader([-1,0,3,5,9,12])
    target = 9
    print("Input: reader = " + str(reader) + ", target = " + str(target))
    print("Output: " + str(search_in_sorted_array_of_unknown_size(reader, target)))
    print()

    reader = ArrayReader([-1,0,3,5,9,12])
    target = 2
    print("Input: reader = " + str(reader) + ", target = " + str(target))
    print("Output: " + str(search_in_sorted_array_of_unknown_size(reader, target)))
    print()

main()