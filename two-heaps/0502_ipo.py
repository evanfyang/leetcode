from heapq import *

def ipo(capital, profits, num_projects, initial_capital):
    min_capital_heap = list()
    max_profit_heap = list()

    for index in range(len(capital)):
        heappush(min_capital_heap, (capital[index], index))
    
    available_capital = initial_capital

    for _ in range(num_projects):
        while min_capital_heap and min_capital_heap[0][0] <= available_capital:
            project_capital, index = heappop(min_capital_heap)
            heappush(max_profit_heap, (-profits[index], index))
    
        if not max_profit_heap:
            break
        
        available_capital += -heappop(max_profit_heap)[0]

    return available_capital

def main():
    print("Maximum capital: " + str(ipo([0, 1, 2], [1, 2, 3], 2, 1)))
    print("Maximum capital: " + str(ipo([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)))
    print("Maximum capital: " + str(ipo([0, 1, 1], [1, 2, 3], 2, 0)))
    print("Maximum capital: " + str(ipo([0, 1, 2], [1, 2, 3], 3, 0)))

main()