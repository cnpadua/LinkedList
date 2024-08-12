print("hello there")

class Node:

    def __init__(self):
        self.next = None
        self.previous = None

    def isTail(self) -> bool:
        ''' Returns true if current node is LinkedList tail '''
        return self.next == None
    
    def isHead(self) -> bool:
        ''' Returns true if current node is LinkedList head '''
        return self.previous == None
