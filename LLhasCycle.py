# https://www.hackerrank.com/challenges/ctci-linked-list-cycle/problem
"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    myDict = {}
    while head.next != None:
        if head in myDict.keys():
            return True
        myDict.setdefault(head, 0)
        myDict[head] += 1
    return False
    
