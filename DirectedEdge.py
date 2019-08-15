#加权有向边
class DirectedEdge():
    def __init__(self,v,w,weight):
        self.v = v
        self.w = w
        self.weight = weight

    def froms(self):
        return self.v

    def tos(self):
        return self.w

    def __repr__(self):
        return str(self.v)+str(self.w)+str(self.weight)

'''a=DirectedEdge(1,2,3)
print(a)'''

    
