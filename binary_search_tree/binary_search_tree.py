"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from queue import Queue

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Case 1: value is less than self.value
        if value < self.value:
            # If there is no left child, insert value here
            if self.left is None:
               self.left = BSTNode(value)
            else:
                # Repeat the process on left subtree
                self.left.insert(value)

        # Case 2: value is greater than or equal self.value
        elif value >= self.value:
            # If there is no right child, insert value here
            if self.right is None:
               self.right = BSTNode(value)
            else:
                # Repeat the process on right subtree
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Case 1: self.value is equal to the target
        if self.value == target:
            return True
        # Case 2: target is less than self.value 
        if target < self.value:
            # if self.left is None, it isn't in the tree
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        # Case 3: otherwise
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        max_value = self.value

        if self.right is None:
            return self.value
        else:
            max_value = self.right.get_max()

        return max_value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call fn on all values
        fn(self.value)

        if self.left:
            # recurse on everythin left of root
            self.left.for_each(fn)
       
        if self.right:
            # recurse on everythin right of root
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # if the current node is None
        # we know we've reached the end of a recursion
        # (base case) we want to return
        if node is None:
            return

        # check if we can "move left"
        if node.left is not None:
            node.in_order_print(node.left)

        # visit the node by printing its value
        print(node.value)

        # check if we can "move right"
        if node.right is not None:
            node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    from collections import deque

    def bft_print(self, node):
        # You should import the queue class from earlier in the
        # week and use that class to implement this method
        # Use a queue to form a "line" 
        # for the nodes to "get in"
        # start by placing the root in the queue
        queue = node.deque()
        queue.append(node)
        # need a while loop to iterate
        # what are we checking in the while statement?
        # while length of queue is greater than 0
        while len(queue) > 0:
            # dequeue item from front of queue
            current = queue.popleft()
            # print that item
            print(current.value)
            # place current item's left node in queue if not None
            if current.left:
                queue.append(current.left)
            # place current item's right node in queue if not None
            if current.right:
                queue.append(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        pass
        # initialize an empty stack
        stack = []
        # push the root node onto the stack
        stack.append(node)

        # need a while loop to manager our iteration
        # if stack is not empty enter the while loop
        while len(stack) > 0:
            # pop top item off the stack
            current = stack.pop()
            # print that item's value
            print(current.value)

            # if there is a right subtree
            if current.right:
                # push right item onto the stack
                stack.append(current.right)
                
            # if there is a left subtree
            if current.left:
                # push left item onto the stack
                stack.append(current.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
