class Node():

    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList():

    def __init__(self):
        self.head = None
        self.tail = None
        self.ll_size = 0

    def addAtTail(self, val):
        
        #   if List is empty put to Head, link Tail to Head
        if self.head == None:
            self.head = Node(val)
            self.tail = self.head
            self.ll_size += 1
            return True
        
        #   if Tail not empty, create new Tail, repoint Previous Tail to the new Tail as next Node
        new_tail = Node(val)
        new_tail.prev = self.tail
        self.tail.next = new_tail
        self.tail = new_tail
        self.ll_size += 1
        return True

    def addAtHead(self, val):

        if self.head == None:
            self.head = Node(val)
            self.tail = self.head
            self.ll_size += 1
            return True
        
        new_head = Node(val)
        self.head.prev = new_head
        new_head.next = self.head
        self.head = new_head
        self.ll_size += 1
        return True

    def get(self, idx):

        current_node = self.head
        if idx < 0:
            return False

        # if requested index is larger than LL
        if idx + 1 > self.ll_size:
            return False
        
        # if reqested index is the same size as LL return Tail
        if idx + 1 == self.ll_size:
            return self.tail.val

        # if requested index is 0 and LL size is 1 or larger, return Head
        if idx == 0 and self.ll_size > 0:
            return self.head.val
        
        # if requested index in the middle iterate thru the LL requested amount of time
        if idx < self.ll_size//2:
            while idx != 0:
                current_node = current_node.next
                idx -= 1
            return current_node.val
        else:
            current_node = self.tail
            while self.ll_size - idx - 1 != 0:
                current_node = current_node.prev
                idx += 1
            return current_node.val

    
    def addAtIndex(self, idx, val):

        # if idx negative
        if idx < 0:
            return False

        # if idx if larger than size of LL – False
        if idx > self.ll_size:
            return False

        #if idx at 0 index – merge Head right
        if idx == 0:
            return self.addAtHead(val)

        #if idx the same as size of LL – add at Tail left merge
        if idx == self.ll_size:
            return self.addAtTail(val)

        #if idx is in the middle – add Node, relink nodes
        if idx < self.ll_size//2:
            current_node = self.head
            while idx != 0:
                current_node = current_node.next
                idx -= 1
            self.ll_size += 1
            new_node = Node(val)
            cur_node_prev = current_node.prev
            new_node.prev = cur_node_prev
            cur_node_prev.next = new_node
            new_node.next = current_node
            current_node.prev = new_node
            return True
        else:
            current_node = self.tail
            while self.ll_size - idx - 1 != 0:
                current_node = current_node.prev
                idx += 1
            self.ll_size += 1
            new_node = Node(val)
            cur_node_prev = current_node.prev
            new_node.prev = cur_node_prev
            cur_node_prev.next = new_node
            new_node.next = current_node
            current_node.prev = new_node
            return True


    def deleteAtIndex(self, idx):

        # if idx negative
        if idx < 0:
            return False

        # if idx if larger than size of LL – False
        if idx + 1 > self.ll_size:
            return False

        #if idx at 0 index – delete Head
        if idx == 0 and self.ll_size > 0:
            self.ll_size -= 1
            if self.ll_size == 0:
                self.head = None
                self.tail = None
                return True
            else:
                current_head = self.head
                self.head = current_head.next
                return True

        #if idx the same as size of LL – delete Tail
        if idx + 1 == self.ll_size:
            self.ll_size -= 1
            current_tail = self.tail
            self.tail = current_tail.prev
            return True

        #if idx is in the middle – remove Node, relink nodes
        if idx < self.ll_size//2:
            current_node = self.head
            while idx != 0:
                current_node = current_node.next
                idx -= 1
            self.ll_size -= 1
            cur_node_next = current_node.next
            cur_node_prev = current_node.prev
            cur_node_next.prev = cur_node_prev
            cur_node_prev.next = cur_node_next
            return True
        else:
            current_node = self.tail
            while self.ll_size - idx - 1 != 0:
                current_node = current_node.prev
                idx += 1
            self.ll_size -= 1
            cur_node_next = current_node.next
            cur_node_prev = current_node.prev
            cur_node_next.prev = cur_node_prev
            cur_node_prev.next = cur_node_next
            return True

