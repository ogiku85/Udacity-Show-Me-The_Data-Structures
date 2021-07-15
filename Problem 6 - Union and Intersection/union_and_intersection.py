class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    if llist_1.head is None and llist_2.head is None:
        print('No operation performed. Both Lists are empty')
        return

    result = LinkedList()
    uniqueSet = set()
    if llist_1 is not None:
        current_node = llist_1.head
        while current_node is not None:
            if current_node.value not in uniqueSet:
                uniqueSet.add(current_node.value)
                result.append(current_node.value)

            current_node = current_node.next
    if llist_2 is not None:
        current_node = llist_2.head
        while current_node is not None:
            if current_node.value not in uniqueSet:
                uniqueSet.add(current_node.value)
                result.append(current_node.value)
                
            current_node = current_node.next
    return result

def intersection(llist_1, llist_2):
    # Your Solution Here
    if llist_1.head is None and llist_2.head is None:
        print('No operation performed. Both Lists are empty')
        return

    result = LinkedList()
    uniqueSet = set()
    if llist_1 is not None:
        current_node = llist_1.head
        while current_node is not None:
            if current_node.value not in uniqueSet:
                uniqueSet.add(current_node.value)

            current_node = current_node.next

    if llist_2 is not None:
        current_node = llist_2.head
        while current_node is not None:
            if current_node.value in uniqueSet:
                result.append(current_node.value)
                
            current_node = current_node.next
    return result


#Edge Test case 

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2)) # No operation performed. Both Lists are empty
print (intersection(linked_list_1,linked_list_2))# No operation performed. Both Lists are empty


linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = []
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2)) # 6 -> 32 -> 4 -> 9 -> 1 -> 11 -> 21 ->
print (intersection(linked_list_1,linked_list_2)) #6 -> 32 -> 4 -> 9 -> 1 -> 11 -> 21 ->

# general test case

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))