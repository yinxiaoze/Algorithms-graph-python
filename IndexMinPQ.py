#索引优先队列
class IndexMinPQ():
    def __init__(self,maxN):
        self.N = 0
        self.keys = [0]*(maxN+1)
        self.pq = [0]*(maxN+1)
        self.qp = [-1]*(maxN+1)
    
    def isEmpty(self):
        return self.N == 0
    
    def contains(self,k):
        return self.qp[k] !=  -1
    
    def insert(self,k,key):
        
        self.N+=1
        self.qp[k] = self.N
        self.pq[self.N] = k
        self.keys[k] = key
        self.swim(self.N)

    def change(self,k,item):
        #print("kkkkkkkkkk",item)
        self.keys[k] = item
        self.swim(self.qp[k])
        self.sink(self.qp[k])
        #self.pq[k] = item
    
    def min(self):
        return self.keys[self.pq[1]]
    
    def less(self,i,j):
        i = int(i)
        j = int(j)
        #print("len",len(self.pq))
        #print(i,j)
        #for i in self.pq:
            #print(i)
        #print("sdasds",self.pq[i],self.pq[j])
        #print(self.pq[0],self.pq[1],self.pq[2],self.pq[3])
        return self.keys[int(self.pq[i])]>self.keys[int(self.pq[j])]

    def exch(self,i,j):
        i = int(i)
        j = int(j)
        t = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = t
        self.qp[self.pq[i]]=i
        self.qp[self.pq[j]]=j

    def swim(self,k):
        k=int(k)
        while (k>1)&self.less(k/2,k):
            self.exch(k/2,k)
            k=k/2

    def sink(self,k):
        k= int(k)
        while 2*k<=self.N:
            j = 2*k
            #print("j",j)
            if (j<self.N)&self.less(j,j+1):
                j+=1
            if self.less(k,j) != True:
                break

            self.exch(k,j)
            k=j
    def delMin(self):
        indexOfMin = self.pq[1]
        #self.N-=1
        self.exch(1,self.N)
        self.N-=1
        self.sink(1)
        self.qp[indexOfMin] = -1
        self.keys[indexOfMin] = 0
        
        self.pq[self.N+1] = -1
        
        #print(self.pq[self.N+1])
        #self.keys[self.pq[self.N+1]] = None
        #self.qp[self.pq[self.N+1]] = -1
        
        return indexOfMin
        

'''a= IndexMinPQ(6)
#a.insert(0,1)
a.insert(3,2)
a.insert(1,5)
a.insert(5,4)
print(a.min())
a.delMin()
print(a.min())
#a.delMin()
#print(a.delMin())'''
