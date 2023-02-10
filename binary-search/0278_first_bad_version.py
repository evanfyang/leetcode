# The isBadVersion API is already defined for you.
# def is_bad_version(version: int) -> bool:

def first_bad_version(self, n: int) -> int:
    left, right = 0, n

    while left <= right:
        middle = (left + right) // 2

        if is_bad_version(middle):
            if not is_bad_version(middle - 1):
                return middle
            else:
                right = middle - 1
        else:
            left = middle + 1
    
    return -1