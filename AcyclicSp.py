#无环加权有向图的最短路径问题，比有环加权有向图快
import DirectedEdge as DE
class AcyclicSp():
    def __init__(self,graph,s):
        self.edgeTo = DE.DirectedEdge()
        self.distTo = [float("inf")]*graph.V
        self.distTo[s] = 0.0
