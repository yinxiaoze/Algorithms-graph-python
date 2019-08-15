#队列是先进先出
import Node
class Queue:
    def __init__(self):
        self.first = Node.Node()
        self.N=0
        self.last = Node.Node()

    def isEmpty(self):
        #print(self.first)
        return self.N == 0

    def size(self):
        return self.N

    def enqueue(self,item):
        oldlast = self.last
        self.last = Node.Node()
        self.last.item = item
        if self.isEmpty():
            
            self.first = self.last
        else:
            #不知道有什么用
            oldlast.next = self.last
        self.N+=1

    def dequeue(self):
        item = self.first.item
        self.first = self.first.next
        if self.isEmpty():
            self.last.item = None
        self.N-=1
        return item
        
            
