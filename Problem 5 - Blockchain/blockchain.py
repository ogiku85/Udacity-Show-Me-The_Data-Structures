import hashlib
from datetime import datetime

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash(data)
      self.next = None

    def calc_hash(self, data):
      sha = hashlib.sha256()

      hash_str = data.encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()

    def __repr__(self):
        s = ''
        s += "Timestamp: " + str(self.timestamp.strftime("%H:%M:%S %m/%d/%y")) + "\n"
        s += "Data: " + self.data + "\n"
        s += "SHA256 Hash: " + str(self.hash) + "\n"
        s += "Prev_Hash: " + str(self.previous_hash) + "\n"
        return s

class BlockChain:
    def __init__(self):
        self.head = None
    
    def prepend(self, value):
        """ Prepend a value to the beginning of the chain. """
        # TODO: Write function to prepend here
        transaction_date = datetime.now()
        previous_hash = "0"
        new_head = Block(transaction_date, value, previous_hash)
        new_head.next = self.head
        if self.head is not None:
            self.head.previous_hash = new_head.hash
        self.head = new_head
    
    def append(self, value):
        """ Append a value to the end of the chain. """    
        # TODO: Write function to append here    
        current_block = self.head
        transaction_date = datetime.now()
        previous_hash = "0"

        if self.head is None:
            self.head = Block(transaction_date, value, previous_hash)
        else:
            while current_block.next is not None:
                current_block = current_block.next
            previous_hash = current_block.hash
            current_block.next = Block(transaction_date, value, previous_hash)
    
    def remove(self, value):
        """ Remove first occurrence of value. """
        # TODO: Write function to remove here
        if self.head is not None and self.head.data == value:
            self.head = self.head.next
            return
        current_block = self.head
        while current_block.next:
            if current_block.next.data == value:
                current_block.next = current_block.next.next
                if current_block.next.next is not None:
                    #set previous hash of the next block to the one before the removed block
                    current_block.next.next.previous_hash = current_block.hash
                break
            current_block = current_block.next
    
    def search(self, value):
        """ Search the block chain for a block with the requested value and return the block. """
        # TODO: Write function to search here
        current_block = self.head
        while current_block is not None:
            if current_block.data == value:
                return current_block
            current_block = current_block.next
    
    def pop(self):
        """ Return the first block's value and remove it from the list. """
        # TODO: Write function to pop here
        result = self.head
        self.head = self.head.next
        if self.head is not None:
            self.head.previous_hash = "0"
        return result.data
    
    def insert(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the
        length of the list, append to the end of the list. """
            
        # TODO: Write function to insert here  

        transaction_date = datetime.now()
        previous_hash = "0"  

        current_block = self.head
        count = 1
        inserted = False
        if self.head is None:
            self.head = Block(transaction_date, value, previous_hash)
            return
        if pos == 0:
            new_block = Block(transaction_date, value, previous_hash)
            new_block.next = self.head
            self.head = new_block
            if self.head.next is not None:
                self.head.next.previous_hash = self.head.hash
            return
        while current_block.next is not None and count <= pos:
            if count == pos:
                new_block = Block(transaction_date, value, previous_hash)
                new_block.next = current_block.next
                current_block.next = new_block
                # updae prevoius hash appropriately
                new_block.previous_hash = current_block.hash
                new_block.next.previous_hash = new_block.hash

                inserted = True
                break
            current_block = current_block.next
            count +=1
        if inserted == False and current_block:
            current_block.next = Block(transaction_date, value, previous_hash)
            current_block.next.previous_hash = current_block.hash
    def size(self):
        """ Return the size or length of the linked list. """
        # TODO: Write function to get size here
        count = 0
        if self.head is None:
            return count
        current_block = self.head
        while current_block is not None:
            count+=1
            current_block = current_block.next
        return count
    
    def to_list(self):
        out = []
        block = self.head
        while block:
            out.append(block.data)
            block = block.next
        return out

    def __repr__(self):

        # Edge case
        if self.head is None:
            return "Blockchain is empty"

        s = ''
        current_block = self.head
        count = 0
        while current_block is not None:
            s += 'Block ' + str(count) + '\n'
            s += str(current_block) + '\n'

            current_block = current_block.next
            count += 1
        return s
#Edge case Test
block_chain = BlockChain()
print(block_chain) #Blockchain is empty

# Test prepend
block_chain = BlockChain()
block_chain.prepend("1")
block_chain.prepend("2")
assert block_chain.to_list() == ["2","1"], f"list contents: {block_chain.to_list()}"
print(block_chain)

block_chain = BlockChain()
block_chain.append("1")
block_chain.append("2")
assert block_chain.to_list() == ["1","2"], f"list contents: {block_chain.to_list()}"
print(block_chain)

block_chain = BlockChain()
block_chain.append("1")
block_chain.append("2")

block_chain.insert("3", 1)
assert block_chain.to_list() == ["1","3","2"], f"list contents: {block_chain.to_list()}"
print(block_chain)


block_chain.remove("3")
assert block_chain.to_list() == ["1","2"], f"list contents: {block_chain.to_list()}"
