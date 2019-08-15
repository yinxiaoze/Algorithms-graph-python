class Bag():
    import copy
    N=0
    class Node:
        def __init__(self,name=None,next=None):
            self.item=name
            self.next=next
        def __repr__(self):
            return self.item
    
    def __init__(self):
        return
    first = Node()
    def add(self,item):
        oldfirst = self.first
        self.first = self.Node()
        self.first.item=item
        
        self.first.next = oldfirst
        self.N+=1
    def size(self):
        return N
    def isEmpty(self):
        if self.N==0:
            return True
        else:
            return False

    def __iter__(self):
        return self  

    def __next__(self):
        
        if self.first.item != None:
            a=self.first.item
            self.first = self.first.next
            return a
            
        else:
            raise StopIteration  # 抛出异常停止遍历
        
