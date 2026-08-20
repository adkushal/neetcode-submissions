class Node:
    def __init__(self, key: int, val: int, next: Node = None, prev: Node = None):
        self.key = key
        self.value = val
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.seen = {} # key to the node in doubly linked list
        self.tail = None
        self.head = None


    def get(self, key: int) -> int:
        if key not in self.seen:
            return -1

        self.delete(self.seen[key])
        self.add(self.seen[key])
        return self.seen[key].value
        

    def put(self, key: int, value: int) -> None:
        if key not in self.seen:
            node = Node(key, value)
            self.add(node)
            self.seen[key] = node
            if len(self.seen) > self.capacity:
                del self.seen[self.head.key]
                self.delete(self.head)

        else:
            node = self.seen[key]
            node.value = value
            self.delete(self.seen[key])
            self.add(self.seen[key])



    def delete(self, node):
        before = node.prev
        after = node.next

        # not head
        if before:
            before.next = after
        else:
            self.head = after
        
        # not tail
        if after:
            after.prev = before
        else:
            self.tail = before

    def add(self, node):
        if not self.tail:
            self.tail = node
            self.head = node

        else:
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node


        
