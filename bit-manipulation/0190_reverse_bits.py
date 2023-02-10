"""
n = 00000010100101000001111010011101 

#######################################

i = 0

1. 00000010100101000001111010011101 
2. 00000000000000000000000000000001 &
   --------------------------------
3. 00000000000000000000000000000001

1. n >> i 
2. 1 in 32 bit representation 
3. apply bitwise and to (1) and (2) to get the current rightmost bit


4. 00000000000000000000000000000000 
5. 10000000000000000000000000000000 |
   --------------------------------
6. 10000000000000000000000000000000

4. result
5. current rightmost bit from n shifted 31 - i places (bit << 31 - i)
6. apply bitwise or to (4) and (5) to get updated result

#######################################

i = 1

1. 00000001010010100000111101001110 
2. 00000000000000000000000000000001 &
   --------------------------------
3. 00000000000000000000000000000000

1. n >> i 
2. 1 in 32 bit representation 
3. apply bitwise and to (1) and (2) to get the current rightmost bit


4. 10000000000000000000000000000000 
5. 00000000000000000000000000000000 |
   --------------------------------
6. 10000000000000000000000000000000

4. result
5. current rightmost bit from n shifted 31 - i places (bit << 31 - i)
6. apply bitwise or to (4) and (5) to get updated result

#######################################

i = 2

1. 00000000101001010000011110100111 
2. 00000000000000000000000000000001 &
   --------------------------------
3. 00000000000000000000000000000001

1. n >> i 
2. 1 in 32 bit representation 
3. apply bitwise and to (1) and (2) to get the current rightmost bit


4. 10000000000000000000000000000000 
5. 00100000000000000000000000000000 |
   --------------------------------
6. 10100000000000000000000000000000

4. result
5. current rightmost bit from n shifted 31 - i places (bit << 31 - i)
6. apply bitwise or to (4) and (5) to get updated result

"""

def reverse_bits(n):
    result = 0

    for i in range(32):
        bit = (n >> i) & 1
        result = result | (bit << (31 - i))
    
    return result

def main():
    n = 0b00000010100101000001111010011100
    print("Input: n = " + str("{:032b}".format(n)))
    print("Output: " + str("{:032b}".format(reverse_bits(n))))
    print() 

    n = 0b11111111111111111111111111111101
    print("Input: n = " + str("{:032b}".format(n)))
    print("Output: " + str("{:032b}".format(reverse_bits(n))))
    print() 

main()