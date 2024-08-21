print("hello there")
'''
TODO
[] LinkedList from list constructor
[] LinkedList getNth node func
[] LinkedList getNthFromEnd func
[] LinkedList insert func
[] LinkedList remove (given key) func
[] LinkedList remove (given position)
[] LinkedList length func
[] Testing
'''
class Node:

    def __init__(self, val=None):
        self.next = None
        self.previous = None
        if val != None:
            self.value = val
        else:
            self.value = None

    def isTail(self) -> bool:
        ''' Returns true if current node is LinkedList tail '''
        return self.next == None
    
    def isHead(self) -> bool:
        ''' Returns true if current node is LinkedList head '''
        return self.previous == None

    def getValue(self):
        return self.value

class LinkedList:

    def __init__(self, initial_value=None):
        ''' Current implentation always assumes LinkedList starts empty '''
        if initial_value != None:
            self.head = Node(initial_value)
        else:
            self.head = Node()
    
    @classmethod
    def fromList(cls, list):

        return self