from linked_list import LinkedList

class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements? * Linked List *
        self.storage = LinkedList()

    def enqueue(self, item): # add  to tail  [item] ---> [12] ---> [23] ---> [4] head
        self.storage.add_to_tail(item)
        self.size += 1

    def dequeue(self): # remove and return an item from the front of the queue. removes from head
         if self.size > 0:
            self.size -= 1
            return self.storage.remove_head()

    def len(self):
        return self.size





