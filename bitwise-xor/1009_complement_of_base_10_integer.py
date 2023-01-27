def complement_of_base_10_integer(number):
    # number ^ complement = all_bits_set
    # number ^ number ^ complement = number ^ all_bits_set
    # 0 ^ complement = number ^ all_bits_set
    # complement = numeber ^ all_bits_set

    if number == 0:
        return 1
    
    n = number
    bit_count = 0
    
    while n != 0:
        bit_count += 1
        n = n >> 1
    
    all_bits_set = pow(2, bit_count) - 1

    return number ^ all_bits_set

def main():
    number = 5
    print("Input: number = " + str(number))
    print("Output: " + str(complement_of_base_10_integer(number)))
    print()

    number = 7
    print("Input: number = " + str(number))
    print("Output: " + str(complement_of_base_10_integer(number)))
    print()

    number = 8
    print("Input: number = " + str(number))
    print("Output: " + str(complement_of_base_10_integer(number)))
    print()

    number = 10
    print("Input: number = " + str(number))
    print("Output: " + str(complement_of_base_10_integer(number)))
    print()

main()