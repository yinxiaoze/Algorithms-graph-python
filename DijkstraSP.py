#最短路径的Dijkstra算法
import Stack
import Bag
import DirectedEdge
import IndexMinPQ as PQ
import EdgeWeightedDigraph
class DijkstraSP():
    def __init__(self,graph,s):
        self.edgeTo = [None]*graph.V
        self.distTo = [float("inf")]*graph.V
        self.pq = PQ.IndexMinPQ(graph.V)
        self.s = s
        self.distTo[s] = 0.0
        self.pq.insert(s,0.0)
        while (self.pq.isEmpty()!=True):
            #print(self.pq.min())
            self.relax(graph,self.pq.delMin())
            
    def relax(self,graph,v):
        #print("vv",v)
        for e in graph.adj[v]:
            w = e.tos()
            #print("v",e)
            if self.distTo[w]>self.distTo[v]+e.weight:
                self.distTo[w] = self.distTo[v] + e.weight
                #print("e",e)
                self.edgeTo[w] = e
                if self.pq.contains(w):
                    self.pq.change(w,self.distTo[w])
                else:
                    self.pq.insert(w,self.distTo[w])
        
    def hasPathTo(self,v):
        return self.distTo[v]<float("inf")
    def pathTo(self,v):
        if self.hasPathTo(v) != True:
            return None
        path = Stack.Stack()
        e=self.edgeTo[v]
        while e!=None:
            #print(e)
            path.push(e)
            e = self.edgeTo[e.froms()]
        
        return path


    
'''import EdgeWeightedDigraph

    E = EdgeWeightedDigraph.EdgeWeightedDigraph(10)

    E.addEdge(DirectedEdge.DirectedEdge(1,2,50))
    #E.addEdge(DirectedEdge.DirectedEdge(1,3,float("inf")))
    E.addEdge(DirectedEdge.DirectedEdge(1,4,40))
    E.addEdge(DirectedEdge.DirectedEdge(1,5,25))
    E.addEdge(DirectedEdge.DirectedEdge(1,6,10))

    E.addEdge(DirectedEdge.DirectedEdge(2,1,50))
    E.addEdge(DirectedEdge.DirectedEdge(2,3,15))
    E.addEdge(DirectedEdge.DirectedEdge(2,4,20))
    #E.addEdge(DirectedEdge.DirectedEdge(2,5,float("inf")))
    E.addEdge(DirectedEdge.DirectedEdge(2,6,25))

    #E.addEdge(DirectedEdge.DirectedEdge(3,1,float("inf")))
    E.addEdge(DirectedEdge.DirectedEdge(3,2,15))
    E.addEdge(DirectedEdge.DirectedEdge(3,4,10))
    E.addEdge(DirectedEdge.DirectedEdge(3,5,20))
    E.addEdge(DirectedEdge.DirectedEdge(3,6,float("inf")))

    E.addEdge(DirectedEdge.DirectedEdge(4,1,40))
    E.addEdge(DirectedEdge.DirectedEdge(4,2,20))
    E.addEdge(DirectedEdge.DirectedEdge(4,3,10))
    E.addEdge(DirectedEdge.DirectedEdge(4,5,10))
    E.addEdge(DirectedEdge.DirectedEdge(4,6,25))

    E.addEdge(DirectedEdge.DirectedEdge(5,1,25))
    #E.addEdge(DirectedEdge.DirectedEdge(5,2,float("inf")))
    E.addEdge(DirectedEdge.DirectedEdge(5,3,20))
    E.addEdge(DirectedEdge.DirectedEdge(5,4,10))
    E.addEdge(DirectedEdge.DirectedEdge(5,6,55))

    E.addEdge(DirectedEdge.DirectedEdge(6,1,10))
    E.addEdge(DirectedEdge.DirectedEdge(6,2,25))
    E.addEdge(DirectedEdge.DirectedEdge(6,3,float("inf")))
    E.addEdge(DirectedEdge.DirectedEdge(6,4,25))
    E.addEdge(DirectedEdge.DirectedEdge(6,5,55))



D=DijkstraSP(E,1)
print(D.hasPathTo(3))
print(D.distTo[2],end=" ")'''







