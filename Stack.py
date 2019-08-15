#栈是后进先出
import Node
class Stack():
    
    def __init__(self):
        self.N = 0
        self.first = Node.Node() 
        return
    
    def isEmpty(self):
        return self.N ==0
    
    def size(self):
        return self.N

    def push(self,item):
        oldfirst = self.first
        self.first = Node.Node()
        self.first.item = item
        self.first.next = oldfirst
        self.N+=1

    #从栈顶删除元素
    def pop(self):
        item = self.first.item
        self.first = self.first.next 
        self.N-=1
        return item
    def __repr__(self):
        diaoyong = self.first
        r=str(diaoyong.item)
        for i in range(self.size()-1):
            r+=str(diaoyong.next)
            diaoyong = diaoyong.next
        return r

'''a=Stack()
a.push("s")
a.push("d")
print(a)'''
    
    
        
