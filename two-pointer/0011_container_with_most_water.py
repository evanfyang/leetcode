def container_with_most_water(heights):
    max_area = 0
    left, right = 0, len(heights) - 1

    while left <= right:
        area = (right - left) * min(heights[left], heights[right])
        max_area = max(max_area, area)
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    
    return max_area

def main():
    heights = [1,8,6,2,5,4,8,3,7]
    print("Input: heights = " + str(heights))
    print("Output: " + str(container_with_most_water(heights))) 
    print() 

    heights = [1,1]
    print("Input: heights = " + str(heights))
    print("Output: " + str(container_with_most_water(heights))) 
    print() 

main()