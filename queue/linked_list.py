class Node():
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node
    
    def get_value(self): # returns the current value
        return self.value

    def get_next(self): # pointer to next node
       return  self.next_node
       
    def set_next(self, new_next): # reassign pointer to next node pointer
        self.next_node = new_next

# value = 15
class LinkedList:
    # What does a linked list contain?
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
       
        # add value by wrapping it in a Node
        new_node = Node(value, None)
        # first check to see if out list has anything in it
        # if the head and tail are None add the new node to the linked list [] ----> [15]
        if self.head is None:
            self.head = new_node 
            self.tail = new_node
        
        # else set the next value as our new node value = 35 [35] ---> [15]
        else:
            self.tail.set_next(new_node)
            self.tail = new_node #now our tail is 35
    
   
    def remove_head(self):
            # if the list is empty
        if self.head == None:
            return None

        # references the head node to be changes
        current_head = self.head
          # to remove the head
            # take head and get the next node in line
            # set it as the head
        self.head = current_head.get_next()
        return current_head.get_value()
        # if the list only has one node return the node [15]
        # if the head and tail are the same
        if self.head is self.tail:
            current_head = self.head
            self.head = None
            self.tail = None
            # return the value of the node [15]
            return current_head.get_value()
        
        def contain(self, target):
            # If list is empty return false
            if not self.head and not self.tail:
                return False
            
            # set current value as self.head
            current = self.head

            # while current is true (if it not None) keep looping
            while current:
                # if the value is the same as the target return true this will break us out of the loop
                if current.get_value() == target:
                    return True

                else: # change the current to the next node and run if statements agin
                    current = current.get_next()
            return False # if nothing matches return false



 
          
        



