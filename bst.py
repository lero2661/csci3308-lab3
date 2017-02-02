# This class implements a Binary Search Tree Class
# The binary search tree class will include functionality of
#   1. Insert a Node in the Tree.
#   2. Search for a Node in the Tree
#   3. Various traversals including in order, preorder and postorder traversals.
#
#  The binary search tree is made of class Node objects.
#    Each node has three members: key is an integer, left and right child point to nodes.
#    If left is None, then it means that the node has no left child.
#    If right is None then the node has no right child.

# name: Leah Rogers
# On my honor as a University of Colorado student I affirm that this code is my own work and that it was not written with any unauthorized help


class Node:

    def __init__(self, my_key): # Constructor for the Node.
        self.key = my_key       # Set the key to my_key
        self.left = None        # Set left child to None
        self.right = None       # Set right child to None

    def insert(self, key_to_insert):
        if(self.key == key_to_insert):
            return
        if(key_to_insert < self.key):
            if(self.left is not None):
                self.left.insert(key_to_insert)
            else:
                self.left = Node(key_to_insert)
        else:
            if(self.right is not None):
                self.right.insert(key_to_insert)
            else:
                self.right = Node(key_to_insert)

    def inorder_traversal(self, ret_list):
        if(self.left is not None):
            self.left.inorder_traversal(ret_list)
        ret_list.append(self.key)
        if(self.right is not None):
            self.right.inorder_traversal(ret_list)

    def get_depth(self):

        if(self.right is not None):
            right_depth = self.right.get_depth()
        else:
            right_depth = 0
        if(self.left is not None):
            left_depth = self.left.get_depth()
        else:
            left_depth = 0
        return 1 + max(right_depth, left_depth)


    def key_exists(self, key_to_find):

        if(self.key == key_to_find):
            return True
        else:
            if((key_to_find < self.key) and (self.left is None)):
                return False
            elif((key_to_find < self.key) and (self.left is not None)):
                return self.left.key_exists(key_to_find)
            elif((key_to_find > self.key) and (self.right is None)):
                return False
            else:
                return self.right.key_exists(key_to_find)

if __name__ == '__main__':
    print('Please do not call this file directly.')
    print('To run autograder script: please call the test_bst.py')
