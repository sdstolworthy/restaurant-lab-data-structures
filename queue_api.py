#!/usr/bin/env python3
from linkedlist_api import LinkedList

class Queue(object):
    '''
    A linked list implementation of a queue.
    
    This contains a LinkedList internally.  It does not extend LinkedList.
    In other words, this class uses "Composition" rather than "Inheritance".
    '''
    
    def __init__(self):
        '''Constructor'''
        self.queue = LinkedList()
    
    def debug_print(self):
        '''Prints a representation of the entire queue.'''
        self.queue.debug_print()

    def enqueue(self, item):
        '''Adds an item to the end of the queue'''
        self.queue.add(item)
        
    def dequeue(self):
        '''
        Dequeues the first item from the list.  This involves the following:
            1. Get the first node in the list.
            2. Delete the node from the list.
            3. Return the value of the node.
        '''
        n = self.queue.get(0)
        self.queue.delete(0)
        return n

    def size(self):
        '''Returns the number of items in the queue'''
        return self.queue.size
