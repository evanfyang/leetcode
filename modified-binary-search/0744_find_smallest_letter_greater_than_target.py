def find_smallest_letter_greater_than_target(letters, target):
    start, end = 0, len(letters) - 1

    while start <= end:
        middle = (start + end) // 2

        if target < letters[middle]:
            end = middle - 1
        else:
            start = middle + 1
    
    return letters[start % len(letters)]

def main():
    letters = ["a","c","f","h"]
    target = "f"
    print("Input: letters = " + str(letters) + ", target = " + str(target))
    print("Output: " + str(find_smallest_letter_greater_than_target(letters, target)))
    print()

    letters = ["a","c","f","h"]
    target = "b"
    print("Input: letters = " + str(letters) + ", target = " + str(target))
    print("Output: " + str(find_smallest_letter_greater_than_target(letters, target)))
    print()

    letters = ["a","c","f","h"]
    target = "m"
    print("Input: letters = " + str(letters) + ", target = " + str(target))
    print("Output: " + str(find_smallest_letter_greater_than_target(letters, target)))
    print()

    letters = ["a","c","f","h"]
    target = "h"
    print("Input: letters = " + str(letters) + ", target = " + str(target))
    print("Output: " + str(find_smallest_letter_greater_than_target(letters, target)))
    print()

    letters = ["c","f","j"]
    target = "a"
    print("Input: letters = " + str(letters) + ", target = " + str(target))
    print("Output: " + str(find_smallest_letter_greater_than_target(letters, target)))
    print()

    letters = ["c","f","j"]
    target = "c"
    print("Input: letters = " + str(letters) + ", target = " + str(target))
    print("Output: " + str(find_smallest_letter_greater_than_target(letters, target)))
    print()    

    letters = ["x","x","y","y"]
    target = "z"
    print("Input: letters = " + str(letters) + ", target = " + str(target))
    print("Output: " + str(find_smallest_letter_greater_than_target(letters, target)))
    print()  

main()