def fruits_into_baskets(fruits):
    windowStart = 0, maxNumFruits = 0, numBaskets = 2
    fruit_types = dict()

    for windowEnd in range(len(fruits)):
        if fruits[windowEnd] in fruit_types:
            fruit_types[fruits[windowEnd]] += 1
        else:
            fruit_types[fruits[windowEnd]] = 1
        
        while len(fruit_types) > numBaskets:
            fruit_types[fruits[windowStart]] -= 1
            if fruit_types[fruits[windowStart]] == 0:
                del fruit_types[fruits[windowStart]]
            windowStart += 1
        
        maxNumFruits = max(maxNumFruits, windowEnd + 1 - windowStart)
    
    return maxNumFruits

def main():
    fruits = ['A', 'B', 'C', 'A', 'C']
    print("Input: " + "fruits = " + fruits)    
    print("Output: " + fruits_into_baskets(fruits))
    
    fruits = ['A', 'B', 'C', 'B', 'B', 'C']
    print("Input: " + "fruits = " + fruits)    
    print("Output: " + fruits_into_baskets(fruits))
    
    fruits = [1, 2, 1]
    print("Input: " + "fruits = " + fruits)    
    print("Output: " + fruits_into_baskets(fruits))
    
    fruits = [0, 1, 2, 2]
    print("Input: " + "fruits = " + fruits)    
    print("Output: " + fruits_into_baskets(fruits))
    
    fruits = [1, 2, 3, 2, 2]
    print("Input: " + "fruits = " + fruits)    
    print("Output: " + fruits_into_baskets(fruits))

main()
