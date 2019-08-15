#任意顶点之间的最短距离
import DijkstraSP
class DijkstraAllPairsSp():
    def __init__(self,graph):
        self.all = []
        for v in range(graph.V):
            self.all.append(DijkstraSP.DijkstraSP(graph,v))
    def path(self,s,t):
        return self.all[s].pathTo(t)

    def dist(self,s,t):
        return self.all[s].distTo(t)
        
