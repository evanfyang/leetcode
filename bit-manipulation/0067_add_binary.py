def add_binary_using_conversion(a: str, b: str):
    num_1 = binary_string_to_decimal(a)
    num_2 = binary_string_to_decimal(b)

    decimal_sum = num_1 + num_2

    return decimal_to_binary_string(decimal_sum)

def binary_string_to_decimal(string):
    decimal_number = 0
    
    for i in range(len(string) - 1, -1, -1):
        if string[i] == "1":
            decimal_number += 2 ** ((len(string) - 1) - i)
    
    return decimal_number

def decimal_to_binary_string(decimal_number):
    if decimal_number == 0:
        return "0"
    
    binary_string = str()
    
    while decimal_number != 0:
        if decimal_number % 2 == 0:
            binary_string += "0"
        else:
            binary_string += "1"
        decimal_number //= 2
    
    return binary_string[::-1]


def add_binary(a, b):
    binary_string = str()
    i, j, carry = len(a) - 1, len(b) - 1, 0
    
    while i >= 0 or j >=0:
        sum = carry
        if i >= 0:
            sum += ord(a[i]) - ord("0")
        if j >= 0:
            sum += ord(b[j]) - ord("0")
        carry = 1 if sum > 1 else 0
        binary_string += str(sum % 2)
        i, j = i - 1, j - 1
    
    if carry != 0:
        binary_string += str(carry)
    
    return binary_string[::-1]

def main():
    a = "11"
    b = "1"
    print("Input: a = " + str(a) + ", b = " + str(b))
    print("Output: " + str(add_binary(a, b)))
    print()

    a = "1010"
    b = "1011"
    print("Input: a = " + str(a) + ", b = " + str(b))
    print("Output: " + str(add_binary(a, b)))
    print()
    
main()
