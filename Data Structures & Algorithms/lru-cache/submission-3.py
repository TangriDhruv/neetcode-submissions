class Node:
    def __init__(self,key,value):
        self.key,self.value = key,value
        self.prev = self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.left, self.right = Node(0,0),Node(0,0)
        
        self.left.next, self.right.prev = self.right,self.left
    
    def insert(self,node):
        prv,nxt = self.right.prev,self.right
        prv.next = nxt.prev = node
        node.next, node.prev = nxt,prv
    
    def remove(self,node):
        prv,nxt = node.prev, node.next
        prv.next,nxt.prev = nxt,prv

    def get(self, key: int) -> int:
        if key in self.dic:
            self.remove(self.dic[key])
            self.insert(self.dic[key])
            return self.dic[key].value
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic[key].value = value
            self.remove(self.dic[key])
            self.insert(self.dic[key])
        else:
            self.dic[key] = Node(key,value)
            self.insert(self.dic[key])
        
        if len(self.dic) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.dic[lru.key]
        
