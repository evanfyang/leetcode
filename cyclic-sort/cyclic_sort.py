def cyclic_sort(nums):
    for index in range(len(nums)):
        while nums[index] - 1 != index:
            temp = nums[nums[index] - 1]
            nums[nums[index] - 1] = nums[index]
            nums[index] = temp
    return nums

def main():
  print(str(cyclic_sort([3, 1, 5, 4, 2])))
  print(str(cyclic_sort([2, 6, 4, 3, 1, 5])))
  print(str(cyclic_sort([1, 5, 6, 4, 3, 2])))

main()
