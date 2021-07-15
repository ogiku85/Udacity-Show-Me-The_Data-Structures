class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def print_list(self):
        current_node = self.head
        print("printing list")
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next
    def add_to_front_of_List(self, new_node):
        #if the list is empty set head and tail to the new node
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        if self.head == self.tail:
            self.tail.previous = self.head

        new_node.next = self.head
        new_node.previous = None
        self.head.previous = new_node
        self.head = new_node
        return
    
    def remove_from_back_of_list(self):
        if self.tail is None:
            return

        removed_node = self.tail
        self.remove_node(removed_node)
        return removed_node
    
    def remove_node(self, node):
        if node is None:
            return
        if node.previous is not None:
            node.previous.next = node.next
        if node.next is not None:
            node.next.previous = node.previous
        else:
            self.tail = node.previous

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.dict = {}
        self.list = DoubleLinkedList()
        self.count = 0

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key not in self.dict:
            return -1
        resultNode = self.dict[key]
        result = resultNode.value
        #remove node from list
        self.list.remove_node(resultNode)
        #add accessed node to front of the list so that it is in the most recently accessed area
        #items at the back of the list are the least frequently accessed
        self.list.add_to_front_of_List(resultNode)
        return result

    def set(self, key, value):
        #taking care of invalid parameters
        if key is None or value is None:
            print("Invalid key or value specified")
            return
        if self.capacity <= 0:
            print("Cannot add items to a cache with a capacity of zero")
            return
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key in self.dict:
            resultNode = self.dict[key]
            #remove the existing node from the list
            self.list.remove_node(resultNode)
            #update node with the latest value
            resultNode.value = value
            #add to front of the list to make it the most recently accessed
            self.list.add_to_front_of_List(resultNode)
        else:
            if self.capacity == self.count:
                #the list is full we need to evict the least frequent node
                #remove from the back of the list
                deleted_node = self.list.remove_from_back_of_list()
                #remove deletd node from the dictionary to make room for new entry
                self.dict.pop(deleted_node.key,None)
                self.count -= 1
            
            #add new value to dictionary and list
            new_node = Node(key, value)
            self.list.add_to_front_of_List(new_node)
            self.dict[key] = new_node
            self.count += 1

#invalid paramters or edge cases tests
our_cache = LRU_Cache(0)
our_cache.set(1, 1);           #Cannot add items to a cache with a capacity of zero
print(our_cache.get(1))       # returns 1

#other tests
our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

