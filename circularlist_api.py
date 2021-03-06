#!/usr/bin/env python3

class CircularLinkedList(object):
    '''
    A circularly-linked list implementation that holds arbitrary objects.
    '''
    
    def __init__(self):
        '''Creates a linked list.'''
        self.head = None
        self.size = 0
        
    def debug_print(self):
        '''Prints a representation of the entire list.'''
        s = ''
        x = self.head
        ar = []
        if x is not None:
            ar.append(self.head.value)
            while x.next is not self.head:
                ar.append(x.next.value)
                x = x.next
        print('>>> ' + ', '.join(ar))
        
    def debug_cycle(self, count):
        '''Prints a representation of the entire cycled list up to count items'''
        for x in range(count):
            self.debug_print()
        
    def _get_node(self, index):
        '''Retrieves the Node object at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        index = int(index)
        if (index >= self.size):
            print('out of bounds')
        else:
            for i in range(self.size):
                if i == index:
                    print('you\'ve reached your index!')
                    return
        
    def add(self, item):
        '''Adds an item to the end of the linked list.'''
        if self.head is None:
            self.head = Node(item)
            self.head.next = self.head
        else:
            head = self.head
            while head.next is not self.head:
                head = head.next
            head.next = Node(item)
            head.next.next = self.head
            self.size += 1
        
    def insert(self, index, item):
        '''Inserts an item at the given index, shifting remaining items right.'''
        index = int(index)
        n = self.head
        if self.head is None and index == 0:
            self.head = Node(item)
        for x in range(index - 1):
            if n.next is self.head:
                print('this index does not exist!')
                raise ValueError('Index out of range!')
            n = n.next
        next_node = n.next
        n.next = Node(item)
        n.next.next = next_node
        n.next.next.next = self.head
        n.next.next.prev = n.next
        self.size += 1
    
    def set(self, index, item):
        '''Sets the given item at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        index = int(index)

        n = self.head
        for x in range(index):
            if n.next is self.head:
                print('this is no good')
                raise ValueError('Index out of range!')
            n = n.next
        n.value = item
        
    def get(self, index):
        '''Retrieves the item at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        index = int(index)
        '''Retrieves the item at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        n = self.head
        for i in range(index):
            if(n.next is self.head):
                print('index error!')
                raise ValueError
                return
            n = n.next
        return n.value
    
    def delete(self, index):
        '''Deletes the item at the given index. Throws an exception if the index is not within the bounds of the linked list.'''
        index = int(index)
        '''Deletes the item at the given index. Throws an exception if the index is not within the bounds of the linked list.'''
        n = self.head
        if index > self.size:
            raise ValueError('Out of range!')
        for i in range(index - 1):
            if n.next is self.head:
                raise ValueError('n.next is none!')
            n = n.next
        n.next = n.next.next
        self.size -= 1
        
    def swap(self, index1, index2):
        '''Swaps the values at the given indices.'''
        index1 = int(index1)
        index2 = int(index2)
        '''Swaps the values at the given indices.'''
        n = self.head

        if index1 > self.size or index1 < 0 or index2 > self.size or index2 < 0:
            raise ValueError('Index out of bounds')
        node1 = None
        node2 = None

        for x in range(index1):
            n = n.next
        node1 = n.value


        n = self.head
        
        for x in range(index2):
            n = n.next
        
        node2 = n.value
        n = self.head
        for x in range(max(index1,index2)+1):
            if x == index1:
                n.value = node2
            if x == index2:
                n.value = node1
            n = n.next
        
        
######################################################
###   A node in the linked list
        
class Node(object):
    '''A node on the linked list'''
    
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def __str__(self):
        return '<Node: {}>'.format(self.value)



######################################################
###   An iterator for the circular list

class CircularLinkedListIterator(object):
    def __init__(self, circular_list):
        self.list = circular_list
        self.node = circular_list.head
        self.HEAD = circular_list.head
        
        
    def has_next(self):
        if self.node.next is not None:
            return True
        else:
            return False
        
    def next(self):
        '''Returns the next value, and increments the iterator by one value.'''
        print('NEXT SONG EXISTS:', self.has_next())
        if self.has_next():
            self.node = self.node.next
            return self.node.value
        else:
            raise ValueError('next node does not exist')
