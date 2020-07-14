"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        pass
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # create instance of ListNode with value
        newNode = ListNode(value)
        # increment the DLL length attribute
        self.length += 1
        # if DLL is empty
        if self.head is None and self.tail is None:
            # set head and tail to the new node instance
            self.head = newNode
            self.tail = newNode
        # if DLL is not empty
        else:
            # set new node's next to current head
            newNode.next = self.head
            # set head's prev to new node
            newNode.prev = newNode
            # set head to the new node
            self.head = newNode
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # store the value of the head
        removedHead = self.head.value
        # decrement the length of the DLL
        # delete the head
        self.delete(self.head)
            # if head.next is not None
                # set head.next's prev to None
                # set head to head.next
            # else (if head.next is None)
                # set head to None
                # set tail to None

        # return the value
        return removedHead
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # create instance of ListNode with value
        newNode = ListNode(value)
        # increment the DLL length attribute
        self.length += 1
        # if DLL is empty
        if self.head is None and self.tail is None:
            # set head and tail to the new node instance
            self.head = newNode
            self.tail = newNode
        
        # if DLL is not empty
        else:
            # set new node's prev to current tail
            newNode.prev = self.tail
            # set tail's next to new node
            self.tail.next = newNode
            # set tail to the new node
            self.tail = newNode
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # store the value of the tail
        removedTail = self.tail.value
        # decrement the length of the DLL
        # delete the tail
        self.delete(self.tail)
            # if tail.prev is not None
                # set tail.prev's next to None
                # set tail to tail.prev
            # else (if tail.prev is None)
                # set head to None
                # set tail to None

        # return the value
        return removedTail
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        newHead = node.value
        self.delete(node)
        self.add_to_head(newHead)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        newTail = node.value
        self.delete(node)
        self.add_to_tail(newTail)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        self.length -= 1

        if self.head is None and self.tail is None:
            return None

        if self.head is self.tail:
            self.head = None
            self.tail = None
        elif self.head is node:
            self.head = node.next
            node.delete()
        elif self.tail is node:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.head is None and self.tail is None:
            return None

        if self.head.next is None:
            return self.head.value

        maxValue = self.head.value
        compare = self.head.next

        while compare:
            if compare.value > maxValue:
                maxValue = compare.value

            compare = compare.next

        return maxValue