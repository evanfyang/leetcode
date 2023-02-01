def knapsack_brute_force(profits, weights, capacity):
    return knapsack_brute_force_recursive(profits, weights, capacity, 0)

def knapsack_brute_force_recursive(profits, weights, capacity, current_index):
    # base case
    if capacity <= 0 or current_index >= len(profits):
        return 0

    # recursive call after choosing the element at the current_index
    # if the weight of the element at current_index exceeds the capacity, we  shouldn't 
    # process this
    profit1 = 0
    if weights[current_index] <= capacity:
        profit1 = profits[current_index] + knapsack_brute_force_recursive(profits, weights, capacity - weights[current_index], current_index + 1)

    # recursive call after excluding the element at the current_index
    profit2 = knapsack_brute_force_recursive(profits, weights, capacity, current_index + 1)

    return max(profit1, profit2)

def knapsack_memoization(profits, weights, capacity):
    # create a two dimensional array for memoization, each element is initialized to '-1'
    dp = [[-1 for x in range(capacity+1)] for y in range(len(profits))]
    return knapsack_memoization_recursive(dp, profits, weights, capacity, 0)

def knapsack_memoization_recursive(dp, profits, weights, capacity, current_index):
    # base case
    if capacity <= 0 or current_index >= len(profits):
        return 0

    # if we have already solved a similar problem, return the result from memory
    if dp[current_index][capacity] != -1:
        return dp[current_index][capacity]

    # recursive call after choosing the element at the current_index
    # if the weight of the element at current_index exceeds the capacity, we
    # shouldn't process this
    profit1 = 0
    if weights[current_index] <= capacity:
        profit1 = profits[current_index] + knapsack_memoization_recursive(dp, profits, weights, capacity - weights[current_index], current_index + 1)

    # recursive call after excluding the element at the current_index
    profit2 = knapsack_memoization_recursive(dp, profits, weights, capacity, current_index + 1)

    # memoization matrix does not store the cumulative result, but rather the current result 
    dp[current_index][capacity] = max(profit1, profit2)
    return dp[current_index][capacity]

def print_selected_weights(dp, weights, profits, capacity):
    print("Output (Selected Weights): ", end="")
    selected_weights = str() 
    n = len(weights)
    totalProfit = dp[n - 1][capacity]
    for i in range(n - 1, 0, -1):
        if totalProfit != dp[i - 1][capacity]:
            selected_weights += str(weights[i]) + ", "
            capacity -= weights[i]
            totalProfit -= profits[i]

    if totalProfit != 0:
        selected_weights += str(weights[0])

    if selected_weights[-2] == ",":
        selected_weights = selected_weights[:-2]
    print(selected_weights)

def knapsack_bottom_up_dynamic_programming(profits, weights, capacity):
    # basic checks
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0

    dp = [[0 for x in range(capacity + 1)] for y in range(n)]

    # populate the capacity = 0 columns, with '0' capacity we have '0' profit
    for i in range(0, n):
        dp[i][0] = 0

    # if we have only one weight, we will take it if it is not more than the capacity
    for c in range(0, capacity + 1):
        if weights[0] <= c:
            dp[0][c] = profits[0]

    # process all sub-arrays for all the capacities
    for i in range(1, n):
        for c in range(1, capacity + 1):
            profit1, profit2 = 0, 0
            # include the item, if it is not more than the capacity
            if weights[i] <= c:
                profit1 = profits[i] + dp[i - 1][c - weights[i]]
            # exclude the item
            profit2 = dp[i - 1][c]
            # take maximum
            dp[i][c] = max(profit1, profit2)

    print_selected_weights(dp, weights, profits, capacity)
    # maximum profit will be at the bottom-right corner.
    return dp[n - 1][capacity]

def main():
    profits = [4,5,3,7]
    weights = [2,3,1,4]
    capacity = 5
    print("Input: profits = " + str(profits) + ", weights = " + str(weights) + ", capacity = " + str(capacity))
    print("Output (Max Profit): " + str(knapsack_bottom_up_dynamic_programming(profits, weights, capacity)))
    print()

    profits = [1,6,10,16]
    weights = [1,2,3,5]
    capacity = 5
    print("Input: profits = " + str(profits) + ", weights = " + str(weights) + ", capacity = " + str(capacity))
    print("Output (Max Profit): " + str(knapsack_bottom_up_dynamic_programming(profits, weights, capacity)))
    print()

    profits = [1,6,10,16]
    weights = [1,2,3,5]
    capacity = 6
    print("Input: profits = " + str(profits) + ", weights = " + str(weights) + ", capacity = " + str(capacity))
    print("Output (Max Profit): " + str(knapsack_bottom_up_dynamic_programming(profits, weights, capacity)))
    print()

    profits = [1,6,10,16]
    weights = [1,2,3,5]
    capacity = 7
    print("Input: profits = " + str(profits) + ", weights = " + str(weights) + ", capacity = " + str(capacity))
    print("Output (Max Profit): " + str(knapsack_bottom_up_dynamic_programming(profits, weights, capacity)))
    print()

main()