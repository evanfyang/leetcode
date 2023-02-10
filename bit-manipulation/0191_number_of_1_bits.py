def hamming_weight(n):
    weight = 0
        
    while n != 0:
        if n & 1:
            weight += 1
        n = n >> 1
    
    return weight

def main():
    n = 0b00000000000000000000000000001011
    print("Input: n = " + str("{:032b}".format(n)))
    print("Output: " + str(hamming_weight(n)))
    print() 

    n = 0b00000000000000000000000010000000
    print("Input: n = " + str("{:032b}".format(n)))
    print("Output: " + str(hamming_weight(n)))
    print() 

    n = 0b11111111111111111111111111111101
    print("Input: n = " + str("{:032b}".format(n)))
    print("Output: " + str(hamming_weight(n)))
    print() 

main()