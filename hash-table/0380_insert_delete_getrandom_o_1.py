import random

class RandomizedSet:
    def __init__(self):
        self.hash_set = set()

    def insert(self, val: int) -> bool:
        if val not in self.hash_set:
            self.hash_set.add(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.hash_set:
            self.hash_set.remove(val)
            return True
        else:
            return False

    def get_random(self) -> int:
        return random.choice(list(self.hash_set))

def main():
    randomized_set = RandomizedSet()
    print("Insert 1: " + str(randomized_set.insert(1)))
    print("Remove 2: " + str(randomized_set.remove(2)))
    print("Insert 2: " + str(randomized_set.insert(2)))
    print("Get Random: " + str(randomized_set.get_random()))
    print("Remove 2: " + str(randomized_set.remove(2)))
    print("Insert 2: " + str(randomized_set.insert(2)))
    print("Get Random: " + str(randomized_set.get_random()))

main()