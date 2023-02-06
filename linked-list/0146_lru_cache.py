"""
LRU Cache Example Diagram

doubly linked-list:     lru <--> [1, 1] <--> [2, 2] <--> mru
                                    ^           ^
                                    |           |
                                    |           |
                         -----------|-----------|----
                        |value:|    *     |     *    |
hash table:              ----------------------------
                        |key:  |    1     |     2    |
                         ----------------------------

"""

# Definition for doubly-linked list.
class ListNode:
    def __init__(self, key=None, value=None, next=None, previous=None):
        self.key, self.value = key, value
        self.next, self.previous = next, previous

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()

        self.lru, self.mru = ListNode(0, 0), ListNode(0, 0)
        self.lru.next = self.mru
        self.mru.previous = self.lru

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = ListNode(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            least_recently_used = self.lru.next
            self.remove(least_recently_used)
            del self.cache[least_recently_used.key]
    
    # inserts node at the most recently used spot (rightmost spot)
    def insert(self, node):
        previous_node, next_node = self.mru.previous, self.mru
        previous_node.next = next_node.previous = node
        node.previous, node.next = previous_node, next_node

    # removes node from anywhere in the list
    def remove(self, node):
        previous_node, next_node = node.previous, node.next
        next_node.previous, previous_node.next = previous_node, next_node

def main():
    lru_cache = LRUCache(2)
    print("Put key = 1, value = 1")
    lru_cache.put(1, 1)
    print("Put key = 2, value = 2")
    lru_cache.put(2, 2)
    print("Get key = 1: " + str(lru_cache.get(1)))
    print("Put key = 3, value = 3")
    lru_cache.put(3, 3)
    print("Get key = 2: " + str(lru_cache.get(2)))
    print("Put key = 4, value = 4")
    lru_cache.put(4, 4)
    print("Get key = 1: " + str(lru_cache.get(1)))
    print("Get key = 3: " + str(lru_cache.get(3)))
    print("Get key = 4: " + str(lru_cache.get(4)))

main()