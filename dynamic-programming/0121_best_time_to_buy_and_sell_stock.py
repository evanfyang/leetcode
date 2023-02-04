def best_time_to_buy_and_sell_stock(prices):
    min_price = float("inf")
    max_profit = 0

    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        if prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
    
    return max_profit

def main():
    prices = [7,1,5,3,6,4]
    print("Input: prices = " + str(prices))
    print("Output: " + str(best_time_to_buy_and_sell_stock(prices))) 
    print() 

    prices = [7,6,4,3,1]
    print("Input: prices = " + str(prices))
    print("Output: " + str(best_time_to_buy_and_sell_stock(prices))) 
    print() 

main()