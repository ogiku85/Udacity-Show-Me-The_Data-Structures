import sys
from queue import PriorityQueue

class HuffmanNode:
    def __init__(self, data, frequency):
        self.data = data
        self.left = None
        self.right = None
        self.frequency = frequency

    def is_leaf(self):
        return self.left is None and self.right is None
    def __lt__(self, other):
        return self.frequency < other.frequency

class HuffmanTree:
    def __init__(self,data):
        self.head = None
        self.queue = PriorityQueue()
        self.dict = {}
        self.data = data
        self.lookup_table = {}

    def generate_frequency_list(self):
        if self.data is None:
            print('Invalid data specified. Cannot generate frequency list')
            return
        if self.data == '':
            print('data is an empty string')
            return
        for c in self.data:
            if self.dict.get(c) is not None:
                self.dict[c] +=1
            else:
                self.dict[c] = 1

    def build_tree(self):

        self.generate_frequency_list()
        if len(self.dict.items()) <= 0:
            print('Cannot generate tree. Specified word does not conatin valid characters.')
            return
        for k, v in self.dict.items():
            new_node = HuffmanNode(k, v)
            self.queue.put(new_node)

        if self.queue.qsize() == 1:
            self.queue.put(HuffmanNode(None,1))
        
        size = self.queue.qsize()
        ss = self.queue.queue
        while self.queue.qsize() > 1:
            left = self.queue.get()
            right = self.queue.get()
            combined_frequency = left.frequency + right.frequency
            default_data = None
            parent = HuffmanNode(default_data, combined_frequency)
            parent.left = left
            parent.right = right
            self.queue.put(parent)
        # return root Nnode
        self.head = self.queue.get()
        return self.head

    def build_lookup_table(self, current_node, current_code):
        self.build_lookup_table_helper(self.head, "")

    def build_lookup_table_helper(self, current_node, current_code):
        if current_node is None:
            return
        if current_node.is_leaf() is not True:
            #For each node, in the Huffman tree, assign a bit 0 for left child and a 1 for right child.
            self.build_lookup_table_helper(current_node.left, current_code + '0')
            self.build_lookup_table_helper(current_node.right, current_code + '1')
        else:
            self.lookup_table[current_node.data] = current_code
        
    def generate_encoded_data(self):
        self.build_tree()
        self.build_lookup_table(self.head, "")
        encoded_data = ''
        for x in self.data:
            encoded_data += self.lookup_table[x]
        return encoded_data

def huffman_encoding(data):
    if data is None or data == '':
        print('Cannot decode invalid data or empty string')
        return None, None
    huffman_tree = HuffmanTree(data)
    huffman_tree.build_tree()
    huffman_tree.build_lookup_table(huffman_tree.head, "")
    encoded_data = ''
    for x in huffman_tree.data:
        encoded_data += huffman_tree.lookup_table[x]
    return encoded_data, huffman_tree

def huffman_decoding(data,tree):
    decoded_data = ''
    current_node = tree.head
    if current_node is None:
        print('Cannot decode data. Invalid tree provided')
        return
    if data is None:
        print('Cannot decode. invalid data specified')
        return
    index = 0
    while index < len(data):
        while current_node.is_leaf() is not True:
            bit = data[index]
            if bit == '1':
                current_node = current_node.right
            elif bit == '0':
                current_node = current_node.left
            else:
                raise Exception('invalid bit found')
            index += 1
        decoded_data += current_node.data
        current_node = tree.head
    return decoded_data

def test_function(data):
    encoded_data, tree = huffman_encoding(data)

    if encoded_data is not None:
        print("The size of the data is: {}\n".format(sys.getsizeof(data)))
        print("The content of the data is: {}\n".format(data))

        print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, tree)

        print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print("The content of the decoded data is: {}\n".format(decoded_data))
    else:
        print('No valid result returned')
    print('\n\n\n')


# Edge test cases
test_function('') #Cannot decode invalid data or empty string
test_function('T')
test_function('TT')
test_function(None) #Cannot decode invalid data or empty string
# general test cases
test_function('The bird is the word')