class Node:
    def __init__(self,name=None,next=None):
        self.item=name
        self.next=next
    def __repr__(self):
        return str(self.item)
        
