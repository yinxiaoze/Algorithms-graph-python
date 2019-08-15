#加权有向图数据类型
import Bag
import DirectedEdge
class EdgeWeightedDigraph():
    def __init__(self,a):
        if type(a) == int:
            self.V = a
            self.E = 0
            self.adj=[]
            for i in range(self.V):
                self.adj.append(Bag.Bag())

    def addEdge(self,e):
        self.adj[e.froms()].add(e)
        self.E+=1

    def edges(self):
        bag=Bag.Bag()
        for v in range(self.V):
            for e in self.adj[v]:
                bag.add(e)
        return bag


'''a=DirectedEdge.DirectedEdge(1,2,1)
b=DirectedEdge.DirectedEdge(2,3,1)
c=DirectedEdge.DirectedEdge(3,4,1)
d=DirectedEdge.DirectedEdge(4,5,1)
e=DirectedEdge.DirectedEdge(4,2,1)
E = EdgeWeightedDigraph(9)
E.addEdge(a)
E.addEdge(b)
E.addEdge(c)
E.addEdge(d)
E.addEdge(e)'''


        
            
        
