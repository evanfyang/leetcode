def counting_bits_brute_force(n):
    number_of_ones = list()

    for i in range(n):
        ones_count = 0
        number = i
        while number != 0:
            ones_count += number % 2
            number //= 2
        number_of_ones.append(ones_count)

    return number_of_ones

"""
0 -> 0000 -> dp[0] = 0 ones
1 -> 0001 -> dp[1 - 1] + 1 = 0 + 1 = 1 one
2 -> 0010 -> dp[2 - 2] + 1 = 0 + 1 = 1 one
3 -> 0011 -> dp[3 - 2] + 1 = 1 + 1 = 2 ones
4 -> 0100 -> dp[4 - 4] + 1 = 0 + 1 = 1 one
5 -> 0101 -> dp[5 - 4] + 1 = 1 + 1 = 2 ones
6 -> 0110 -> dp[6 - 4] + 1 = 1 + 1 = 2 ones
7 -> 0111 -> dp[7 - 4] + 1 = 2 + 1 = 3 ones
8 -> 1000 -> dp[8 - 8] + 1 = 0 + 1 = 1 one
9 -> 1001 -> dp[9 - 8] + 1 = 1 + 1 = 2 ones
"""

def counting_bits(n):
    dp = [0] * (n + 1)
    offset = 1
    
    for i in range(1, n + 1):
        if i == offset * 2:
            offset *= 2
        dp[i] = dp[i - offset] + 1
    
    return dp

def main():
    n = 2
    print("Input: n = " + str(n))
    print("Output: " + str(counting_bits(n)))
    print() 
    
    n = 5
    print("Input: n = " + str(n))
    print("Output: " + str(counting_bits(n)))
    print()
    
    n = 9
    print("Input: n = " + str(n))
    print("Output: " + str(counting_bits(n)))
    print()

main()
