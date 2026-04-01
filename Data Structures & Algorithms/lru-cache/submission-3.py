class Node:
    def __init__(self,key:int, value:int):
        self.key = key
        self.value = value
        self.next: 'Node | None' = None
        self.prev: 'Node | None' = None

#[h]<->[3]<->[1]<->[2]<->[5]<->[t]
# [10]

class LRUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._cache:dict[int,Node] = {}
        self._head:Node  = Node(-1,-1)
        self._tail:Node = Node(-1,-1)
        # [h]<->[t]
        self._tail.prev = self._head
        self._head.next = self._tail

    def _update(self,node:Node) -> None:

        if node.prev and node.next:
            # existing node
            node_prev = node.prev
            node_next = node.next
            node_prev.next = node.next
            node_next.prev = node.prev
        
        next_from_head = self._head.next
        node.prev = self._head
        node.next = next_from_head
        next_from_head.prev = node
        self._head.next = node
        return None
        

    def _evict(self)->None:
        # update pointers
        #[h]<->[3]<->[1]<->[2]<->[5]<->[t]
        lru_node = self._tail.prev
        prev_lru_node = lru_node.prev
        prev_lru_node.next = self._tail
        self._tail.prev = prev_lru_node
        del self._cache[lru_node.key]
        lru_node = None
        return None

    def get(self, key: int) -> int:
        if key not in self._cache:
            return -1
        node = self._cache[key]
        self._update(node)
        return self._cache[key].value
        

    def put(self, key: int, value: int) -> None:
        if key in self._cache:
            node = self._cache[key]
            node.value = value
            self._update(node)
            return None
        node = Node(key,value)
        self._cache[key] = node
        self._update(node)
        if len(self._cache) > self._capacity:
            self._evict()
        # update value if key exists, otherwise add to cache.
        # if insertion exceeds max capacity, evict lru key
    
    # A key is considered used on get/put operations
    # get/put needs to be O(1)

    # To implement this problem we need 2 data structures:
    # 1. dictionary
    #   Will hold k,v pairs -> represents cache
    # 2. doubly linkedlist
    #   - Each node will hold the key. When a key is evicted it will also get removed from the cache
    #   - the LRU node is the one adjacent to the tail node -> O(1) operation due to doubly linked list
    #   Update logic:
    #   - Each put/get request node will be moved to head
    #   - pointers will need to be re-organized.

    # {1:0,3:100}
    # [h]<->[3]<->[1]<->[2]<->[5]<->[t]
        
