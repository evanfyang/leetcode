def roman_to_integer(string):
    roman_to_integer = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    integer = 0
    
    for i in range(len(string) - 1):
        if roman_to_integer[string[i]] < roman_to_integer[string[i + 1]]:
            integer -= roman_to_integer[string[i]]
        else:
            integer += roman_to_integer[string[i]]
    
    integer += roman_to_integer[string[-1]]

    return integer

def main():
    string = "III"
    print("Input: string = " + str(string))
    print("Output: " + str(roman_to_integer(string))) 
    print()

    string = "LVIII"
    print("Input: string = " + str(string))
    print("Output: " + str(roman_to_integer(string))) 
    print()

    string = "MCMXCIV"
    print("Input: string = " + str(string))
    print("Output: " + str(roman_to_integer(string))) 
    print()

main()