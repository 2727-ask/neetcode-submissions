class LRUCache:

    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.next = None
            self.prev = None

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.head = self.Node(0,0)
        self.tail = self.Node(0,0)

        self.head.next = self.tail
        self.tail.prev = self.head
        
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.bring_forward(key)
            return self.cache[key].val
        return -1


    def bring_forward(self, key):
        node = self.cache[key]
        node.prev.next = node.next
        node.next.prev = node.prev

        front = self.head.next
        self.head.next = node
        node.next = front
        node.prev = self.head

        front.prev = node
         

    def remove(self):
        last = self.tail.prev
        temp = last.prev
        temp.next = self.tail
        self.tail.prev = temp
        del self.cache[last.key]
    
    def insert(self, key, val):

        first = self.head.next
        newNode = self.Node(key,val)
        self.cache[key] = newNode

        self.head.next = newNode
        newNode.prev = self.head

        newNode.next = first
        first.prev = newNode

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.bring_forward(key)
            return

        if(len(self.cache) == self.capacity):
            self.remove()
        
        self.insert(key, value)


        
