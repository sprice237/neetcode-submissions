class Node:
    def __init__(self, key, value, next, prev):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity

        self.head = Node(-1, -1, None, None)
        self.tail = Node(-1, -1, None, None)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.d = {}

    def print(self) -> None:
        nodes = []
        n = self.head
        while n:
            nodes.append(str(n.key))
            n = n.next
        print(f"forwards: {" > ".join(nodes)}")

        nodes = []
        n = self.tail
        while n:
            nodes.insert(0, str(n.key))
            n = n.prev
        print(f"backwards: {" < ".join(nodes)}")
        
    def get_node(self, key: int) -> Node:
        n = self.d.get(key)

        if not n:
            return None

        n.prev.next = n.next
        n.next.prev = n.prev

        n.prev = self.head
        n.next = self.head.next

        self.head.next.prev = n
        self.head.next = n

        return n

    def get(self, key: int) -> int:
        # self.print()
        n = self.get_node(key)
        # self.print()
        return n.value if n else -1

    def put(self, key: int, value: int) -> None:
        n = self.get_node(key)

        if n:
            n.value = value
            return

        # self.print()
        n = Node(key, value, self.head.next, self.head)
        
        self.head.next.prev = n
        self.head.next = n
        self.d[key] = n

        # self.print()

        if self.size == self.capacity:
            del self.d[self.tail.prev.key]
            self.tail.prev = self.tail.prev.prev
            self.tail.prev.next = self.tail
        else:
            self.size += 1
