# https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root, min=-float('inf'), max=float('inf')):
    if root == None:
        return True
    return root.data > min and root.data < max and checkBST(root.left,min,root.data) and checkBST(root.right,root.data,max)