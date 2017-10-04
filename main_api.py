#!/usr/bin/env python3
from circularlist_api import CircularLinkedList, CircularLinkedListIterator
from doublylinkedlist_api import DoublyLinkedList, DoublyLinkedListIterator
from stack_api import Stack
from queue_api import Queue


class Processor(object):
    
    def __init__(self):
        '''Creates the lists'''
        self.callahead = DoublyLinkedList()
        self.waiting = DoublyLinkedList()
        self.appetizers = Queue()
        self.buzzers = Stack()
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.songs = CircularLinkedList()
        self.songs.add('Song 1')
        self.songs.add('Song 2')
        self.songs.add('Song 3')
        self.songs_iter = CircularLinkedListIterator(self.songs)

    def run(self, f):
        '''Processes the given file stream.'''
        self.songs.debug_print()
        for line_i, line in enumerate(f):
            line = line.rstrip()
            comms = line.split(',')
            print('%d:%s'%(line_i,line))
            if comms[0] == 'SEAT':
                print('SEAT >>>>', line)
            elif comms[0] == 'APPETIZER':
                wait_iter = DoublyLinkedListIterator(self.waiting)
                while wait_iter.has_next():
                    wait_iter.next()
                count = 0
                person_array = []
                try:
                    food = self.appetizers.dequeue()
                except:
                    print('error')
                while wait_iter.has_prev() and count < 3:
                    person_array.append(wait_iter.node.value)
                    count += 1                    
                print('%s >>> %s' % (food, ', '.join(person_array)))
            elif comms[0] == 'SONG':
                self.songs_iter.next()
                print(self.songs_iter.node.value)
            elif comms[0] == 'LEAVE':
                self.waiting.delete(comms[1])
            elif comms[0] == 'DEBUG':
                self.debug()
            elif comms[0] == 'ARRIVE':
                self.waiting.add(comms[1])
                try:
                    self.callahead.delete(comms[1])
                except ValueError('error'):
                    continue
            elif comms[0] == 'CALL':
                self.callahead.add(comms[1])
            elif comms[0] == 'APPETIZER_READY':
                self.appetizers.enqueue(comms[1])
            else:
                print("ERROR!!!!!", line)
            # split and handle the commands here
            
    def debug(self):
        '''print all objects'''
        self.callahead.debug_print()
        self.waiting.debug_print()
        self.appetizers.debug_print()
        self.buzzers.debug_print()
        self.songs.debug_print()



#######################
###   Main loop

with open('data.csv', newline='') as f:
    processor = Processor()
    processor.run(f)

