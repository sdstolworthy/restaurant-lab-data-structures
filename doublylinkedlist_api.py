#!/usr/bin/env python3


class DoublyLinkedList(object):
    '''
    A linked list implementation that holds arbitrary objects.
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
        rar = []
        if x is not None:
            ar.append(self.head.value)
            while x.next is not None:
                ar.append(x.next.value)
                x = x.next
        if x is not None:
            rar.append(x.value)
            while x.prev is not None:
                rar.append(x.prev.value)
                x = x.prev
        print('>>> ' + ', '.join(ar) + ' >>> ' + ', '.join(rar))


    def _get_node(self, index):
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
        else:
            head = self.head
            while head.next is not None:
                head = head.next
            head.next = Node(item)
            head.next.prev = head
            self.size += 1

    def insert(self, index, item):
        '''Inserts an item at the given index, shifting remaining items right.'''
        index = int(index)
        n = self.head
        if self.head is None and index == 0:
            self.head = Node(item)
        for x in range(index - 1):
            if n.next is None:
                print('this index does not exist!')
                raise ValueError('Index out of range!')
            n = n.next
            n.next.prev = n
        next_node = n.next
        n.next = Node(item)
        n.next.next = next_node
        n.next.next.prev = n
        self.size += 1

    def set(self, index, item):
        index = int(index)

        '''Sets the given item at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        n = self.head
        for x in range(index):
            if n.next is None:
                print('this is no good')
                raise ValueError('Index out of range!')
            n = n.next
            n.next.prev = n
        n.value = item
        
    def get(self, index):
        index = int(index)
        '''Retrieves the item at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        n = self.head
        for i in range(index):
            if(n.next is None):
                print('index error!')
                raise ValueError
                return
            n = n.next
            n.next.prev = n
        return n.value
    
    def delete(self, index):
        
        '''Deletes the item at the given index. Throws an exception if the index is not within the bounds of the linked list.'''
        n = self.head
        if n is None:
            return
        try:
            ind = int(index)
            for i in range(ind):
                if n.next is None:
                    break
                n = n.next
            n.next = n.next.next
            n.next.next.prev = n
        except:
            pass
        for i in range(self.size - 1):
            if n.next.value is index:
                break
            if n.next is None:
                raise ValueError('n.next is none!')
            n = n.next
            # n.next.prev = n
        if n.next.next is not None:
            n.next = n.next.next
            n.next.prev = n

        self.size -= 1
    def swap(self, index1, index2):

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
# A node in the linked list
        
class Node(object):
    '''A node on the linked list'''
    
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
    def __str__(self):
        return '<Node: {}>'.format(self.value)

class DoublyLinkedListIterator(object):
    def __init__(self, doubly_linked_list):
        self.list = doubly_linked_list
        self.node = doubly_linked_list.head
        self.HEAD = doubly_linked_list.head
        
    def has_next(self):
        if self.node.next is not None:
            return True
        else:
            return False
    def has_prev(self):
        if self.node.prev is not None:
            return True
        else:
            return False
    
    def prev(self):
        '''returns the prev value'''
        if self.has_prev():
            self.node = self.node.prev
            return self.node.value

    def next(self):
        '''Returns the next value, and increments the iterator by one value.'''
        print('NEXT SONG EXISTS:', self.has_next())
        if self.has_next():
            self.node = self.node.next
            return self.node.value
        else:
            raise ValueError('next node does not exist')