def climbing_stairs_recursive(total_steps, step_number, dp):
    # when you land on a step greater than n, there were no possible
    # moves to get to this step
    if step_number > total_steps:
        return 0
    
    # only one way to get to nth step: stay at the nth step
    if step_number == total_steps:
        return 1

    if step_number in dp.keys():
        return dp[step_number]
    
    distinct_ways = climbing_stairs_recursive(total_steps, step_number + 1, dp) + climbing_stairs_recursive(total_steps, step_number + 2, dp)
    dp[step_number] = distinct_ways

    return distinct_ways

def climbing_stairs_memoization(n):
    dp = dict()
    return climbing_stairs_recursive(n, 0, dp)

'''
bottom up dynamic programming approach

Example: n = 5

on the nth step, there is only one way to get to it: stay at the nth step
on the n - 1 step, there is only one way to get to the nth step: move one step forward

[0][1][2][3][4][5]
[8][5][3][2][1][1]
          a [b  c]
       a [b  c]
    a [b  c]
 a [b  c]

a = b + c, reassign: c = b, b = a
repeat for n - 1 iterations

this solution is the same for 
generating the nth fibonacci number
'''
def climbing_stairs(n):
    one, two = 1, 1
    for i in range(n - 1):
        next = one + two
        two = one
        one = next

    return next

def main():
    n = 2
    print("Input: n = " + str(n))
    print("Output: " + str(climbing_stairs(n))) 
    print()

    n = 3
    print("Input: n = " + str(n))
    print("Output: " + str(climbing_stairs(n))) 
    print()

    n = 5
    print("Input: n = " + str(n))
    print("Output: " + str(climbing_stairs(n))) 
    print()

    n = 8
    print("Input: n = " + str(n))
    print("Output: " + str(climbing_stairs(n))) 
    print()

main()